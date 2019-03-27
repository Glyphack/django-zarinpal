#!/bin/bash

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# Build the project.
hugo

# Add changes to git.
git add -A

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"
cd ../..
# Push source and build repos.
git subtree push --prefix docs/public origin gh-pages
# git subtree push --prefix=public https://github.com/[github username]/blog.git gh-pages