import random

class tictactoe():
	# Game Grid #
	game_grid = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
	Player1_name = "Player1"
	Player2_name = "Player2"
	Player1_turn = True
	Player2_turn = False
	game_counter = 0

	# Game Grid Display #
	def display_grid(self,game_grid):
		print ("===TIC===TAC===TOE===")
		print ( "||[ "+ game_grid[6] + " ]","[ "+ game_grid[7] + " ]","[ "+ game_grid[8] + " ]||")
		print ( "||[ "+ game_grid[3] + " ]","[ "+ game_grid[4] + " ]","[ "+ game_grid[5] + " ]||")
		print ( "||[ "+ game_grid[0] + " ]","[ "+ game_grid[1] + " ]","[ "+ game_grid[2] + " ]||")
		print ("=====================")

	# Game Grid Display END #

	# Input #
	def input_cell(self):
		test_list = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
		print ("Press the number of Cell:")
		cellnum = input()
		if cellnum in test_list:
			cellnum = int(cellnum)
			return cellnum
		else:
			print ("You entered a wrong number!")
			return False

	# Checking of the cell #
	def cell_check(self,cell,game_grid,player1_turn):
		temp = int(cell) - 1
		if game_grid[temp] == 'X' or game_grid[temp] == 'O':
			print ("Cell is Occupied!")
			print ("Enter again!")
			return player1_turn
			
		else:	
			if player1_turn == True:
				game_grid[temp] = 'X'
				return False
			else:
				game_grid[temp] = 'O'
				return True
				
	# Checking of the cell END #


	# Check pattern #
	def patter_check(self,game_grid):
#check if X
		if game_grid[0] == 'X'and game_grid[1]=='X' and game_grid[2]=='X':
			return 1
		if game_grid[3] == 'X'and game_grid[4]=='X' and game_grid[5]=='X':
			return 1
		if game_grid[6] == 'X'and game_grid[7]=='X' and game_grid[8]=='X':
			return 1
		if game_grid[0] == 'X'and game_grid[3]=='X' and game_grid[6]=='X':
			return 1
		if game_grid[1] == 'X'and game_grid[4]=='X' and game_grid[7]=='X':
			return 1
		if game_grid[2] == 'X'and game_grid[5]=='X' and game_grid[8]=='X':
			return 1
		if game_grid[0] == 'X'and game_grid[4]=='X' and game_grid[8]=='X':
			return 1
		if game_grid[6] == 'X'and game_grid[4]=='X' and game_grid[2]=='X':
			return 1
#check if O		
		if game_grid[0] == 'O'and game_grid[1]=='O' and game_grid[2]=='O':
			return 2
		if game_grid[3] == 'O'and game_grid[4]=='O' and game_grid[5]=='O':
			return 2
		if game_grid[6] == 'O'and game_grid[7]=='O' and game_grid[8]=='O':
			return 2
		if game_grid[0] == 'O'and game_grid[3]=='O' and game_grid[6]=='O':
			return 2
		if game_grid[1] == 'O'and game_grid[4]=='O' and game_grid[7]=='O':
			return 2
		if game_grid[2] == 'O'and game_grid[5]=='O' and game_grid[8]=='O':
			return 2
		if game_grid[0] == 'O'and game_grid[4]=='O' and game_grid[8]=='O':
			return 2
		if game_grid[6] == 'O'and game_grid[4]=='O' and game_grid[2]=='O':
			return 2

		else:
			return 0
		
# Done Checking Done #
		

	# Check pattern END #
# Class tictactoe END #
#
#
#
#
# tictactoe.py start #
game = True
while game == True:
# Game Condition #
	game_mode = True
#################

# Class Loading #
	t = tictactoe()
# Class Loaded #

	print ("Welcome to Tic-Tac-Toe")
	print ("Enter Player 1 name:")
	input_name = input();

#Checking player 1 name if blank
	if input_name != "":
		t.Player1_name = input_name

	print ("Hello " + t.Player1_name)
	print ("Enter Player 2 name:")
	input_name = input()

#Checking player 2 name if blank
	if input_name != "":
		t.Player2_name = input_name

	print ("Hello " + t.Player2_name)

# Game Starting #
	print ( t.Player1_name + " is X")
	print ( t.Player2_name + " is O")

# Game Start #
	while game_mode == True:
		if t.game_counter ==8:
			print ("Tie")
			break
		

	# Printing the Grid #
		t.display_grid(t.game_grid)
	
	# Whose turn now? #

		if t.Player1_turn == True:
			print ( t.Player1_name + " turn! X")
		else:
			print ( t.Player2_name + " turn! O")

		cellnum = False
		temp_status = t.Player1_turn
		
		while temp_status == t.Player1_turn:
			while cellnum == False:
					cellnum = t.input_cell()
			t.Player1_turn = t.cell_check(cellnum,t.game_grid,t.Player1_turn)
			cellnum = False
		t.game_counter+=1

		checkme = t.patter_check(t.game_grid)
		if checkme == 1:
			t.display_grid(t.game_grid)
			print (t.Player1_name + " win!")
			break
		elif checkme == 2:
			t.display_grid(t.game_grid)
			print (t.Player2_name + " win!")	
			break

	print("Want to play again? [Y/N]")
	game_again = input()
	if game_again == 'N' or game_again=='n':
		break		
