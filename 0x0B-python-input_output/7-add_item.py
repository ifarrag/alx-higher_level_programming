#!/usr/bin/python3
""" Module Doc"""


import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

diss = 1
f = open("add_item.json", 'a+', encoding="utf-8")
if f.tell() == 0:
    diss = 0
f.close()

listed = list()
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        listed.append(sys.argv[i])

if diss == 1:
    my_dir = load("add_item.json")
    my_dir += listed
else:
    my_dir = listed

save(my_dir, "add_item.json")
