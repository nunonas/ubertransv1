#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 60
# 43558 Nuno Amaral Soares
# 50021 Bruno Miguel da Silva Machado

from copy import deepcopy
from dateTime import *
from constants import *

def critQuality(translators, subtask, possibleTranslators):
	"""
	Returns a list with the names of the possible translators
	for specific task if the criterion used in the task is 'quality'.

	Requires: dictionary 'translators' with information for each of them,
	list 'subtask' with the information about a specific task, list with
	the names of the current possible translators
	Ensures: updated list of the possible translators
	"""

	uptranslators = deepcopy(translators)

	possible = tuple(possibleTranslators)
	for name in possible:
		if uptranslators[name][INDEXTranslatorQuality] != "3*":
			possibleTranslators.remove(name)

	# if more than one possible translator, the tiebreaker is the one who is available sooner
	if (len(possibleTranslators) > 1):
		possible = tuple(possibleTranslators)  # tuple with the elements from possibleTranslators
		i = 0
		names = []
		for name in possible:
			if i == 0:
				names.append(name)
				date1 = uptranslators[name][INDEXTranslatorDelivery]
			elif i != 0:
				date2 = uptranslators[name][INDEXTranslatorDelivery]
				comp = datesComparison(date1, date2)
				if comp == date2:
					if date1 != date2:
						for n in names:
							possibleTranslators.remove(n)
							names = []
							names.append(name)
							date1 = date2
					elif date1 == date2:
						names.append(name)
				elif comp != date2:
					possibleTranslators.remove(name)
			i = i + 1

	# if more than one possible translator, the tiebreaker is the one who is cheaper
	if (len(possibleTranslators) > 1):
		possible = tuple(possibleTranslators)  # tuple with the elements from possibleTranslators
		i = 0
		names = []
		for name in possible:
			if i == 0:
				names.append(name)
				price1 = float(uptranslators[name][INDEXTranslatorPrice])
			elif i != 0:
				price2 = float(uptranslators[name][INDEXTranslatorPrice])
				if price2 == price1:
					names.append(name)
				elif price2 < price1:
					for n in names:
						possibleTranslators.remove(n)
						names = []
						names.append(name)
						price1 = price2
				elif price2 > price1:
					possibleTranslators.remove(name)
			i = i + 1

	return possibleTranslators




def critPrice(translators, subtask, possibleTranslators):
	"""
	Returns a list with the names of the possible translators
	for specific task if the criterion used in the task is 'price'.

	Requires: dictionary 'translators' with information for each of them,
	list 'subtask' with the information about a specific task, list with
	the names of the current possible translators
	Ensures: updated list of the possible translators
	"""

	uptranslators = deepcopy(translators)

	if (len(possibleTranslators) > 1):
		possible = tuple(possibleTranslators)  # tuple with the elements from possibleTranslators
		i = 0
		names = []
		for name in possible:
			if i == 0:
				names.append(name)
				price1 = float(uptranslators[name][INDEXTranslatorPrice])
			elif i != 0:
				price2 = float(uptranslators[name][INDEXTranslatorPrice])
				if price2 == price1:
					names.append(name)
				elif price2 < price1:
					for n in names:
						possibleTranslators.remove(n)
						names = []
						names.append(name)
						price1 = price2
				elif price2 > price1:
					possibleTranslators.remove(name)
			i = i + 1

	#if more than one possible translator, the tiebreaker is the one with lowest rating
	if (len(possibleTranslators) > 1):
		possible = tuple(possibleTranslators)
		i = 0
		names = []
		for name in possible:
			if i == 0:
				names.append(name)
				rating1 = int(uptranslators[name][INDEXTranslatorQuality][0])
			elif i != 0:
				rating2 = int(uptranslators[name][INDEXTranslatorQuality][0])
				if rating2 == rating1:
					names.append(name)
				elif rating2 < rating1:
					for n in names:
						possibleTranslators.remove(n)
						names = []
						names.append(name)
						rating1 = rating2
				elif rating2 > rating1:
					possibleTranslators.remove(name)
			i = i + 1

	# if more than one possible translator, the tiebreaker is the one who is available sooner
	if (len(possibleTranslators) > 1):
		possible = tuple(possibleTranslators)  # tuple with the elements from possibleTranslators
		i = 0
		names = []
		for name in possible:
			if i == 0:
				names.append(name)
				date1 = uptranslators[name][INDEXTranslatorDelivery]
			elif i != 0:
				date2 = uptranslators[name][INDEXTranslatorDelivery]
				comp = datesComparison(date1, date2)
				if comp == date2:
					if date1 != date2:
						for n in names:
							possibleTranslators.remove(n)
							names = []
							names.append(name)
							date1 = date2
					elif date1 == date2:
						names.append(name)
				elif comp != date2:
					possibleTranslators.remove(name)
			i = i + 1

	return possibleTranslators



def critSpeed(translators, subtask, possibleTranslators):
	"""
	Returns a list with the names of the possible translators
	for specific task if the criterion used in the task is 'speed'.

	Requires: dictionary 'translators' with information for each of them,
	list 'subtask' with the information about a specific task, list with
	the names of the current possible translators
	Ensures: updated list of the possible translators
	"""

	uptranslators = deepcopy(translators)

	task = deepcopy(subtask)
	taskrating = int(task[INDEXTaskQuality][0])

	if (len(possibleTranslators) > 1):
		possible = tuple(possibleTranslators)  # tuple with the elements from possibleTranslators
		i = 0
		names = []
		for name in possible:
			if i == 0:
				names.append(name)
				date1 = uptranslators[name][INDEXTranslatorDelivery]
			elif i != 0:
				date2 = uptranslators[name][INDEXTranslatorDelivery]
				comp = datesComparison(date1, date2)
				if comp == date2:
					if date1 != date2:
						for n in names:
							possibleTranslators.remove(n)
							names = []
							names.append(name)
							date1 = date2
					elif date1 == date2:
						names.append(name)
				elif comp != date2:
					possibleTranslators.remove(name)
			i = i + 1

	# if more than one possible translator, the tiebreaker is the one with lowest possible rating
	if (len(possibleTranslators) > 1):
		possible = tuple(possibleTranslators)
		for name in possible:
			if int(uptranslators[name][INDEXTranslatorQuality][0]) < taskrating:
				possibleTranslators.remove(name)

		possible = tuple(possibleTranslators)
		i = 0
		names = []
		for name in possible:
			if i == 0:
				names.append(name)
				rating1 = int(uptranslators[name][INDEXTranslatorQuality][0])
			elif i != 0:
				rating2 = int(uptranslators[name][INDEXTranslatorQuality][0])
				if rating2 == rating1:
					names.append(name)
				elif rating2 < rating1:
					for n in names:
						possibleTranslators.remove(n)
						names = []
						names.append(name)
						rating1 = rating2
				elif rating2 > rating1:
					possibleTranslators.remove(name)
			i = i + 1

	# if more than one possible translator, the tiebreaker is the one who is cheaper
	if (len(possibleTranslators) > 1):
		possible = tuple(possibleTranslators)  # tuple with the elements from possibleTranslators
		i = 0
		names = []
		for name in possible:
			if i == 0:
				names.append(name)
				price1 = float(uptranslators[name][INDEXTranslatorPrice])
			elif i != 0:
				price2 = float(uptranslators[name][INDEXTranslatorPrice])
				if price2 == price1:
					names.append(name)
				elif price2 < price1:
					for n in names:
						possibleTranslators.remove(n)
						names = []
						names.append(name)
						price1 = price2
				elif price2 > price1:
					possibleTranslators.remove(name)
			i = i + 1

	return possibleTranslators




def scheduleTasks(translators, tasks, date, hour, periodAfter):

	"""Assigns translation tasks to translators.
	
	Requires:
	translators is a dict with a structure as in the output of
	readingFromFiles.readTranslatorsFile concerning the update time; 
	tasks is a list with the structure as in the output of 
	readingFromFiles.readTasksFile concerning the period of
	periodAfter minutes immediately after the update time of translators;
	date is string in format DD:MM:YYYY with the update time;
	hour is string in format HH:MN: with the update hour;
	periodAfter is a int with the number of minutes of a period 
	of time elapsed.
	Ensures:
	a list of translation tasks assigned according to the conditions
	indicated in the general specification (omitted here for 
	the sake of readability).
	"""

	uptasks = deepcopy(tasks)
	numbertasks = len(uptasks) #number of tasks to be assigned

	assignedTasks = [] #list with sublists of assigned tasks

	dateinfo = updatedate(date, hour, periodAfter) #list with the date and hour of the next update

	for t in range(0,numbertasks):
		uptranslators = deepcopy(translators)
		possibleTranslators = sorted(uptranslators)
		subtask = deepcopy(uptasks[t])
		subtaskwords = int(subtask[INDEXTaskWords])
		subtaskname = subtask[INDEXTaskID]
		original_language = subtask[INDEXWrittenLanguage]
		wanted_language = subtask[INDEXTranslatedLanguage]
		criterion = subtask[INDEXTaskCriterion]

		possible = tuple(possibleTranslators)
		for name in possible:
			availablewords = int(uptranslators[name][INDEXTranslatorMaxWords]) - int(uptranslators[name][INDEXTranslatorWords])
			if (availablewords < subtaskwords):
				possibleTranslators.remove(name)

		possible = tuple(possibleTranslators)
		for name in possible:
			languageFrom = uptranslators[name][INDEXFromLanguage]
			languageFrom = languageFrom[1:(len(languageFrom) - 1)]
			languageFrom = languageFrom.split("; ")
			languageTo = uptranslators[name][INDEXToLanguage]
			languageTo = languageTo[1:(len(languageTo) - 1)]
			languageTo = languageTo.split("; ")
			capable = True
			if original_language not in languageFrom:
				capable = False
			if wanted_language not in languageTo:
				capable = False
			if capable == False:
				possibleTranslators.remove(name)

		#choice of translator dependent of what the task's criterion is
		if criterion == CritQuality:
			critQuality(uptranslators, subtask, possibleTranslators)
		elif criterion == CritPrice:
			critPrice(uptranslators, subtask, possibleTranslators)
		elif criterion == CritSpeed:
			critSpeed(uptranslators, subtask, possibleTranslators)

		assigntask = []
		if (len(possibleTranslators) != 0):
			possibleTranslators = sorted(possibleTranslators, key=str.lower)
			assigntranslator = possibleTranslators[0]
			comp = datesComparison(dateinfo[0],uptranslators[assigntranslator][INDEXTranslatorDelivery]) #checks the later date between the header date and the last assigned task date
			if comp == dateinfo[0]:
				usedate = uptranslators[assigntranslator][INDEXTranslatorDelivery]
			elif comp == uptranslators[assigntranslator][INDEXTranslatorDelivery]:
				usedate = dateinfo[0]
			numberdays = subtaskwords/int(uptranslators[assigntranslator][INDEXTranslatorRhythm]) #number of days required to complete task
			for d in range(0,numberdays+1):
				usedate = dateChange(usedate) #sums the number of days required to complete task
			totalprice = int(round(float(uptranslators[assigntranslator][INDEXTranslatorPrice])*float(subtaskwords)))
			assigntask.append(usedate)
			assigntask.append(assigntranslator)
			assigntask.append(totalprice)
			assigntask.append(subtaskname)
		elif (len(possibleTranslators) == 0):
			usedate = dateinfo[0]
			assigntranslator = NOTAssigned
			totalprice = NOTApplicable
			assigntask.append(usedate)
			assigntask.append(assigntranslator)
			assigntask.append(totalprice)
			assigntask.append(subtaskname)

		assignedTasks.append(assigntask)
		intermediateTask = []
		assigntask.append(subtaskwords)
		intermediateTask.append(assigntask)
		updateTranslators(translators,intermediateTask) #updates the modified translator
		del assigntask[4] #deletes the task's words variable because it is only needed in the translator information and not in the assigned task information

	return assignedTasks




def updateTranslators(translators, schedule):

	"""
	Updates the translators dictionary with updated information
	as new tasks are assigned.

	Requires:
	translators is a dict with a structure as in the output of
	readingFromFiles.readTranslatorsFile;
	schedule is a list of translation tasks assigned according
	to the conditions indicated in the general specification
	(omitted here for the sake of readability).
	Ensures:
	updated translators dictionary with the updated info according
	to the new tasks assigned.
	"""

	for i in range(0,len(schedule)):
		name = schedule[i][INDEXAssignedTranslator] #name of the translator with the assigned task
		if name != NOTAssigned:
			date = schedule[i][INDEXScheduleDate] #date of delivery for new assigned task
			words = int(schedule[i][4]) #number of words of new assigned task
			translators[name][INDEXTranslatorWords] = int(translators[name][INDEXTranslatorWords])
			translators[name][INDEXTranslatorWords] = str(translators[name][INDEXTranslatorWords] + words) #updates the number of translator's accumulated words
			translators[name][INDEXTranslatorDelivery] = str(date) #updates the translator's date of last delivery according to the new assigned task

	return translators

