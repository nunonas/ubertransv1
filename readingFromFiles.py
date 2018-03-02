#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 60
# 43558 Nuno Amaral Soares
# 50021 Bruno Miguel da Silva Machado

from constants import *

def removeHeader(opened_file):
	""" Skips the header present on the beginning
    of the text file.

    Requires: an opened text file with a header that complies
    with the specifications of the project's list headers
    Ensures: The opened file, with the filehandler now pointing
    to the first line after the header
	"""

	for i in range(NUMBEROfLinesInHeader):
		opened_file.readline()

	return opened_file



def readTranslatorsFile(file_name):
	"""Reads a file with a list of translators into a collection.

    Requires:
    file_name is str with the name of a .txt file containing
    a list of translators organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    dict where each item corresponds to a translator listed in
    file with name file_name, a key is the string with the name of a translator,
    and a value is the list with the other elements belonging to that
    translator, in the order provided in the lines of the file.
    """

	infile = removeHeader(open(file_name, "r"))
	translator_dict = {}
	for i in infile:
		if i != "\n":
			translatorsList = i.rstrip().split(", ")
			translatorName = translatorsList.pop(INDEXTranslatorName)
			translator_dict[translatorName] = translatorsList


	infile.close()
	return translator_dict



def readTasksFile(file_name):
	"""Reads a file with a list of translation tasks into a collection.

	Requires:
    file_name is str with the name of a .txt file containing
    a list of translation tasks organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list with various sublists, with each sublist corresponding to a specific
    task with its various parameters. Each line in the input file corresponds
    to a different subtask.
    """

	inFile = removeHeader(open(file_name, "r"))

	tasksList = []
	for line in inFile:
		if line != "\n":
			taskData = line.rstrip().split(", ")
			tasksList.append(taskData)

	inFile.close()
	return tasksList
