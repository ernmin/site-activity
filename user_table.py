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
        # add_photo(df)

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


def add_rows(collapsed_df):
    """
    Put whatever your python script is supposed to 'check' or do with the data here.
    """
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


def add_photo(df):
    with open('output.json', 'r') as file:
        photo_list = json.load(file)
    photo_list_new = df.to_dict(orient='records')
    photo_list_join = photo_list + photo_list_new
    with open('output.json', 'w') as file:
        json.dump(photo_list_join, file, indent=4)

def delete_photo(df):
    with open('output.json', 'r') as file:
        photo_list = json.load(file)
    photo_delete = df.to_dict(orient='records')
    print(photo_delete)
    for row in photo_list:
        if row['Upload your photo!'] == photo_delete[0]['Upload your photo!']:
            photo_list.remove(row)
    with open('output.json', 'w') as file:
        json.dump(photo_list, file, indent=4)