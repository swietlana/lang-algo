import random
print("\nHi!\n")

words = {'kot':'cat','pies':'dog','słoń':'elephant', 'mysz': 'mouse', 'wąż': 'snake', 'ślimak': 'snail'}

bad = ["Wrong. You need to practise more.", "Oops. Somebody skipped some classes."]
good = ["Congratulations!", "Yes!", "Great!", "You're great.", "Keep going!"]

for i in words:
	print ("\nHow would you say in English: %s ?" % i)
	answer = input()
	if answer == words[i]:
		print("%s" % random.choice(good))
	else:
		print("%s The proper answer is %s." % (random.choice(bad), words[i]))



