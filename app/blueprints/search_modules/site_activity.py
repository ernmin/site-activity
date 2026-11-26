import pandas as pd
import duckdb
from app.load_json import all_df

def search_site_activity(PK):
    site_activity = all_df['site_activity']
    query = """
    SELECT *
    FROM site_activity
    WHERE 1=1
    AND PK = $PK

    """
    result_df = duckdb.query(query, params={"PK": PK}).to_df().to_dict(orient='records')
    print(result_df)
    return result_df