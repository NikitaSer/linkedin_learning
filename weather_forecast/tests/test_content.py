"""Tests for content module"""
from content import get_random_quote, get_weather_forecast, get_twitter_trends, get_wikipedia_article

def test_get_random_quote():
    """Get random quote"""
    print(get_random_quote())

def test_get_weather_forecast():
    """Check the forecast contains periods"""
    forecast = get_weather_forecast()
    for p in forecast["periods"]:
        print(
            f"date={p['timestamp']}| t={p['temp']} C\N{DEGREE SIGN}| weather='{p['description']}'"
        )


def test_get_twitter_trends():
    """Receive the top 10 trends for Ukraine"""
    trends = get_twitter_trends()
    for t in trends[0:10]:
        print(f"name: {t['name']} | url: {t['url']}")


def test_get_wikipedia_article():
    """Receive a random wiki article"""
    article = get_wikipedia_article()
    for k, v in article.items():
        print(f"{k}: {v}")
