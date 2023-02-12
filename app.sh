#!/usr/bin/env bash

git add .
git commit -m "update"
git pull
cd ${pwd}
conda run -n base python main.py