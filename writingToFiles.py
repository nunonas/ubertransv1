#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 60
# 43558 Nuno Amaral Soares
# 50021 Bruno Miguel da Silva Machado

from dateTime import *
from constants import *

def createHeader (day, time, type):
	"""
	Creates a header for an output file, according to
    the project's specification
    Requires: day is a string in the DD:MM:YY format with the
    update date
    time is a string in the HH:MM format with the update hour
    type refers if the header is for a Schedule or Translators file
    Ensures: a string equal to the pretended header, according
    to the project's specification and respective to the given
    day and time
	"""

	header = "Company:\nReBaBel\nDay:\n"
	header += day #adds the day
	header += "\nTime:\n"
	header += time #adds the time
	if type == "schedule":
		header += "\nSchedule:"
	elif type == "translators":
		header += "\nTranslators:"

	return header



def writeScheduleFile(tasksAssigned, file_name, header):
	"""Writes a collection of services into a file.

    Requires:
    tasksAssigned is a list with the structure as in the output of
    scheduling.scheduleTasks representing the translation tasks assigned;
    file_name is a str with the name of a .txt file;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability).
    Ensures:
    writing of file named file_name representing the list of
    translation tasks in tasksAssigned prefixed by header and 
    organized as in the examples provided  in the general specification 
    (omitted here for the sake of readability);
    the listing in this file keeps the ordering top to bottom of 
    the translations tasks as ordered head to tail in tasksAssigned.
    """

	outfile = open(file_name, 'w')
	headerlist = header.split('\n')

	for line in headerlist:
		outfile.writelines(line + '\n')

	for task in tasksAssigned:
		for i in range(0,len(task)):
			task[i] = str(task[i])

	for task in tasksAssigned:
		string = ', '.join(task) + '\n'
		outfile.writelines(string)

	outfile.close()


def writeTranslatorsFile(translatorsUpdated, file_name, header):
	"""
	Writes the translators information from the translators dictionary
	into a file.

    Requires:
    translatorsUpdated is the updated translator dictionary.
    file_name is a str with the name of a .txt file;
    header is a string with a header, as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    writing of file named file_name representing the updated information
    about each translator from the updated translators dictionary (translatorsUpdated)
	prefixed by header and organized as in the examples provided
	in the general specification (omitted here for the sake of readability);
	"""

	outfile = open(file_name, 'w')
	headerlist = header.split('\n')

	for line in headerlist:
		outfile.writelines(line + '\n')

	names = sorted(translatorsUpdated)

	for name in translatorsUpdated:
		for i in range(0, len(translatorsUpdated[name])):
			translatorsUpdated[name][i] = str(translatorsUpdated[name][i])

	for name in names:
		string = name + ', ' + ', '.join(translatorsUpdated[name]) + '\n'
		outfile.writelines(string)

	outfile.close()

