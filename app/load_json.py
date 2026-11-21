import json
import pandas as pd
import os
import duckdb
folder_path = "json_files/"

all_df = {}


def init_db():
    for item in os.listdir(folder_path):
        # Get the full path of the item
        full_path = os.path.join(folder_path, item)
        
        with open(full_path, 'r') as file:
            new_table = json.load(file)
        idx = item.index('.')
        all_df[item[:idx]] = pd.DataFrame(new_table)
        all_df[item[:idx]].columns = all_df[item[:idx]].columns.str.replace(" ", "_")
        new_columns = [all_df[item[:idx]].columns[-1]] + list(all_df[item[:idx]].columns[:-1])
        all_df[item[:idx]] = all_df[item[:idx]][new_columns]
        

def timestamp():
    all_df['raw']['Timestamp'] = pd.to_datetime(all_df['raw']['Timestamp'])
    all_df['raw']['Date_of_Site_Activity'] = pd.to_datetime(all_df['raw']['Date_of_Site_Activity'])
    all_df['site_activity']['Timestamp'] = pd.to_datetime(all_df['site_activity']['Timestamp'])
    all_df['site_activity']['Date_of_Site_Activity'] = pd.to_datetime(all_df['site_activity']['Date_of_Site_Activity'])