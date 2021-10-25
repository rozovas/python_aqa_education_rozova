# https://pythonworld.ru/moduli/modul-time.html
import time
# time.clock(0)

# https://realpython.com/python-time-module/
# The Epoch
print(time.gmtime(0))
# number of seconds that have passed since the epoch:
print(time.time())

# Python Time in Seconds as a String Representing Local Time
print(time.ctime(time.time()))
print(time.ctime())

# Python Time as an Object
from time import struct_time
time_tuple = (2019, 2, 26, 7, 6, 55, 1, 57, 0)
time_obj = struct_time(time_tuple)
print(time_obj)
print(time_obj.tm_yday)
print(time_obj.tm_mon)
print(time_obj.tm_min)

# Converting Python Time in Seconds to an Object
print(time.gmtime(1.99))
print(time.gmtime())

import calendar
print(calendar.timegm(time.gmtime(0)))
print(calendar.timegm(time.gmtime(33)))

# Local Time
print(time.time())
print(time.localtime(1635699154.0739415))
n_t = 1635699154.0739415 - 86400 * 2
print(time.localtime(n_t))

cur_local = time.localtime()
print(cur_local.tm_zone)
print(cur_local.tm_gmtoff / 3600)
print(cur_local.tm_isdst)

# Converting a Local Time Object to Seconds
time_tuple = (2019, 3, 10, 8, 50, 6, 6, 69, 1)
print(time.mktime(time_tuple))

time_struct = time.struct_time(time_tuple)
print(time.mktime(time_struct))
import time
from time import gmtime, mktime
# 1
current_utc = time.gmtime()
print(current_utc)

# 2
current_utc_secs = mktime(current_utc)
print(current_utc_secs)

# 3
print(time.gmtime(current_utc_secs))

# Converting a Python Time Object to a String
print(time.asctime(time.gmtime()))
print(time.asctime(time.localtime()))
print(time.asctime())

import time
print(time.strftime('%d-%m-%Y %I:%M %p', time.localtime()))

from datetime import date
print(date(year=2019, month=3, day=1).isoformat())

from time import asctime
print(asctime())

even after programmatically changing your locale,
asctime() still returns the date and time in the same format as before.
import locale
locale.setlocale(locale.LC_TIME, 'zh_HK')  # Chinese - Hong Kong
print(asctime())

from time import strftime, localtime
print(strftime('%c', localtime()))
import locale
from time import strftime, localtime

locale.setlocale(locale.LC_TIME, 'zh_HK')
print(locale.getlocale(locale.LC_TIME))# Chinese - Hong Kong
print(strftime('%c', localtime()))

# Converting a Python Time String to an Object
from time import strptime
print(strptime('2019-03-01', '%Y-%m-%d'))

# The format parameter is optional and defaults to '%a %b %d %H:%M:%S %Y'.
#  tm_isdst=-1 - strptime() can’t determine by the timestamp
#  whether it represents daylight savings time or not.
print(strptime('Fri Mar 01 23:38:40 2019'))

# Suspending Execution
from time import sleep, strftime
print(strftime('%c'))
sleep(10) # fractionl seconds like o.5 cn be also passed
print(strftime('%c'))

# Measuring Performance
import time
from time import perf_counter
def longrunning_function():
    for i in range(1, 11):
        time.sleep(i / i ** 2)

start = perf_counter()
longrunning_function()
end = perf_counter()
print(f'execution time = {end - start}')

# perf_counter_ns() works the same as perf_counter(), but uses nanoseconds instead of seconds.

# https://realpython.com/python-datetime/
Creating Python datetime Instances
from datetime import date, time, datetime

print(date(year=2020, month=1, day=31))
print(time(hour=13, minute=14, second=31))
print(datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31))

print(date.today())
print(datetime.now())
today = date.today()
now = datetime.now()
current_t = time(now.hour, now.minute, now.second)
print(datetime.combine(today, current_t))

# Using Strings to Create Python datetime Instances
print(date.fromisoformat('2022-01-17'))
date_str = '01-17-2022 16:00:00'
format_str = '%m-%d-%Y %H:%M:%S'
print(datetime.strptime(date_str, format_str))

pyconc countdown

from datetime import datetime

PYCON_DATE = datetime(year=2022, month=5, day=12, hour=8)
countdown = PYCON_DATE - datetime.now()
print(f"Countdown to PyCon US 2021: {countdown}")

# Working With Time Zones
# installed dateutil
from dateutil import tz
from datetime import datetime
now = datetime.now(tz=tz.tzlocal())
print(now)
print(now.tzname())

London_tz = tz.gettz('Europe/London')
now = datetime.now(tz=London_tz)
print(now)
print(now.tzname())
print(datetime.now(tz=tz.UTC))

# Doing Arithmetic With Python datetime
from datetime import datetime, timedelta
now = datetime.now()
print(now)
tomorrow = timedelta(days=+1)
print(now + tomorrow)
yesterday = timedelta(days=-1)
print(now + yesterday)
delta = timedelta(days=+3, hours=-4)
print(now + delta)

from dateutil.relativedelta import relativedelta
tomorrow = relativedelta(days=+1)
print(now + tomorrow)
delta = relativedelta(years=+5, months=+1, days=+3, hours=-4, minutes=-30)
print(now + delta)

# calculating the difference between two datetime instanses
tomorrow = datetime(2021, 10, 31, 9, 37, 46, 380905)
print(relativedelta(now, tomorrow))

# https://docs.python.org/3/library/datetime.html
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

d = timedelta(microseconds=-1)
print((d.days, d.seconds, d.microseconds))

# The comparisons == or != always return a bool,
# no matter the type of the compared object
from datetime import timedelta
delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)
print(delta2 != delta1)
print(delta2 == 5)
print(delta2 > delta1)
# print(delta2 > 5)
# a timedelta object is considered to be true if and only if it isn’t equal to timedelta(0)
print(timedelta(0))

# Components of another_year add up to exactly 365 days (timedelta.total_seconds() example)
from datetime import timedelta
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
print(year == another_year)
print(year.total_seconds())

# Examples of timedelta arithmetic:
from datetime import timedelta
year = timedelta(days=365)
ten_years = 10 * year
print(ten_years)
print(ten_years.days // 365)
nine_years = ten_years - year
print(nine_years)
three_years = nine_years // 3
print(three_years, three_years.days // 365)

from datetime import date
date.fromisoformat('2019-12-04')

d = date(2002, 12, 31)
print(d.replace(day=26))

print(date(2003, 12, 29).isocalendar())
print(date(2004, 1, 4).isocalendar())
print(date(2002, 12, 4).isoformat())

from datetime import date
print(date(2002, 12, 4).ctime())

# Example of counting days to an event:
import time
from datetime import date
today = date.today()
print(today)
print(today == date.fromtimestamp(time.time()))
my_birthday = date(today.year, 6, 24)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
print(my_birthday)

time_to_birthday = abs(my_birthday - today)
time_to_birthday.days

from datetime import datetime
print(datetime.fromisoformat('2011-11-04'))
print(datetime.fromisoformat('2011-11-04T00:05:23'))
print(datetime.fromisoformat('2011-11-04 00:05:23.283'))
print(datetime.fromisoformat('2011-11-04 00:05:23.283+00:00'))
print(datetime.fromisoformat('2011-11-04T00:05:23+04:00'))


from datetime import datetime, timezone
print(datetime(2021, 5, 18, 15, 17, 8, 132263).isoformat())
print(datetime(2021, 5, 18, 15, 17, tzinfo=timezone.utc).isoformat())

# The optional argument sep (default 'T') is a one-character separator,
# placed between the date and time portions of the result.
from datetime import tzinfo, timedelta, datetime
class TZ(tzinfo):
    """A time zone with an arbitrary, constant -06:39 offset."""
    def utcoffset(self, dt):
        return timedelta(hours=-6, minutes=-39)

print(datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' '))
print(datetime(2009, 11, 27, microsecond=100, tzinfo=TZ()).isoformat())


from datetime import datetime, date, time, timezone
# Using datetime.combine()
d = date(2005, 7, 14)
t = time(12, 30)
print(datetime.combine(d, t))
# Using datetime.now()
print(datetime.now())
print(datetime.now(timezone.utc))
# Using datetime.strptime()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)
# Using datetime.timetuple() to get tuple of all attributes
tt = dt.timetuple()
for it in tt:
    print(it)
# Date in ISO format
ic = dt.isocalendar()
for it in ic:
    print(it)
# Formatting a datetime
print(dt.strftime("%A, %d. %B %Y %I:%M%p"))
print('The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time"))

from datetime import time
print(time.fromisoformat('04:23:01'))
print(time.fromisoformat('04:23:01.000384'))
print(time.fromisoformat('04:23:01+04:00'))
