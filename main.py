#Price-Drop-Alert-Bot main.py

import time
from datetime import datetime as dt
from notification import desktop_notification
from price import price_record, last_price
from scraper import scrape_price
import schedule

def main():
    current_price = scrape_price()
    
    if current_price < last_price():
        desktop_notification()

    datetime_now = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    price_record(current_price, datetime_now)

schedule.every().day.at('00:00').do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
