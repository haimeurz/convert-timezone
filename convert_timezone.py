from datetime import datetime
from dateutil import tz

# Fonction qui convert une utc date en nimporte quelle autre timezone au canada

def  convert_to_local(utc_date,timezone):
    # 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific',
    # 'Canada/Saskatchewan', 'Canada/Yukon'-----> Timezones accepted
    if "Canada/" in timezone:
        utc = tz.gettz("UTC")
        timezone_to_convert_to = tz.gettz(timezone)
        utc_date = datetime.strptime(utc_date, '%Y-%m-%d %H:%M:%S')
        utc_date = utc_date.replace(tzinfo=utc)
        print(f'time in UTC:{utc_date}')
        # Convert to time zone
        time_converted = utc_date.astimezone(timezone_to_convert_to)
        #new_time = datetime.now(timezone(timezone_to_convert_to))
        print(f'time in {timezone}: {time_converted} ')
        return time_converted

    else:
        print("Timezone is not in Canada")
convert_to_local("2022-01-26 15:00:18",'Canada/Eastern')
#DURING Daylight saving time
convert_to_local("2021-06-26 15:00:18",'Canada/Eastern')