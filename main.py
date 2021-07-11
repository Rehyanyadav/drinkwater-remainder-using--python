import time
from plyer import notification 

if __name__ == '__main__':
    while True:
        notification.notify(
        title="**please Drink Water now!! -made by rehyan",
        message= "The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
        app_icon ="icon.ico",
        timeout=2
    )
        time.sleep(60*60)
        #time stances
    