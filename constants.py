#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 60
# 43558 Nuno Amaral Soares
# 50021 Bruno Miguel da Silva Machado



# This module records the constants used in the application


# Value for translator's name in task not assigned in the output schedule
NOTAssigned = "not-assigned"


# Value for cost in task not assigned in the output schedule
NOTApplicable = "not-applicable"


# Number of minutes between updates
periodafter = 10


# Criterium for specific task is quality
CritQuality = 'quality'


# Criterium for specific task is price
CritPrice = 'price'


# Criterium for specific task is speed
CritSpeed = 'speed'


# In a file:
# Number of line in a header
NUMBEROfLinesInHeader = 7


# In a translators' list:
# Index of element with translator's name
INDEXTranslatorName = 0

# In a translator list inside a translators dictionary:
# Index of translator's possible languages from which he can translate
INDEXFromLanguage = 0

# Index of translator's possible languages to which he can translate
INDEXToLanguage = 1

# Index of translator's quality level
INDEXTranslatorQuality = 2

# Index of translator's price per word
INDEXTranslatorPrice = 3

# Index of translator's rhythm (number of words translated per day)
INDEXTranslatorRhythm = 4

# Index of translator's maximum accumulated words
INDEXTranslatorMaxWords = 5

# Index of translator's current accumulated words
INDEXTranslatorWords = 6

# Index of translator's last delivery date
INDEXTranslatorDelivery = 7


# In a specific task list:
# Index of task ID
INDEXTaskID = 0

# Index of task's written language
INDEXWrittenLanguage = 1

# Index of task's translated language
INDEXTranslatedLanguage = 2

# Index of task's quality level wanted
INDEXTaskQuality = 3

# Index of task's number of words
INDEXTaskWords = 4

# Index of task's criterion
INDEXTaskCriterion = 5

# Index of task's entity
INDEXTaskEntity = 6


# In a schedule list:

# Index of task's delivery date
INDEXScheduleDate = 0

# Index of task's assigned translator (possibly not-assigned)
INDEXAssignedTranslator = 1

# Index of task's total price
INDEXSchedulePrice = 2

# Index of task's entity
INDEXScheduleEntity = 3

