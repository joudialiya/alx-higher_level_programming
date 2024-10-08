#!/usr/bin/python3
"""Serialize argv"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    file_name = "add_item.json"
    try:
        my_list = load_from_json_file(file_name)
    except FileNotFoundError:
        my_list = []
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, file_name)
