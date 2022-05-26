"""Module for constants using in the app"""
import os

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.environ.get("TWITTER_API_SECRET_KEY")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

QUOTES_FILE = os.path.join(ROOT_DIR, "quotes.csv")
