import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
REALIZA_ASSISTANCE=os.getenv("REALIZA_ASSISTANCE")
EUROP_ASSISTANCE=os.getenv("EUROP_ASSISTANCE")