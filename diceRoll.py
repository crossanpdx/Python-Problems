import random

def dice(sides=6):
    return random.randint(1, sides)
	
def player_names():
	playerA = raw_input("Enter playerA name: ")
	playerB = raw_input("Enter playerB name: ")
	return playerA, playerB
	
def dice_roll(playerA, playerB):

	rollA = dice()
	
	rollB = dice()
	
	if rollA > rollB:
		return playerA
	elif rollB > rollA:
		return playerB
	else:
		return ""
		
def announceWinner(winner):
	print "The winner is: ",
	if winner == '':
		print "The game is a tie."
	else:
		print winner
	print
	
def main():
	playerA, playerB = player_names()
	roll_again = True
	while roll_again:
		print "Dice is rolling..."
		winner = dice_roll(playerA, playerB)
		announceWinner(winner)
		answer = raw_input("Care to roll again? (y/n) ")
		roll_again = answer.strip().lower() in ('y', 'yes')
main()
