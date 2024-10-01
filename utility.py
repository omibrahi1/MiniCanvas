"""
File Name: utility.py
    Purpose: This file is the utility file of the program 
    where the main unique functions and csvs are defined.
First Create Date: 10/20/2023
Last Update Date: 11/28/2023
Author: Omar Ibrahim
Version: 1.1
"""
import csv
import os

import csv
import os

def load_csv(file_path, obj_class):
    # If the file doesn't exist, create it with headers
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=obj_class.__init__.__code__.co_varnames[1:])
            writer.writeheader()

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        rows = []

        # Check if the CSV file is empty
        if not reader.fieldnames:
            return []

        for row in reader:
            # all keys are strings
            row = {str(k): v for k, v in row.items()}
            # all required keys are present
            if all(key in row for key in obj_class.__init__.__code__.co_varnames[1:]):
                rows.append(row)

        return [obj_class(**row) for row in rows]



    
    
def load_admin_csv(file_path, obj_class):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [obj_class(**row) for row in reader]



def save_to_csv(file_path, data):
    with open(file_path, 'a', newline='') as file:
        if not data:
            return  # No data to save

        # Assuming data[0] is a dictionary
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # If the file is empty, write the headers
        if file.tell() == 0:
            writer.writeheader()

        # Write the data rows
        writer.writerow(data[-1])


def is_unique(data, new_value, keys):
    if isinstance(keys, str):
        keys = (keys,)

    return all(new_value != tuple(getattr(obj, str(key)) for key in keys) for obj in data)




def get_formatted_output(data):
    if not data:
        return "No data available."

    headers = list(data[0].__dict__.keys())

    # maximum width for each column
    column_widths = {}
    for header in headers:
        max_width = max(len(header), max(len(str(getattr(obj, header))) for obj in data))
        column_widths[header] = max_width

    # Generate the separator line
    separator = "+".join("-" * (column_widths[header] + 2) for header in headers)
    separator = f"+{separator}+"

    # Generate the header row
    header_row = "|"
    for header in headers:
        header_row += f" {header.ljust(column_widths[header])} |"
    output = f"{separator}\n{header_row}\n{separator}\n"

    # Generate data rows
    for obj in data:
        row = "|"
        for header in headers:
            value = str(getattr(obj, header)).ljust(column_widths[header])
            row += f" {value} |"
        output += f"{row}\n"

    output += separator
    return output


