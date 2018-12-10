#!/usr/bin/python3
def clear_output():
	for line in range(50):
		print(' ')

def display_board(board):
	clear_output()
	print('    |   |')
	print('  ' + board[7]+' | '+board[8]+' | '+board[9])
	print('    |   |')
	print('------------')
	print('    |   |')
	print('  ' + board[4]+' | '+board[5]+' | '+board[6])
	print('    |   |')
	print('------------')
	print('    |   |')
	print('  ' + board[1]+' | '+board[2]+' | '+board[3])

test_board = ['#','1','2','3','4','5','6','7','8','9']
display_board(test_board)
display_board(test_board)

def player_input():
	
	marker = ''
	
	while marker != 'X' and merker != 'O':
		marker = input('Player1: Choose X or O: ').upper()

	if marker == 'X':

		return ('X','O')
	else:
		return ('O', 'X')

def place_marker(board, marker, position):

	board[position] = marker

def win_check(board, mark):

	(board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark) or


place_marker(test_board,'#',7)
display_board(test_board)

def space_check(board, position):
	return board[position] == ' '

def full_board_check(board):

	for parts in range(1, 10):
		if space_check(board, parts):
			return False

	return True

def player_choice(board):

	position = 0

	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
		position = int(input('Choose a position: (1-9) '))

	return position

def replay():

	choice = input("Play again? Yes or No")

	if choice[0].lower() == 'y':

		return choice = 'Yes' 

#primary while loop
print('Welcome to Tic-Tac-Toe')

while True:

	## Set Up variables(board, player selection, choose markers X,O )
	the_board = ['']*10	
	player1_marker,player2_marker = player_input()

	turn = choose_first()
	print(turn + ' will go first')

	play_game = input('Ready to play? (y/n) ')
	
	if play_game[0].lower() == 'y':
		game_on = True
	else:
		game_on =False

	while game_on:
	
		if turn == 'Player 1':
			display_board(the_board)
			position = player_choice(the_board)
			place_marker(the_board,player1_marker,position)

			if win_check(the_board,player1_marker,position):
				display_board(the_board)
				print('Player 1 has won!!')
				game_on = False
			else:
				if full_board_check(the_board):
					display_board()
					print('Tie Game!')
					game_on = False
				else:
					turn = 'Player 2'
		else:

		
	#break out on the reply()
	if not replay():
		break




