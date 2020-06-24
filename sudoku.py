import random

board =[ [
			[7,8,0,4,0,0,1,2,0],
			[6,0,0,0,7,5,0,0,9],
			[0,0,0,6,0,1,0,7,8],
			[0,0,7,0,4,0,2,6,0],
			[0,0,1,0,5,0,9,3,0],
			[9,0,4,0,6,0,0,0,5],
			[0,7,0,3,0,0,0,1,2],
			[1,2,0,0,0,7,4,0,0],
			[0,4,9,2,0,6,0,0,7]
		 ],
		 [
		  	[3,0,6,5,0,8,4,0,0], 
          	[5,2,0,0,0,0,0,0,0], 
          	[0,8,7,0,0,0,0,3,1], 
          	[0,0,3,0,1,0,0,8,0], 
          	[9,0,0,8,6,3,0,0,5], 
          	[0,5,0,0,9,0,6,0,0], 
          	[1,3,0,0,0,0,2,5,0], 
          	[0,0,0,0,0,0,0,7,4], 
         	[0,0,5,2,0,6,3,0,0]
         ],
         [
         	[3,8,5,0,0,0,0,0,0],
   			[9,2,1,0,0,0,0,0,0],
   			[6,4,7,0,0,0,0,0,0], 
   			[0,0,0,1,2,3,0,0,0],
   			[0,0,0,7,8,4,0,0,0], 
   			[0,0,0,6,9,5,0,0,0], 
   			[0,0,0,0,0,0,8,7,3], 
   			[0,0,0,0,0,0,9,6,2], 
   			[0,0,0,0,0,0,1,4,5] 
         ],
		]
		
def solve(bo):
	find = is_empty(bo)
	if find:
		row,col = find
	else:
		return True

	for i in range(1,10):
		if is_valid(bo,(row,col),i):
			bo[row][col]=i

			if solve(bo):
				return True
			bo[row][col]=0
	return False

def is_valid(bo,pos,num):
	#for rows
	for i in range(len(bo[0])):
		if(bo[pos[0]][i]==num and pos[1]!=i):
			return False
	#for columns
	for i in range(len(bo)):
		if(bo[i][pos[1]]==num and pos[0]!=i):
			return False
	#for box
	box_x = pos[1]//3
	box_y = pos[0]//3

	for i in range(box_y*3,box_y*3+3):
		for j in range(box_x*3,box_x*3+3):
			if bo[i][j]==num and pos!=(i,j):
				return False
	return True

def is_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j]==0:
				return (i,j)
	return None

def show_board(bo):
	for i in range(len(bo)):
		if i%3==0 and i!=0:
			print("- - - - - - - - - - - - - - - - -")
		for j in range(len(bo[0])):
			if j%3==0 and j!=0:
				print(" | ",end=" ")
			if j==8:
				print(bo[i][j])
			else:
				print(str(bo[i][j]) + " ",end=" ")

ran = random.randrange(len(board))
show_board(board[ran])
print("After solving....")
solve(board[ran])
show_board(board[ran])