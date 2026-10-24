
import json
from column_config import *

def add_site_activity(df):
    site_activity_list_new = df.to_dict(orient='records')
    with open(folder_path + 'key_info.json', 'r') as file:
        key_info = json.load(file)
    next_pk = key_info[0]["last_pk"] + 1
    key_info[0]["last_pk"] += 1
    add_raw(df, next_pk)

    with open(folder_path + 'site_activity.json', 'r') as file:
        site_activity_list = json.load(file)

    for i in range(len(csv_column)):
        add_csv(df, next_pk, csv_column[i], csv_file[i])
        site_activity_list_new[0].pop(csv_column[i], None)

    for column in personnel_column:
        add_personnel(df, next_pk, column)
        site_activity_list_new[0].pop(column, None)

    for column in test_column:
        add_test(df, next_pk, column)
        site_activity_list_new[0].pop(column, None)

    for column in ISF_column:
        add_ISF(df, next_pk, column)
        site_activity_list_new[0].pop(column, None)

    
    site_activity_list_new[0]['PK'] = next_pk
    site_activity_list_join = site_activity_list + site_activity_list_new
    with open(folder_path + 'site_activity.json', 'w') as file:
        json.dump(site_activity_list_join, file, indent=4)
    with open(folder_path + 'key_info.json', 'w') as file:
        json.dump(key_info, file, indent=4)

def add_raw(df, next_pk):
    raw_list_new = df.to_dict(orient='records')
    with open(folder_path + 'raw.json', 'r') as file:
        raw_list = json.load(file)
    raw_list_new[0]['PK'] = next_pk
    raw_list_join = raw_list + raw_list_new
    with open(folder_path + 'raw.json', 'w') as file:
        json.dump(raw_list_join, file, indent=4)

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
        entry_new = [{'FK':next_pk, 'test': item, "status": column_name[11:]}]
        memory_list = memory_list + entry_new
    
    with open(folder_path + 'test.json', 'w') as file:
        json.dump(memory_list, file, indent=4)

def add_ISF(df, next_pk, column_name):
    entry = df.to_dict(orient='records')
    column_string = entry[0][column_name]
    list_new = column_string.split(", ")
    with open(folder_path + 'ISF.json', 'r') as file:
        memory_list = json.load(file)

    for item in list_new:
        entry_new = [{'FK':next_pk, 'ISF': item, "status": column_name[4:]}]
        memory_list = memory_list + entry_new
    
    with open(folder_path + 'ISF.json', 'w') as file:
        json.dump(memory_list, file, indent=4)