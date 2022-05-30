from weather_forecast.wf_scheduler import DailyDigestSheduler
from weather_forecast.wf_email import DailyDigestEmail
import time


def test_run_scheduler():
    email = DailyDigestEmail()

    scheduler = DailyDigestSheduler()
    scheduler.start()

    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min + 1
    print(f"Sсhedule test for {hour:02d}:{minute:02d}")
    scheduler.schedule_daily(hour, minute, email.send_email)
    time.sleep(60)
    scheduler.stop()


if __name__ == "__main__":
    test_run_scheduler()
