import csv
import random
import requests
import datetime
import traceback
import tweepy


def get_random_quote(quotes_file="quotes.csv"):
    try:
        with open(quotes_file) as csv_file:
            quotes = [
                {"author": line[0], "quote": line[1]}
                for line in csv.reader(csv_file, delimiter="|")
            ]
    except Exception as e:
        print(e)
        quotes = [
            {
                "author": "Ciri's sword",
                "quote": "The flash that cuts through darkness, the light that breaks the night.",
            }
        ]
    return random.choice(quotes)


def get_weather_forecast(lat=49.84, lon=24.02):
    try:
        api_key = "6724e513aa3fd78887611d6fea9fb513"
        url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        r = requests.get(url=url)
        data = r.json()
        forecast = {
            "city": data["city"]["name"],
            "country": data["city"]["country"],
            "periods": list(),
        }

        for period in data["list"][0:9]:
            forecast["periods"].append(
                {
                    "timestamp": datetime.datetime.fromtimestamp(period["dt"]),
                    "temp": round(period["main"]["temp"]),
                    "description": period["weather"][0]["description"].title(),
                    "icon": f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}@2x.png',
                }
            )
        return forecast
    except Exception as e:
        print(f"Exception: {e}\ntraceback: {traceback.print_exc()}")


def get_twitter_trends(woeid=23424976):
    try:
        api_key = "QMrTqU2ucXea6p2QcYWXvK1q2"
        api_secret_key = "B9WHvFCFHjh1Stly8yirR9Nuooe2moep651Xd66PUrCLIppvQu"
        auth = tweepy.AppAuthHandler(api_key, api_secret_key)
        return tweepy.API(auth).get_place_trends(woeid)[0]["trends"]
    except Exception as e:
        print(f"Exception: {e}\ntraceback: {traceback.print_exc()}")


def get_wikipedia_article():
    """Retrieve the summary extract for a random Wikipedia article"""
    try:
        data = requests.get(
            url="https://en.wikipedia.org/api/rest_v1/page/random/summary"
        ).json()
        return {
            "title": data["title"],
            "extract": data["extract"],
            "url": data["content_urls"]["desktop"]["page"],
        }
    except Exception as e:
        print(f"Exception: {e}\ntraceback: {traceback.print_exc()}")


if __name__ == "__main__":
    pass
