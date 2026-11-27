from app.config import NGROK_URL
from flask import request, jsonify
import requests
import pandas as pd

def get_data(site_data, route):
    print(site_data)
    print(NGROK_URL)
    try:
        response = requests.get(NGROK_URL + route, params=site_data, timeout=5)
        if response.status_code == 200:
            print("Success!")
            data_response = response.json()
            print(data_response)
            df = pd.DataFrame(response.json())
            print(route)
            if route == 'searchkey':
                html_table = df.T.to_html(header=False)
            else:
                html_table = df.to_html(index=False)
            return jsonify({
                    "status": "success",
                    # "serverPayload": local_file_data.get('result', 'No match found')
                    "result": html_table
                })
        elif response.status_code == 429:
            return jsonify({
                                "status": "success",
                                # "serverPayload": local_file_data.get('result', 'No match found')
                                "result": "You have clicked too many times, try again in a minute"
                            })

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")
        # resolve error
    return