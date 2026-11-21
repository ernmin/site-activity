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
        print(full_path)
        with open(full_path, 'r') as file:
            new_table = json.load(file)
        idx = item.index('.')
        all_df[item[:idx]] = pd.DataFrame(new_table)
        all_df[item[:idx]].columns = all_df[item[:idx]].columns.str.replace(" ", "_")
        new_columns = [all_df[item[:idx]].columns[-1]] + list(all_df[item[:idx]].columns[:-1])
        all_df[item[:idx]] = all_df[item[:idx]][new_columns]