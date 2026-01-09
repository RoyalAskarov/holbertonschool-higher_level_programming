#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list,
and then saves them to a file named add_item.json.
"""
import sys

# Importing required functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try to load the existing list from the file
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, initialize an empty list
    items = []

# Add all command-line arguments to the list (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
