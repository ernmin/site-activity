import pandas as pd
import duckdb
from app.load_json import all_df

def search_site_activity(PK):
    site_activity = all_df['site_activity']
    media = all_df['media']
    query = """
    SELECT PK AS ID, Date_of_Site_Activity AS Date, Title
    FROM site_activity
    JOIN media ON site_activity.PK = media.FK
    WHERE 1=1
    AND PK = $PK

    """
    result_df = duckdb.query(query, params={"PK": PK}).to_df().to_dict(orient='records')
    print(result_df)
    return result_df