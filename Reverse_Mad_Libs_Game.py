mad_libs_text_easy = ("A ___1___ is a place that you can store value(s) in your code. A ___1___ can store a single value, such " 
					"as a number or string, or multiple values. For example, a ___2___ is a data structure that stores multiple " 
					"values, enclosed in brackets. You will want to name your ___1___ as descriptive as possible so others can " 
					"understand your code. ___3___, which take in some input and produce an output, are blocks of reusable code " 
					"that perform some action. When you run into errors in your ___3___, you will need to use some ___4___ " 
					"best-practices to find and correct the issues so your code runs as it should.")

mad_libs_text_medium = ("A ___1___ is a place that you can store value(s) in your code. A ___1___ can store a single value, such "
					"as a number or string, or multiple values. For example, a ___2___ is a data structure that stores multiple "
					"values, enclosed in brackets. You will want to name your ___1___ as descriptive as possible so others can "
					"understand your code. ___3___, which take in some input and produce an output, are blocks of reusable code "
					"that perform some action. Inside of our ___3___, we can use a number of different commands to achieve our "
					"eventual output. We can use ___4___ to repeat some action n number of times. When you run into errors "
					"in your code, you will need to use some ___5___ best-practices to find and correct the issues so your code "
					"runs as it should.")

mad_libs_text_hard = ("A ___1___ is a place that you can store value(s) in your code. A ___1___ can store a single value, such "
					"as a number or string, or multiple values. For example, a ___2___ is a data structure that stores multiple "
					"values, enclosed in brackets. You will want to name your ___1___ as descriptive as possible so others can "
					"understand your code. ___3___, which take in some ___4___ and produce an ___5___, are blocks of reusable code "
					"that perform some action. Inside of our ___3___, we can use a number of different commands to achieve our "
					"eventual output. We can use ___6___ to repeat some action n number of times. But be careful - you do not want "
					"to create an ___7___ and possibly crash your computer. When you run into errors in your code, you will need to "
					"use some ___8___ best-practices to find and correct the issues so your code runs as it should.")

answer_key_easy = [["___1___", "VARIABLE"], ["___2___", "LIST"], ["___3___", "FUNCTIONS"], ["___4___", "DEBUGGING"]]

answer_key_medium = [["___1___", "VARIABLE"], ["___2___", "LIST"], ["___3___", "FUNCTIONS"], ["___4___", "LOOPS"], ["___5___", "DEBUGGING"]]

answer_key_hard = [["___1___", "VARIABLE"], ["___2___", "LIST"], ["___3___", "FUNCTIONS"], ["___4___", "INPUT"], ["___5___", "OUTPUT"], 
["___6___", "LOOPS"], ["___7___", "INFINITE-LOOP"], ["___8___", "DEBUGGING"]]

mad_libs_easy = {mad_libs_text_easy: answer_key_easy}

mad_libs_medium = {mad_libs_text_medium: answer_key_medium}

mad_libs_hard = {mad_libs_text_hard: answer_key_hard}


def find_difficulty_level():
	'''Finds the user's desired difficulty level'''
	accepted_difficulties = ["EASY", "MEDIUM", "HARD"]
	user_difficulty = raw_input("Please choose difficulty level (Easy, Medium, Hard): ")
	while user_difficulty.upper() not in accepted_difficulties:
		print "Invalid Response. Please enter either Easy, Medium or Hard."
		user_difficulty = raw_input("Please choose difficulty level (Easy, Medium, Hard): ")
	user_difficulty = user_difficulty.upper()
	return user_difficulty


def find_mad_libs_info(difficulty_level):
	'''Finds the corresponding Mad Libs text and answer key depending on difficulty level'''
	if difficulty_level == "EASY":
		return mad_libs_easy
	elif difficulty_level == "MEDIUM":
		return mad_libs_medium
	elif difficulty_level == "HARD":
		return mad_libs_hard

def fill_in_mad_libs(text, answer_key):
	'''Fills in correct user answer for mad libs game and prints new text with correct answer filled in'''
	for blank, answer in answer_key:
			print "\n" + str(text) + "\n"
			replaced  = []
			text = text.split()
			question = "What is the correct word for " + str(blank) + "?: "
			user_answer = raw_input(question)
			while user_answer.upper() != answer:
				print "Invalid answer. Try again!"
				user_answer = raw_input(question)
			for word in text:
				if blank in word:
					replaced.append(user_answer)
				else:
					replaced.append(word)
			text = " ".join(replaced)


def reverse_mad_libs_game(text_and_answer_key):
	'''Reverse Mad Libs Game: User fills in blanks in the text with correct answers'''
	for text, answer_key in text_and_answer_key.iteritems():
		fill_in_mad_libs(text, answer_key)
		print text

reverse_mad_libs_game(find_mad_libs_info(find_difficulty_level()))


