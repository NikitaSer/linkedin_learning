import threading
import time
import schedule


class DailyDigestSheduler(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__stop_running = threading.Event()

    def schedule_daily(self, hour, minute, job):
        schedule.clear()
        schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(job)

    def run(self):
        self.__stop_running.clear()
        while not self.__stop_running.is_set():
            schedule.run_pending()
            time.sleep(1)

    def stop(self):
        self.__stop_running.set()
