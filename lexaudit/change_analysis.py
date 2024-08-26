import json
import os

def load_version_control(filename):
    """
    Load the version control data from a JSON file if the file is a JSON file.

    :param filename: The name of the file to load.
    :return: The content of the JSON file if it is JSON, otherwise return None.
    """
    if filename.endswith('.json'):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        print(f"File '{filename}' is not a JSON file. Skipping JSON parsing.")
        return None
