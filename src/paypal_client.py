Python


import os
import requests
from dotenv import load_dotenv

load_dotenv()

class PayPalClient:
    def __init__(self):
        self.client_id = os.getenv("PAYPAL_CLIENT_ID")
        self.client_secret = os.getenv("PAYPAL_CLIENT_SECRET")
        self.base_url = "https://api-m.sandbox.paypal.com"  # Sandbox environment

    def get_access_token(self):
        url = f"{self.base_url}/v1/oauth2/token"
        response = requests.post(
            url,
            auth=(self.client_id, self.client_secret),
            headers={"Accept": "application/json", "Accept-Language": "en_US"},
            data={"grant_type": "client_credentials"}
        )
        if response.status_code == 200:
            return response.json().get("access_token")
        raise Exception(f"Failed to get PayPal access token: {response.text}")
