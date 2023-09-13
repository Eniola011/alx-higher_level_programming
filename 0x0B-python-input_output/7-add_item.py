#!/usr/bin/python3
"""

7-add_item.py

"""


import os.path
import sys
import json


save_the_file = __import__('5-save_to_json_file').save_to_json_file
load_the_file = __import__('6-load_from_json_file').load_from_json_file

the_list = []

if os.path.exists("add_item.json"):
    the_list = load_the_file("add_item.json")

for arg in sys.argv[1:]:
    the_list.append(arg)

save_the_file(the_list, "add_item.json")
