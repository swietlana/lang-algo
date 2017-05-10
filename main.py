import random


class Language:
	def __init__(self, id, name, iso_code):
		self.id = id
		self.name = name
		self.iso_code = iso_code


class Word:
	def __init__(self, language, text, level):
		self.language = language
		self.text = text
		self.level = level

	def get_len(self, text):
		return len(text)


class Dictionary:
	def __init__(self, title, description, author, words, rate, date):
		self.title = title
		self.description = description
		self.author = author
		self.words = words
		self.rate = rate
		self.date = date
print("\nHi!\n")

words = {'kot':'cat','pies':'dog','słoń':'elephant', 'mysz': 'mouse', 'wąż': 'snake', 'ślimak': 'snail'}

bad = ["Wrong. You need to practise more.", "Oops. Somebody skipped some classes."]
good = ["Congratulations!", "Yes!", "Great!", "You're great.", "Keep going!"]

for i in words:
	print("\nHow would you say in English: %s ?" % i)
	answer = input()
	if answer == words[i]:
		print("%s" % random.choice(good))
	else:
		print("%s The proper answer is %s." % (random.choice(bad), words[i]))
