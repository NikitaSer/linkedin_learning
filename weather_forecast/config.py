"""Module for constants using in the app"""
import os

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.environ.get("TWITTER_API_SECRET_KEY")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
EMAIL_USER = os.environ.get("EMAIL_USER")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
QUOTES_FILE = os.path.join(ROOT_DIR, "quotes.csv")
WF_CONFIG = os.path.join(ROOT_DIR, "wf_config.json")
