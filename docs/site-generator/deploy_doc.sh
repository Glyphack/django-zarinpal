#!/bin/bash

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"
cd ../dist
rm -rf .
cd ../site-generator
# Build the project.
hugo

# Add changes to git.
cd ..
git add .

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"
cd ..
# Push source and build repos.
git subtree push --prefix docs/dist origin gh-pages