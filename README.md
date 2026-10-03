App for tracking site progress
1. Make sure that you have a free ngrok domain
2. When running the ngrok domain from the terminal it should be in the following format:
ngrok http --url=(insert url here) (insert same port number as flask app)
3. When using a new account and developer URL, remember to configure the Authtoken so that the dev URL can be used with the correct ngrok account (https://dashboard.ngrok.com/get-started/your-authtoken)

4. Google Sheet can be connected with ngrok domain and server.py
Next step: Work on the data model for the function transform and process row