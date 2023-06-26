from plyer import notification
import time
import os

while True:
    time.sleep(60*60)
    notification.notify(
        title="Please Drink Water Now",
        message="It's been long time you working....Take break and have a drink of water...Be healthy!",
        app_icon=r"C:\water.ico",
        timeout=10
    )