# coding=utf-8

import time
import os
import json

json_file = "driver.json"

def load_file():
    if os.path.exists(json_file):
        with open("driver.json", mode='r') as ff:
            b = json.load(ff)
            return b
    else:
        with open(json_file, mode='w', encoding='utf-8') as f:
            json.dump({}, f)
            return {}

with open("driver.json", mode='r') as ff:
    b = json.load(ff)
print(b)