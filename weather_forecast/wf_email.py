import content
import datetime


class DailyDigestEmail:
    def __init__(self):
        self.content = {
            "quote": {"include": True, "content": content.get_random_quote()},
            "weather": {"include": True, "content": content.get_weather_forecast()},
            "twitter": {"include": True, "content": content.get_twitter_trends()},
            "wikipedia": {"include": True, "content": content.get_wikipedia_article()},
        }

    def send_email(self):
        pass

    def format_message(self):
        text = f'*~*~*~* Daily Digest - {datetime.date.today().strftime("%d %b %Y")} *~*~*~*\n\n'

        if self.content["quote"]["include"] and self.content["quote"]["content"]:
            text += '*~*~*~* Quote of the day *~*~*~*\n\n'
            text += f'{self.content["quote"]["content"]["quote"]}: {self.content["quote"]["content"]["author"]}'

        if self.content["weather"]["include"] and self.content["weather"]["content"]:
            text += '*~*~*~* Weather forecast *~*~*~*\n\n'
            for p in content["weather"]["content"]["periods"]:
                text += f"date={p['timestamp']}| t={p['temp']} C\N{DEGREE SIGN}| weather='{p['description']}'"
            text += "\n"

        if self.content["twitter"]["include"] and self.content["twitter"]["content"]:
            text += '*~*~*~* Quote of the day *~*~*~*\n\n'
            text += f'{self.content["quote"]["content"]["quote"]}: {self.content["quote"]["content"]["author"]}'

        if self.content["wikipedia"]["include"] and self.content["wikipedia"]["content"]:
            text += '*~*~*~* Quote of the day *~*~*~*\n\n'
            text += f'{self.content["quote"]["content"]["quote"]}: {self.content["quote"]["content"]["author"]}'