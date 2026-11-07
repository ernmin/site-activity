import pandas as pd
import numpy as np
import json
from add_row import *
from delete_row import *
from column_config import *
# THINK ABOUT HOW TO MINIMIZE CONVERTING TO A DF
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
        delete_site_activity(df)
        
        

