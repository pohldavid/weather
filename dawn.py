from astral import LocationInfo
#from astral import now, today
import datetime
from pytz import timezone
#import pytz
from astral.sun import sun
from time import sleep


central = timezone("US/Central")

city = LocationInfo("Pohl Barn", "USA", "US/Central", 29.2829243, -96.8658090) # barn coordinates from google maps

print((
    f"Information for {city.name}/{city.region}\n"
    f"Timezone: {city.timezone}\n"
    f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
))


while True:
    
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)
    sun_today = sun(city.observer, today, tzinfo=city.timezone)
    sun_tomorrow = sun(city.observer, tomorrow, tzinfo=city.timezone)
    localized_now =  central.localize(datetime.datetime.now())
    time_till_dawn = sun_tomorrow["dawn"] - localized_now
    print("time till dawn ", time_till_dawn)
    seconds_till_dawn = time_till_dawn.total_seconds()
    print("seconds till dawn", seconds_till_dawn)
    
    sleep(seconds_till_dawn)
    print("Its Dawn")
    for pause in range(9):
        sleep(60*15)
        print("Its " + str(pause) + " quarter hours since dawn") 
    break
    


    

