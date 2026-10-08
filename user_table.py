import pandas as pd
import numpy as np
import json

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


    # df = df.rename(columns={'Upload your photo!': 'Photo', 'Which question is this photo for?': 'Question'})
    # df.drop(columns=['Approved'], inplace=True)
    # collapsed_df = pd.melt(df, id_vars=["Timestamp", "Photo", "Question"], value_vars=[f"Person {i} ID" for i in range(1,11)], value_name="ID",).drop(columns=['variable'])
    # collapsed_df["ID"] = (collapsed_df["ID"].astype(str).str.strip().replace(["", "None", "NaN", "nan"], np.nan))
    # collapsed_df = collapsed_df.dropna(subset=["ID"])
    # collapsed_df = collapsed_df[['ID', 'Photo', 'Question', 'Timestamp']]

    # if cell_value == '1':
    #     add_rows(collapsed_df)

    # elif cell_value == '0':
    #     delete_rows(collapsed_df)

    # refresh_data_cache()

"""
def add_rows(collapsed_df):
    
    print("🚀 [Processor] Running analysis workflow on the cleaned record...")

    with open('user_table.json', 'r') as file:
        user_table_list = json.load(file)
    
    user_table_new = collapsed_df.to_dict(orient='records')
    # print(user_table_new)
    user_table_join = user_table_list + user_table_new
    with open('user_table.json', 'w') as file:
        json.dump(user_table_join, file, indent=4)
    
def delete_rows(collapsed_df):
    with open('user_table.json', 'r') as file:
        user_table_list = json.load(file)
    user_table_delete = collapsed_df.to_dict(orient='records')
    user_table_new = [row for row in user_table_list if row['Photo'] != user_table_delete[0]['Photo']]
    # for row in user_table_list:
    #     if row['Link'] == user_table_delete[0]['Link']:
    #         user_table_list.remove(row)
    with open('user_table.json', 'w') as file:
        json.dump(user_table_new, file, indent=4)

        """


def add_site_activity(df):
    site_activity_list_new = df.to_dict(orient='records')
    with open('key_info.json', 'r') as file:
        key_info = json.load(file)
    next_pk = key_info[0]["last_pk"] + 1
    key_info[0]["last_pk"] += 1
    with open('site_activity.json', 'r') as file:
        site_activity_list = json.load(file)
    add_subsystem(df, next_pk)
    site_activity_list_new[0].pop("Subsystem", None)
    add_systembaseline(df, next_pk)
    site_activity_list_new[0].pop("System Baseline", None)

    site_activity_list_new[0]['PK'] = next_pk
    site_activity_list_join = site_activity_list + site_activity_list_new
    with open('site_activity.json', 'w') as file:
        json.dump(site_activity_list_join, file, indent=4)
    with open('key_info.json', 'w') as file:
        json.dump(key_info, file, indent=4)

def add_subsystem(df, next_pk):
    subsystem_entry = df.to_dict(orient='records')
    subsystem_string = subsystem_entry[0]["Subsystem"]
    subsystem_list_new = subsystem_string.split(",")
    with open('subsystem.json', 'r') as file:
        subsystem_list = json.load(file)
        
    for item in subsystem_list_new:
        subsystem_entry_new = [{next_pk: item}]
        subsystem_list = subsystem_list + subsystem_entry_new
    
    with open('subsystem.json', 'w') as file:
        json.dump(subsystem_list, file, indent=4)

def add_systembaseline(df, next_pk):
    systembaseline_entry =  df.to_dict(orient='records')
    systembaseline_entry_new = [{next_pk: systembaseline_entry[0]["System Baseline"]}]
    with open('systembaseline.json', 'r') as file:
        systembaseline_list = json.load(file)
    systembaseline_list = systembaseline_list + systembaseline_entry_new
    with open('systembaseline.json', 'w') as file:
            json.dump(systembaseline_list, file, indent=4)

# def delete_photo(df):
#     with open('output.json', 'r') as file:
#         photo_list = json.load(file)
#     photo_delete = df.to_dict(orient='records')
#     print(photo_delete)
#     for row in photo_list:
#         if row['Upload your photo!'] == photo_delete[0]['Upload your photo!']:
#             photo_list.remove(row)
#     with open('output.json', 'w') as file:
#         json.dump(photo_list, file, indent=4)