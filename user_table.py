import pandas as pd
import numpy as np
import json

folder_path = "json_files/"

# from return_entries import refresh_data_cache


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


    # have a list of the expected fields
    # combine into 2 functions, 1 type needing to split based on commas, another expecting a single field
    # arguments to take in are the df, next_pk, field to focus on, file to write to

    add_subsystem(df, next_pk)
    site_activity_list_new[0].pop("Subsystem", None)
    add_systembaseline(df, next_pk)
    site_activity_list_new[0].pop("System Baseline", None)
    add_media(df, next_pk)
    site_activity_list_new[0].pop("Photos or Videos", None)

    site_activity_list_new[0]['PK'] = next_pk
    site_activity_list_join = site_activity_list + site_activity_list_new
    with open(folder_path + 'site_activity.json', 'w') as file:
        json.dump(site_activity_list_join, file, indent=4)
    with open(folder_path + 'key_info.json', 'w') as file:
        json.dump(key_info, file, indent=4)

def add_subsystem(df, next_pk):
    subsystem_entry = df.to_dict(orient='records')
    subsystem_string = subsystem_entry[0]["Subsystem"]
    subsystem_list_new = subsystem_string.split(",")
    with open(folder_path + 'subsystem.json', 'r') as file:
        subsystem_list = json.load(file)
        
    for item in subsystem_list_new:
        subsystem_entry_new = [{next_pk: item}]
        subsystem_list = subsystem_list + subsystem_entry_new
    
    with open(folder_path + 'subsystem.json', 'w') as file:
        json.dump(subsystem_list, file, indent=4)

def add_systembaseline(df, next_pk):
    systembaseline_entry =  df.to_dict(orient='records')
    systembaseline_entry_new = [{next_pk: systembaseline_entry[0]["System Baseline"]}]
    with open(folder_path + 'systembaseline.json', 'r') as file:
        systembaseline_list = json.load(file)
    systembaseline_list = systembaseline_list + systembaseline_entry_new
    with open(folder_path + 'systembaseline.json', 'w') as file:
            json.dump(systembaseline_list, file, indent=4)

def add_media(df, next_pk):
    media_entry = df.to_dict(orient='records')
    media_string = media_entry[0]["Photos or Videos"]
    media_list_new = media_string.split(",")
    with open(folder_path + 'media.json', 'r') as file:
        media_list = json.load(file)
        
    for item in media_list_new:
        media_entry_new = [{next_pk: item}]
        media_list = media_list + media_entry_new
    
    with open(folder_path + 'media.json', 'w') as file:
        json.dump(media_list, file, indent=4)

