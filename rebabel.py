#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 60
# 43558 Nuno Amaral Soares
# 50021 Bruno Miguel da Silva Machado

from sys import argv
from constants import *
from dateTime import *
from readingFromFiles import *
from scheduling import *
from writingToFiles import *

def checkTimeAndScope(translatorsFileName, tasksFileName):
    """
    Checks if the day, time and scope are the same in translatorsFileName and
    tasksFileName and if so, returns a list with the date and time information.

    Requires: all the filenames are the same than the ones passed as an argument
    in the function assign. The scope in the file must be consistent with each
    file name. The day and hour must be the same in each file.
    Ensures: IOError exception if any of the required rules are not respected. If
    exception is not raised, then returns a list (datetimeinfo) with the date and
    time information (date in "DD:MM:YYYY" str format and hour in "HH:MM" str format).
    """

    translators = open(translatorsFileName, 'r')
    tasks = open(tasksFileName, 'r')

    day = []
    time = []
    scope = []

    #gets the day, time and scope from the files
    for i in (translators, tasks):
        i.readline()
        i.readline()
        i.readline()
        day.append(i.readline())
        i.readline()
        time.append(i.readline())
        scope.append(i.readline())

    #raises IOError if day or time are not consistent between the two files
    if not all([d == day[0] for d in day]) or not all([t == time[0] for t in time]):
        raise IOError

    datetimeinfo = []
    datetimeinfo.append(day[0])
    datetimeinfo.append(time[0])

    for i in range(0, len(scope)):
        scope[i] = scope[i].rstrip(":\n")

    for i in range(0, len(scope)):
        scope[i] = scope[i].lower()

    #raises IOError if the scope in the files are not consistent with the file names
    if scope[0] != translatorsFileName[0:11]:
        raise IOError

    if scope[1] != tasksFileName[0:5]:
        raise IOError

    return datetimeinfo


def assign(translatorsFileName, tasksFileName):
    """Obtains the assignment of translation tasks to translators.

    Requires:
    translatorsFileName is a str with the name of a .txt file containing a list
    of translators, organized as in the examples provided;
    tasksFileName is a str with the name of a .txt file containing a list
    of translation tasks requested in the 10 minute period right after the update
    time of translatorsFileName, organized as in the examples provided;
    both these input files concern the same company, date and time.
    Ensures:
    writing of two .txt files containing the list of translation tasks assigned
    to translators and the updated list of translators, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, scheduleXXhYY.txt and
    translatorsXXhYY.txt, where XXhYY represents the time and date 10 minutes
    after the time and date indicated in the files translatorsFileName and 
    tasksFileName, and are written in the same directory of the latter.
    """
    
    try:

        # checks if the day/time and the scope are the same in all files
        datetime = checkTimeAndScope(translatorsFileName, tasksFileName)
        if len(datetime) == 2:
            day = datetime[0].rstrip("\n")
            time = datetime[1].rstrip("\n")

            hour = str(hourToInt(time))
            minutes = str(minutesToInt(time))

            # checks if the hour in each file are the same as in the file name. If not, raises IOError
            if hour != translatorsFileName[11:13]:
                raise IOError
            if hour != tasksFileName[5:7]:
                raise IOError

            # checks if the minutes in each file are the same as in the file name. If not, raises IOError
            if minutes != translatorsFileName[14:16]:
                raise IOError
            if minutes != tasksFileName[8:10]:
                raise IOError

        translators = readTranslatorsFile(translatorsFileName) #translator dictionary with the information from the translators file
        tasks = readTasksFile(tasksFileName) #tasks list with the information from the tasks file

        updateschedule = scheduleTasks(translators,tasks,day,time,periodafter) #assigns the tasks to translators periodafter minutes (=10) after the initial update time, the assigned tasks' information put into a schedule list and updates the translators dictionary

        newdatetime = updatedate(day, time, periodafter)
        newday = newdatetime[0]
        newtime = newdatetime[1]
        newtime2 = newtime.split(":")
        newhour = newtime2[0]
        newminutes = newtime2[1]

        writeScheduleFile(updateschedule,'schedule' + newhour + 'h' + newminutes + '.txt', createHeader(newday,newtime,'schedule')) #writes a schedule file with the assigned tasks' information from updateschedule
        writeTranslatorsFile(translators,'translators' + newhour + 'h' + newminutes + '.txt', createHeader(newday,newtime,'translators')) #writes an updated translators file with the update information from the translators dictionary

    except IOError:
        print "Input file error: scope or time inconsistency between name and header in one of the files"



assign(argv[1], argv[2])

