# Task
# Create a Python function called process_json(data: dict, filename: str) -> dict that does the following:

# Takes a dictionary (data) and a filename (filename) as input.
# Serializes the dictionary to a JSON file with the given filename.
# Deserializes the JSON file back into a dictionary.
# Returns the deserialized dictionary.

import json

data={
    'name': 'Godfred',
    'occupation': 'Digital officer',
    'salary': '7000',
}

def process_write_data_json(data,file):
    
    try:
        with open(file,'w') as f:
            json.dump(data,f)
    except FileNotFoundError:
        print('File Not Found')
        

def process_read_data_json(file):
    with open(file,'r') as f:
        jsonData = json.load(f)
        
    print(jsonData)

    print(f"\nEmployee Details\n________________________\n\nName: {jsonData['name']}\nPosition: {jsonData['occupation']}")

process_write_data_json(data,'info.json')

process_read_data_json('info.json')