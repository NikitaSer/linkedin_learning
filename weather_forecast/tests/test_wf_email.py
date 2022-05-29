from weather_forecast.wf_email import DailyDigestEmail


def test_create_email_template_html():
    with open("email_template.html", mode="w", encoding="utf-8") as file:
        file.write(DailyDigestEmail().format_message().get("html"))
