from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_limiter.errors import RateLimitExceeded
from user_table import transform_and_process_row
# from return_entries import return_entries, return_all_entries, refresh_data_cache
import pandas as pd

app = Flask(__name__)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["20000 per day", "5000 per hour"],
    storage_uri="memory://",
)

@app.route('/webhook', methods=['POST'])
def handle_sheets_update():
    response_headers = {"ngrok-skip-browser-warning": "true"}
    
    payload = request.json
    row_index = payload.get('approvedRowIndex')
    headers = payload.get('headers', [])
    row_data = payload.get('rowData', [])
    cell_value = payload.get('cellValue')
    
    if not row_data:
        return jsonify({"status": "no data received"}), 400, response_headers

    df = pd.DataFrame([row_data], columns=headers)
    
    print(f"\n--- [ALERT] Row {row_index} Has Been Received! ---")
    print(df)
    print("----------------------------------------------------\n")
    
    transform_and_process_row(row_data, headers, row_index, cell_value)
    # refresh_data_cache()

    return jsonify({"status": "success", "processed_row": row_index}), 200, response_headers

# @app.route('/entries', methods=['GET'])
# @limiter.limit("1 per second")
# def get_entries():
#     response_headers = {"ngrok-skip-browser-warning": "true"}
#     received_var = request.args.get('requestedUser')
#     print(f"Heroku sent me this variable: {received_var}")

#     if received_var == 'ALLzxc':
#         json_rows = return_all_entries()
#         print(json_rows)
#         return json_rows
#     else:
#         json_filtered_rows = return_entries(received_var)
#         print(type(json_filtered_rows))
#         print(json_filtered_rows)
#         return json_filtered_rows


if __name__ == '__main__':
    app.run(port=5050, debug=True)