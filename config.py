import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7812163933:AAHJNXrhJkNsWK3SBhBn-gfKdj8ULDdswQ0")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", 22632693))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "44e5cc6bbd184e43c0d6d41a939f342d")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "1615865254").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    # HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    HOST = os.environ.get("HOST", "http://127.0.0.1:8000")  # local server
    CREDIT = os.environ.get("CREDIT", "**ANDYSX BOTS**")  # Making CREDIT an environment variable for flexibility
