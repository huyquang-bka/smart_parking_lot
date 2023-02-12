#!/usr/bin/env bash

git add .
git commit -m "update"
git pull
conda activate base
python main.py