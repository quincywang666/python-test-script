#!python

from random import randrange

coinUser,coinBot=10,10
roundOfGames=0

def bet(dice,wager):
	if dice == 7:
		print(f'The dice is {dice};\nDRAW!\n')
		return 0
	elif dice < 7:
		if wager == 's':
			print(f'The dice is {dice};\nYou WIN!\n')
			return 1
		else:
			print(f'The dice is {dice};\nYou LOST!\n')
			return -1
	elif dice>7:
		if wager == 's':
			print(f'The dice is {dice};\nYou LOST!\n')
			return -1
		else:
			print(f'The dice is {dice};\nYou WIN!\n')
			return 1

while True:
	print(f'You: {coinUser}\t Bot:{coinBot}')
	dice = randrange(2,13)
	wager = input("What's your bet?")
	if wager == 'q':
		break
	elif wager in 'bs':
		result=bet(dice,wager)
		coinUser += result
		coinBot -= result
		roundOfGames +=1
	if coinUser == 0:
		print("Woops,you're LOST ALL,and game over!")
		break
	elif coinBot == 0:
		print("Woops, the robot's LOST ALL, and game over!")
		break

print(f"You've played {roundOfGames} rounds.\n")
print(f"You have {coinUser} coins now.\nBye!")

