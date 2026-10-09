import pandas as pd
import numpy as np
import json

folder_path = "json_files/"

# from return_entries import refresh_data_cache

csv_column = ["Subsystem", "Photos or Videos", "System Baseline"]
csv_file = ["subsystem", "media", "systembaseline"]
personnel_column = ["JRLP (Separate name by a comma and space)", "J152 (Separate name by a comma and space)"]
test_column = ["Test Cases Passed (Separate each test case conducted by a comma and space)", "Test Cases Failed (Separate each test case conducted by a comma and space)", "Test Cases Pending (Separate each test case conducted by a comma and space)"]
ISF_column = ["ISFs Opened (Separate each ISF by a comma and space)", "ISFs Closed (Separate each ISF by a comma and space)"]

def transform_and_process_row(row_data, headers, row_index, cell_value):
    """
    This function accepts the raw data from server.py,
    transforms it into a usable structure, and processes it.
    """
    print(f"\n⚙️ [Processor] Starting data transformation for Sheet Row {row_index}...")
    
    # 1. Convert the single row lists into a Pandas DataFrame
    df = pd.DataFrame([row_data], columns=headers)
    # df.to_json('output.json', orient='records', indent=4)
    if cell_value == '1':
        print('add')
        add_site_activity(df)

    elif cell_value == '0':
        print('delete')
        # delete_photo(df)

    print(df)


def add_site_activity(df):
    site_activity_list_new = df.to_dict(orient='records')
    with open(folder_path + 'key_info.json', 'r') as file:
        key_info = json.load(file)
    next_pk = key_info[0]["last_pk"] + 1
    key_info[0]["last_pk"] += 1
    with open(folder_path + 'site_activity.json', 'r') as file:
        site_activity_list = json.load(file)

    # no_csv_column = ["System Baseline"]
    # no_csv_file = ["systembaseline"]
    
    # have a list of the expected fields
    # combine into 2 functions, 1 type needing to split based on commas, another expecting a single field
    # arguments to take in are the df, next_pk, field to focus on, file to write to

    # for i in range(len(no_csv_column)):
    #     add_no_csv(df, next_pk, no_csv_column[i], no_csv_file[i])
    #     site_activity_list_new[0].pop(no_csv_column[i], None)

    for i in range(len(csv_column)):
        add_csv(df, next_pk, csv_column[i], csv_file[i])
        site_activity_list_new[0].pop(csv_column[i], None)

    for column in personnel_column:
        add_personnel(df, next_pk, column)
        site_activity_list_new[0].pop(column, None)

    for column in test_column:
        add_test(df, next_pk, column)
        site_activity_list_new[0].pop(column, None)
    
    site_activity_list_new[0]['PK'] = next_pk
    site_activity_list_join = site_activity_list + site_activity_list_new
    with open(folder_path + 'site_activity.json', 'w') as file:
        json.dump(site_activity_list_join, file, indent=4)
    with open(folder_path + 'key_info.json', 'w') as file:
        json.dump(key_info, file, indent=4)


# def add_no_csv(df, next_pk, column_name, file_name):
#     entry =  df.to_dict(orient='records')
#     entry_new = [{next_pk: entry[0][column_name]}]
#     with open(folder_path + file_name + '.json', 'r') as file:
#         memory_list = json.load(file)
#     memory_list = memory_list + entry_new
#     with open(folder_path + file_name + '.json', 'w') as file:
#             json.dump(memory_list, file, indent=4)


def add_csv(df, next_pk, column_name, file_name):
    entry = df.to_dict(orient='records')
    column_string = entry[0][column_name]
    list_new = column_string.split(", ")
    with open(folder_path + file_name + '.json', 'r') as file:
        memory_list = json.load(file)

    for item in list_new:
        entry_new = [{'FK':next_pk, file_name: item}]
        memory_list = memory_list + entry_new
    
    with open(folder_path + file_name + '.json', 'w') as file:
        json.dump(memory_list, file, indent=4)

def add_personnel(df, next_pk, column_name):
    entry = df.to_dict(orient='records')
    column_string = entry[0][column_name]
    list_new = column_string.split(", ")
    with open(folder_path + 'personnel.json', 'r') as file:
        memory_list = json.load(file)

    for item in list_new:
        entry_new = [{'FK':next_pk, 'name': item, "team": column_name[:4]}]
        memory_list = memory_list + entry_new
    
    with open(folder_path + 'personnel.json', 'w') as file:
        json.dump(memory_list, file, indent=4)

def add_test(df, next_pk, column_name):
    entry = df.to_dict(orient='records')
    column_string = entry[0][column_name]
    list_new = column_string.split(", ")
    with open(folder_path + 'test.json', 'r') as file:
        memory_list = json.load(file)

    for item in list_new:
        entry_new = [{'FK':next_pk, 'test': item, "status": column_name[11:15]}]
        memory_list = memory_list + entry_new
    
    with open(folder_path + 'test.json', 'w') as file:
        json.dump(memory_list, file, indent=4)