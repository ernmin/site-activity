import json
import os
from column_config import *

def delete_site_activity(df):
    timestamp = df['Timestamp'].iloc[0]
    date_site_activity = df['Date of Site Activity'].iloc[0]
    print(timestamp, date_site_activity)
    print(find_primary_key(timestamp, date_site_activity))

def find_primary_key(timestamp, date_site_activity):
    with open(folder_path + 'site_activity.json', 'r') as file:
        site_activity_list = json.load(file)
    for item in site_activity_list:
        if timestamp == item['Timestamp'] and date_site_activity == item['Date of Site Activity']:
            delete_all_assoc_entries(item['PK'])
            # return item['PK']

def delete_all_assoc_entries(PK):
    for item in os.listdir(folder_path):
        # Get the full path of the item
        full_path = os.path.join(folder_path, item)
        #CHANGE FILE NAMES TO VARIABLES
        if item != 'key_info.json':
            with open(full_path, 'r') as file:
                json_file_list = json.load(file)

            remain = remain_delete(json_file_list, PK)
            
            with open(full_path, 'w') as file:
                json.dump(remain, file, indent=4)

def remain_delete(json_file_list, PK):
    remaining_list = []
    delete_list = []
    for item in json_file_list:
        if item.get('FK') is not None:
            if PK == item['FK']:
                delete_list.append(item)
            else:
                remaining_list.append(item)
            
        elif item.get('PK') is not None:
            if PK == item['PK']:
                delete_list.append(item)
            else:
                remaining_list.append(item)
    return remaining_list