import datetime
import time
##Time Basics
#https://docs.python.org/2/library/datetime.html#datetime.timedelta
#https://pymotw.com/2/datetime/#formatting-and-parsing


#There are two kinds of date and time objects: naive and aware
#An aware object has sufficient knowledge of applicable algorithmic and political time adjustments, such as time zone and daylight saving time information,
# to locate itself relative to other aware objects. An aware object is used to represent a specific moment in time that is not open to interpretation [1].

#For applications requiring aware objects, datetime and time objects have an optional time zone information attribute, tzinfo
##tzinfo objects capture information about the offset from UTC time, the time zone name, and whether Daylight Saving Time is in effect.


#Objects of the date type are always naive.

#An object of type time or datetime may be naive or aware. A datetime object d is aware if d.tzinfo is not None and d.tzinfo.utcoffset(d) does not return None.
# If d.tzinfo is None, or if d.tzinfo is not None but d.tzinfo.utcoffset(d) returns None, d is naive. A time object t is aware if t.tzinfo is not None and
# t.tzinfo.utcoffset(None) does not return None. Otherwise, t is naive.

#datetime.time
t = datetime.time(1, 2, 3)

print t
print 'hour  :', t.hour
print 'minute:', t.minute
print 'second:', t.second
print 'microsecond:', t.microsecond
print 'tzinfo:', t.tzinfo


print 'Earliest  :', datetime.time.min
print 'Latest    :', datetime.time.max
print 'Resolution:', datetime.time.resolution

# for m in [ 1, 0, 0.1, 0.6 ]:
#     try:
#         print '%02.1f :' % m, datetime.time(0, 0, 0, microsecond=m)
#     except TypeError, err:
#         print 'ERROR:', err


#datetime.date
today=datetime.date.today() # Naive date object
# today=datetime.datetime.today # Aware date object - tzinfo

print today
print 'ctime:', today.ctime() # string rep of time
print 'tuple:', today.timetuple()
print 'ordinal:', today.toordinal() # Gregorian Rep of time
print 'fromordinal:', datetime.datetime.fromordinal(today.toordinal())
print 'Year:', today.year
print 'Mon :', today.month
print 'Day :', today.day


#datetime
todaydatetime=datetime.datetime.today()

print 'ctime',todaydatetime.ctime()
print 'utctime',todaydatetime.utctimetuple()
print 'today :',todaydatetime
print 'Year' ,todaydatetime.year
print 'month', todaydatetime.month
print 'day',todaydatetime.day
print 'weekday num ',todaydatetime.weekday()
print 'Timezonfo', todaydatetime.tzinfo


#timestamp & fromordinal

o = 733114
print 'o:', o
print 'fromordinal(o):', datetime.datetime.fromordinal(o)
print 'fromordinal(o):', datetime.date.fromordinal(o)
t = time.time()
print 't:', t
print 'fromtimestamp(t):', datetime.datetime.fromtimestamp(t)
print 'fromtimestamp(t):', datetime.date.fromtimestamp(t)


#date, datetime, datetime.datetime, time -  min & max


print 'Earliest  :', datetime.date.min
print 'Earliest  :', datetime.datetime.min
#print 'Earliest  :', time.time().min                     - error
print 'Earliest  :', datetime.time.min


print 'Latest    :', datetime.date.max
print 'Latest    :', datetime.datetime.max
#print 'Latest  :', time.time().max                       - error
print 'Latest  :', datetime.time.max


print 'Resolution:', datetime.date.resolution
print 'Resolution:', datetime.datetime.resolution
#print 'Resolution  :', time.time().resolution               -  error
print 'Resolution  :', datetime.time.resolution



#replace for creating new date

date1=datetime.date(2008, 3, 12)
date2=date1.replace(year=datetime.datetime.today().year)

print date1
print date2

#timedelta

print "microseconds:", datetime.timedelta(microseconds=1)
print "milliseconds:", datetime.timedelta(milliseconds=1)
print "seconds     :", datetime.timedelta(seconds=1)
print "minutes     :", datetime.timedelta(minutes=1)
print "hours       :", datetime.timedelta(hours=1)
print "days        :", datetime.timedelta(days=1)
print "weeks       :", datetime.timedelta(weeks=1)



#Arithmatic ops on DATES

today = datetime.date.today()
print 'Today    :', today

one_day = datetime.timedelta(days=1)
print 'One day  :', one_day

yesterday = today - one_day
print 'Yesterday:', yesterday

tomorrow = today + one_day
print 'Tomorrow :', tomorrow

print 'tomorrow - yesterday:', tomorrow - yesterday
print 'yesterday - tomorrow:', yesterday - tomorrow



#comparing date


print 'Times:'
t1 = datetime.time(12, 55, 0)
print 't1:', t1
t2 = datetime.time(13, 5, 0)
print 't2:', t2
print 't1 < t2:', t1 < t2

print 'Dates:'
d1 = datetime.date.today()
print 'd1:', d1
d2 = datetime.date.today() + datetime.timedelta(days=1)
print 'd2:', d2
print 'd1 > d2:', d1 > d2