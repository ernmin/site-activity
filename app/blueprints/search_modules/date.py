import pandas as pd
import duckdb

def search_date(from_date, to_date):
    query = """
    SELECT *
    FROM site_activity
    WHERE 1=1
    AND Date_of_Site_Activity > $from_date
    AND Date_of_Site_Activity < $to_date

    """
    result_df = duckdb.query(query, params={"from_date": from_date, "to_date": to_date}).to_df()
    return result_df