import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and writes its content to 'data.json'.
    Returns True if successful, False otherwise.
    """
    try:
        data_list = []
        # Use DictReader to convert each row into a dictionary
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        # Serialize the list of dictionaries to 'data.json'
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True
    except (FileNotFoundError, Exception):
        # Return False if the file is not found or another error occurs
        return False