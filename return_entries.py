import pandas as pd
import json

_user_table_cache = None
_output_cache = None


def refresh_data_cache():
    global _user_table_cache, _output_cache
    with open('user_table.json', 'r') as file:
        _user_table_cache = json.load(file)
    with open('output.json', 'r') as file:
        _output_cache = json.load(file)


refresh_data_cache()


def return_entries(requestedUser):
    user_table_list = _user_table_cache
    if user_table_list is None:
        refresh_data_cache()
        user_table_list = _user_table_cache

    df = pd.DataFrame(user_table_list)
    df_filtered = df[df['ID'] == requestedUser]
    df_filtered_no_time = df_filtered[['ID', 'Photo', 'Question']]
    df_filtered_no_time = df_filtered_no_time.sort_values(by='Question')
    json_filtered = df_filtered_no_time.to_dict(orient='records')
    return json_filtered


def return_all_entries():
    photo_list = _output_cache
    if photo_list is None:
        refresh_data_cache()
        photo_list = _output_cache

    df = pd.DataFrame(photo_list)
    df = df.rename(columns={'Upload your photo!': 'Photo', 'Which question is this photo for?': 'Question'})
    df['ID'] = '-'
    df = df[['ID', 'Photo', 'Question']]
    json_filtered = df.to_dict(orient='records')
    return json_filtered

# def return_error():
#     return [{'ID': '-', 'Photo': 'You clicked too much', 'Question': '-'}]