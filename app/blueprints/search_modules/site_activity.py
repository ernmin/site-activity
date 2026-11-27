import pandas as pd
import duckdb
from app.load_json import all_df

def search_raw(PK):
    raw = all_df['raw']
    query = """
    SELECT PK AS SiteID,
    Date_of_Site_Activity AS Date,
    Start_Time AS Start,
    End_Time AS End,
    Title,
    Activity_Description,
    JRLP,
    J152,
    Location,
    Subsystem,
    System_Baseline AS SyBL,
    Test_Cases_Passed AS Passed,
    Test_Cases_Failed AS Failed,
    Test_Cases_Pending AS Pending,
    ISF_Opened,
    ISF_Closed,
    ISF_Failed
    FROM raw
    WHERE 1=1
    AND PK = $PK
    """
    result_df = duckdb.query(query, params={"PK": PK}).to_df().to_dict(orient='records')
    print(result_df)
    return result_df

# def search_site_activity(PK):
#     site_activity = all_df['site_activity']
#     media = all_df['media']
#     query = """
#     SELECT PK AS ID, Date_of_Site_Activity AS Date, Title
#     FROM site_activity
#     JOIN media ON site_activity.PK = media.FK
#     WHERE 1=1
#     AND PK = $PK

#     """
#     result_df = duckdb.query(query, params={"PK": PK}).to_df().to_dict(orient='records')
#     print(result_df)
#     return result_df

# def search_personnel(PK):
#     personnel = all_df['personnel']
#     query = """
#     SELECT team AS Team, name AS Name
#     FROM personnel
#     WHERE 1=1
#     AND FK = $PK
#     ORDER BY Team
#     """
#     result_df = duckdb.query(query, params={"PK": PK}).to_df().to_dict(orient='records')
#     print(result_df)
#     return result_df

# def search_location(PK):
#     location = all_df['location']
#     query = """
#     SELECT location AS Location
#     FROM location
#     WHERE 1=1
#     AND FK = $PK
#     ORDER BY location
#     """
#     result_df = duckdb.query(query, params={"PK": PK}).to_df().to_dict(orient='records')
#     print(result_df)
#     return result_df

