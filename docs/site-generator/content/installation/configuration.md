+++
title= "Configuration"
date= 2019-03-27T09:18:15+04:30
draft= false
description = ""
weight= 2
+++

<!--more-->

Add zarinpal to your installed apps
```
INSTALLED_APPS = [
...
"zarinpal",
...
```

there are some variables that indicates how you want to work with django-zarinpal:

1.ZARINPAL_CALLBACK_URL(if you want to handle verification yourself)

2.ZARINPAL_SIMULATION(if you want to try package in sandbox mode without any api key)

3.ZARINPAL_MERCHANT_ID (it is your api key, you may leave it blank if you set the simulation to True)