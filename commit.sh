#!/usr/bin/env bash

export EDITOR=mousepad
./clean.sh
git add .
git checkout devel
git commit -a
git checkout master
git merge devel
git push origin master


