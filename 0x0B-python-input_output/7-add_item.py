#!/usr/bin/python3
""" Module Doc"""


import sys
save = __import__('5-save_to_json_file.py').save_to_json_file
load = __import__('6-load_from_json_file.py').load_from_json_file

f = open("add_item.json", 'a', encoding="utf-8")
f.close()

if sys.argv > 1:
    listed = str(sys.argv[1:])
else:
    listed = list()

save1 = save()
load1 = load()
my_dir = load1("add_item.json")

my_dir += listed

save1(my_dir, "add_item.json")
