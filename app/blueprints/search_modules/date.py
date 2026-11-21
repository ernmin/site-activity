import pandas as pd
import duckdb
from app.load_json import all_df

def search_date(from_date, to_date):
    site_activity = all_df['site_activity']
    query = """
    SELECT *
    FROM site_activity
    WHERE 1=1
    AND Date_of_Site_Activity > $from_date
    AND Date_of_Site_Activity < $to_date

    """
    result_df = duckdb.query(query, params={"from_date": from_date, "to_date": to_date}).to_df()
    return result_df