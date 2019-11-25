#!/bin/bash
sudo apt install python-virtualenv
virtualenv --python=python3 myvenv
source myvenv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
