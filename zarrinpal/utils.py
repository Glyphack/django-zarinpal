from zeep import Client

ZARINPAL_WEBSERVICE = 'https://sandbox.zarinpal.com/pg/services/WebGate/wsdl'  # Required
MMERCHANT_ID = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'  # Required
amount = 100


def start_transaction(transaction_data: dict, test_mode: bool) -> str:
    amount = ''
    description = u'توضیحات تراکنش تستی'  # Required
    email = 'user@userurl.ir'  # Optional
    mobile = '09123456789'  # Optional
    CallbackURL = 'http://127.0.0.1:8000/order/verify/'
    client = Client(ZARINPAL_WEBSERVICE)
    result = client.service.PaymentRequest(
        MMERCHANT_ID,
        amount,
        description,
        email,
        mobile,
        CallbackURL)
    if result.Status == 100:
        return 'https://sandbox.zarinpal.com/pg/StartPay/' + result.Authority


def verify_transaction(request):
    client = Client(ZARINPAL_WEBSERVICE)
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MMERCHANT_ID,
                                                    request.GET['Authority'],
                                                    amount)
        if result.Status == 100:
            order = Order.objects.create(
                user=request.user,
                paid=True
            )
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    item=get_object_or_404(Dota2Item, pk=item),
                    price=cart[item]['price']
                )
                Dota2Item.objects.filter(pk=item).update(quantity=0)
            del request.session['total_price']
            del request.session['cart']
            context = {
                'message': "خرید شما با موفقیت انجام شد شماره : {}".format(result.RefID)
            }
            return render(request, 'order/success.html', context)
        elif result.Status == 101:
            context = {
                'message': "خرید ثبت شد : {}".format(result.Status)
            }
            return render(request, 'order/success.html', context)
        else:
            context = {
                'message': "خرید با شکست مواجه شد : {}".format(result.Status)
            }
            return render(request, 'order/failed.html', context)
    else:
        context = {
            'message': "توسط کاربر کنسل شد"
        }
        return render(request, 'order/failed.html', context)
