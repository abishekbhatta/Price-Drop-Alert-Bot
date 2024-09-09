#this moudle contains desktop_notification function which pops up notifcation to desktop on being called

from plyer import notification
from scraper import scrape_price

def desktop_notification():
        notification.notify(
                app_name="Bot",
                app_icon= "media/icons8-alert-100.ico",
                message= f"MacBook Pro M3 Pro chip price has been dropped down. The current price is ${scrape_price()}.",
                title="Price Drop Alert",
                timeout = 5
        )

