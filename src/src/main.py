Python


from paypal_client import PayPalClient

def main():
    print("Initializing AURA-Secretary (Autonomous AI & Inclusive PayPal Assistant)...")
    try:
        paypal = PayPalClient()
        token = paypal.get_access_token()
        print("Successfully connected to PayPal Sandbox API!")
        print(f"Token acquired: {token[:10]}...")
    except Exception as e:
        print(f"Initialization warning: {e}")

if __name__ == "__main__":
    main()
