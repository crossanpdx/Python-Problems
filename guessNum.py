import random

randNum = random.randrange(1, 1000)

def guess(num1):
	correct = False
	while not correct:
		if num1 > randNum:
			print "That's too high. Guess again. "
			print ""
		elif num1 < randNum:
			print "That's too low. Guess again. "
			print ""
		elif num1 == randNum:
			break
		num1 = input ("What is your guess? ")
	if num1 == randNum:
		guessAgain = raw_input ("Radical! That's the correct number. Guess again? ")
		if guessAgain == "n":
			print "Thanks for guessing. Come again. "
		elif guessAgain == "y":
			main()


def main():
	print ""
	num = input("Guess and number between 1 and 1000: ")
	guess(num)

main()
