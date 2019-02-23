import random 
import os
from termcolor import colored

# Print multiline instruction 
# performstring concatenation of string 
def play():
	width = os.get_terminal_size().columns
	print('==========================================================='.center(width))
	print("Winning Rules of the Rock paper scissor game as follows: ".center(width))
	print("Rock vs paper->paper wins ".center(width))
	print("Rock vs scissor->Rock wins ".center(width))
	print("paper vs scissor->scissor wins ".center(width))


	while True:
		win = {
			'computer':0,
			'user':0,
		}

		print('\n\nYOU WILL GET THREE CHANCES'.center(width))
		for i in range(3):
			print("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n") 
			
			# take the input from user 
			choice = int(input("Your turn: ")) 
		 
			while choice > 3 or choice < 1: 
				choice = int(input("enter valid input: "))
				os.system('clear') 
				


			if choice == 1: 
				choice_name = 'Rock'
			elif choice == 2: 
				choice_name = 'Paper'
			else: 
				choice_name = 'Scissor'
				
			# print user choice 
			print('\n'+"Your choice is: " + choice_name)
			print("\nNow its computer turn.......") 


			comp_choice = random.randint(1, 3) 
			

			while comp_choice == choice: 
				comp_choice = random.randint(1, 3) 


			if comp_choice == 1: 
				comp_choice_name = 'Rock'
			elif comp_choice == 2: 
				comp_choice_name = 'Paper'
			else: 
				comp_choice_name = 'Scissor'
				
			print("Computer choice is: " + comp_choice_name) 

			print(choice_name + " V/s " + comp_choice_name) 

			# condition for winning 
			if((choice == 1 and comp_choice == 2) or
			(choice == 2 and comp_choice ==1 )): 
				print("Paper wins => ",) 
				result = "Paper"
				
			elif((choice == 1 and comp_choice == 3) or
				(choice == 3 and comp_choice == 1)): 
				print("Rock wins =>",) 
				result = "Rock"
			else: 
				print("Scissor wins =>",) 
				result = "Scissor"

			# Printing either user or computer wins 
			
			if result == choice_name:
				win['user']+=1
			else:
				win['computer']+=1
				
		print(chr(27) + "[2J")
		if win['computer']>win['user']:
			cprint(figlet_format('Computer won ', font='starwars'),'white', 'on_red', attrs=['bold','blink'])
		else:
			cprint(figlet_format(' You won', font='starwars'),'white', 'on_blue', attrs=['bold','blink'])

		print("Do you want to play again? (Y/N)") 
		ans = input() 


		# if user input n or N then condition is True 
		if ans == 'n' or ans == 'N': 
			break


	print("\nThanks for playing.") 

if __name__=='__main__':
	import sys

	from colorama import init
	init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
	from termcolor import cprint 
	from pyfiglet import figlet_format

	cprint(figlet_format('ROCK PAPER SCISSOR!', font='starwars'),
	       'white', 'on_blue', attrs=['bold','blink'])

	play()