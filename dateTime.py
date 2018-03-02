#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 60
# 43558 Nuno Amaral Soares
# 50021 Bruno Miguel da Silva Machado

from constants import *

def hourToInt(time):
    """
	Change the hours in the received time to an integer.

	Requires: time is str in the "hh:mm" format
	Ensures: integer representing the hour from the time str
    """

    t = time.split(":")
    return int(t[0])




def minutesToInt(time):
    """
	Change the minutes in the received time to an integer.

	Requires: time is str in the "hh:mm" format
	Ensures: integer representing the minutes from the time str
	"""

    t = time.split(":")
    return int(t[1])



def intToTime(hour, minutes):
    """
	Receives two integers, hour and minutes, representing a specific time and converts it into str format.

	Requires: hour is an integer; minutes is an integer
	Ensures: returns a time in str format ("hh:mm")
	"""

    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + ":" + m


def dayToInt(date):
    """
	Change the day in the received date to an integer.

	Requires: date is str in the "DD:MM:YYYY" format
	Ensures: integer representing the day from the date str
    """

    d = date.split(":")
    return int(d[0])


def monthToInt(date):
    """
	Change the month in the received date to an integer.

	Requires: date is str in the "DD:MM:YYYY" format
	Ensures: integer representing the month from the date str
    """

    d = date.split(":")
    return int(d[1])


def yearToInt(date):
    """
	Change the year in the received date to an integer.

	Requires: date is str in the "DD:MM:YYYY" format
	Ensures: integer representing the year from the date str
    """

    d = date.split(":")
    return int(d[2])
    

def intToDate(day,month,year):
    """
    Change the year in the received date to an integer.

	Requires: day, month and year in the int format
	Ensures: respective date (according to the day, month
	and year received) as str in the "DD:MM:YYYY" format
    """

    d = str(day)
    m = str(month)
    y = str(year)

    if day < 10:
        d = "0" + d

    if month < 10:
        m = "0" + m

    date = d + ":" + m + ":" + y
    return date



def datesComparison(date1,date2):
    """
	Returns the earliest date (whichever happens first)
	between two received dates.

	Requires: two dates in the "DD:MM:YYYY" str format
	Ensures: one date in the "DD:MM:YYYY" str format
	(earliest of the two recieved)
	"""
	
    day1 = dayToInt(date1)
    day2 = dayToInt(date2)
	
    month1 = monthToInt(date1)
    month2 = monthToInt(date2)
	
    year1 = yearToInt(date1)
    year2 = yearToInt(date2)
	
    if year1 < year2:
        return date1
    elif month1 < month2:
        return date1
    elif day1 < day2:
        return date1
    else:
        return date2



def dateChange(date):
    """
    Receives a date in the "DD:MM:YYYY" str format and
    advances it one day (with respect to the different
    lengths of a month in a year's calendar).

	Requires: one date in the "DD:MM:YYYY" str format
	Ensures: date of following day in the "DD:MM:YYYY"
	str format
    """

    day = dayToInt(date)
    month = monthToInt(date)
    year = yearToInt(date)
    totaldays = 0
    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #number of days for each month in a year

    for m in range(0, month):
        if m < (month - 1):
            totaldays = totaldays + daysInMonths[m]
        elif m == (month - 1):
            totaldays = totaldays + day

    if totaldays == 365:
        newday = 1
        newmonth = 1
        newyear = year + 1
    elif totaldays < 365:
        if day == daysInMonths[month - 1]:
            newday = 1
            newmonth = month + 1
            newyear = year
        else:
            newday = day + 1
            newmonth = month
            newyear = year

    date = intToDate(newday, newmonth, newyear)
    return date


def updatedate(date,hour,periodAfter):
    """
    Receives a date in the "DD:MM:YYYY" str format,
    one hour in the "HH:MM" str format and a periodAfter int
    which represent how many minutes have passed since last update.

	Requires: one date in the "DD:MM:YYYY" str format, one hour
	in the "HH:MM" str format and an int (periodAfter)
	Ensures: a list (dateTimeInfo) whose elements are the
	updated date and hour
    """

    hour1 = hourToInt(hour)
    minutes1 = minutesToInt(hour)

    hours = (minutes1 + periodAfter) / 60
    minutes = (minutes1 + periodAfter) % 60

    sumhour = hour1 + hours
    newhour = (sumhour) % 24
    newminutes = minutes

    hour = intToTime(newhour,newminutes) #new hour

    #in case of day change, day advances
    if sumhour >= 24:
        daysPassed = sumhour/24 #number of days passed
        for i in range(0,daysPassed):
            date = dateChange(date)

    dateTimeInfo = []
    dateTimeInfo.append(date)
    dateTimeInfo.append(hour)

    return dateTimeInfo