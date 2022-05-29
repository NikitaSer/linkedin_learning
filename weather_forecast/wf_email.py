import weather_forecast.content as content
import datetime
import weather_forecast.config as config
import smtplib
import ssl
from email.message import EmailMessage


class DailyDigestEmail:
    def __init__(self):
        self.content = {
            "quote": {"include": True, "content": content.get_random_quote()},
            "weather": {"include": True, "content": content.get_weather_forecast()},
            "twitter": {"include": True, "content": content.get_twitter_trends()},
            "wikipedia": {"include": True, "content": content.get_wikipedia_article()},
        }

        self.recipients_list = [config.EMAIL_USER]
        self.sender_credentials = {
            "email": config.EMAIL_USER,
            "password": config.EMAIL_PASS,
        }

    def send_email(self):
        msg = EmailMessage()
        msg["Subject"] = f'Daily Digest - {datetime.date.today().strftime("%d %b %Y")}'
        msg["From"] = self.sender_credentials["email"]
        msg["To"] = self.recipients_list

        msg_body = self.format_message()
        msg.set_content(msg_body["text"])
        msg.add_alternative(msg_body["html"], subtype="html")

        contex = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contex) as server:
            server.login(
                self.sender_credentials["email"], self.sender_credentials["password"]
            )
            server.send_message(msg)

    def format_message(self):
        text = f'*~*~*~* Daily Digest - {datetime.date.today().strftime("%d %b %Y")} *~*~*~*\n\n'

        if self.content["quote"]["include"] and self.content["quote"]["content"]:
            text += "*~*~*~* Quote of the day *~*~*~*\n\n"
            text += f'{self.content["quote"]["content"]["quote"]}: {self.content["quote"]["content"]["author"]}'

        if self.content["weather"]["include"] and self.content["weather"]["content"]:
            text += "*~*~*~* Weather forecast *~*~*~*\n\n"
            for forecast in self.content["weather"]["content"]["periods"]:
                text += f"date={forecast['timestamp']}| t={forecast['temp']}\u00b0С| weather='{forecast['description']}'"
            text += "\n"

        if self.content["twitter"]["include"] and self.content["twitter"]["content"]:
            text += "*~*~*~* Top ten twitter trends *~*~*~*\n\n"
            for trend in self.content["twitter"]["content"][0:10]:
                text += f'{trend["name"]}\n'
            text += "\n"

        if (
            self.content["wikipedia"]["include"]
            and self.content["wikipedia"]["content"]
        ):
            text += "*~*~*~* Random wiki article *~*~*~*\n\n"
            text += f'{self.content["wikipedia"]["content"]["title"]}\n{self.content["wikipedia"]["content"]["extract"]}'

        html = f"""<html>
    <body>
        <h1>Daily Digest - {datetime.date.today().strftime("%d %b %Y")}</h1>
        """
        if self.content["quote"]["include"] and self.content["quote"]["content"]:
            html += f"""
            <h2>Quote of the day</h2>
            <i>"{self.content["quote"]["content"]["quote"]}"</i> {self.content["quote"]["content"]["author"]}
            """

        if self.content["weather"]["include"] and self.content["weather"]["content"]:
            html += f"""
            <h2>Forecast for {self.content["weather"]["content"]["city"]}</h2>
            <table>
            """
            for forecast in self.content["weather"]["content"]["periods"][0:3]:
                html += f"""
                <tr>
                    <td>
                        {forecast['timestamp'].strftime("%d %b %Y")}
                    </td>
                    <td>
                        <img src="{forecast['icon']}">
                    </td>
                    <td>
                        {forecast['temp']}\u00b0С | '{forecast['description']}
                    </td>
                </tr>
                """
            html += """
            </table>
            """

        if self.content["twitter"]["include"] and self.content["twitter"]["content"]:
            html += f"""
            <h2>Top ten twitter trends</h2>
            """
            for trend in self.content["twitter"]["content"][0:10]:
                html += f"""
                <b><a href={trend["url"]}> {trend["name"]}</a></b><p>
            """

        if (
            self.content["wikipedia"]["include"]
            and self.content["wikipedia"]["content"]
        ):
            html += f"""
            <h2>Random wiki article</h2>
                <h3><a href="{self.content["wikipedia"]["content"]["url"]}">{self.content["wikipedia"]["content"]["title"]}</a><h3>
                    <table width="800">
                        <tr>
                            <td>{self.content["wikipedia"]["content"]["extract"]}'</td>
                        </tr>
                    </table>
            """
            html += f"""
    </body>
    </html>
    """

        return {"text": text, "html": html}


if __name__ == "__main__":
    d = DailyDigestEmail()
    d.send_email()
