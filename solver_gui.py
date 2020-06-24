
import pygame
import time

pygame.init()

class MainBlock:
	board = [
            [3,0,6,5,0,8,4,0,0], 
            [5,2,0,0,0,4,0,0,0], 
            [0,8,7,0,0,0,0,3,1], 
            [0,0,3,0,1,0,0,8,0], 
            [9,0,0,8,6,3,0,0,5], 
            [0,5,0,0,9,0,6,0,0], 
            [1,3,0,0,0,0,2,5,0], 
            [0,0,0,0,0,0,0,7,4], 
            [0,0,5,2,0,6,3,0,0]
         ]
	
	def __init__(self, rows, cols, width, height, screen):
		self.rows = rows
		self.cols = cols
		self.width = width
		self.height = height
		self.screen = screen
		self.box = [[Box(i, j, width, height, self.board[i][j]) for j in range(cols)] for i in range(rows)]
		self.model = None
		self.update_model()

	def draw(self):
		cellSize = self.width//9

		for x in range(self.rows+1):
			if x%3 == 0:
				thick = 3
			else:
				thick = 1
			pygame.draw.line(self.screen, (0,0,0), (75,100 + cellSize*x), (75 + self.width,100 + cellSize*x), thick)	#horizontal lines 
			pygame.draw.line(self.screen, (0,0,0), (75 + cellSize*x,100), (75 + cellSize*x,100 + self.height), thick)	#vertical lines 

		#Draw blocks/boxes
		for i in range(self.rows):
			for j in range(self.cols):
				self.box[i][j].draw(self.screen)

	def solver(self):
		location = is_empty(self.model)
		if not location:
			return True
		else:
			row,col = location

		for i in range(1, 10):
			if is_valid(self.model, (row,col), i):
				self.box[row][col].set(i)
				self.box[row][col].draw_updates(self.screen, True)
				self.update_model()
				pygame.display.update()
				pygame.time.delay(50)

				if self.solver():
					return True

				self.box[row][col].set(0)
				self.update_model()
				self.box[row][col].draw_updates(self.screen, False)
				pygame.display.update()
				pygame.time.delay(50)

		return False

	def update_model(self):
		self.model = [[self.box[i][j].val for j in range(self.cols)] for i in range(self.rows)]

	def is_finished(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.box[i][j].val == 0:
					return False
		return True


class Box:
	rows = 9
	cols = 9

	def __init__(self, row, col, width, height, val):
		self.row = row
		self.col = col
		self.width = width
		self.height = height
		self.val = val
		self.temp = 0
		self.selected = False


	def draw(self, screen):

		fnt = pygame.font.SysFont("Comfortaa", 25)

		cellSize = self.width // 9
		x = self.col * cellSize
		y = self.row * cellSize

		if self.temp != 0 and self.val == 0:
			text = fnt.render(str(self.text), 1, (128, 128, 128))
			screen.blit(text, (x+75, y+100))

		elif not(self.val == 0):
			text = fnt.render(str(self.val), 1, (0, 0, 0))
			screen.blit(text, ((x+ 75) + (cellSize - text.get_width())//2, (y + 100) + (cellSize - text.get_height())//2))

		if self.selected:
			pygame.draw.rect(screen, (255,0,0), (75, 100, width, height), 2)


	def draw_updates(self, screen, correct=True):
		
		fnt = pygame.font.SysFont("Comfortaa", 25)

		cellSize = self.width // 9
		x = self.col * cellSize
		y = self.row * cellSize

		pygame.draw.rect(screen, (200, 190, 100), (x+75, y+100, cellSize, cellSize), 0)

		text = fnt.render(str(self.val), 1, (0, 0, 0))
		screen.blit(text, ((x + 75) + (cellSize - text.get_width())//2, (y + 100) + (cellSize - text.get_height())//2))
		if correct:
			pygame.draw.rect(screen, (0, 255, 0), (x+75, y+100, cellSize, cellSize), 2)
		else:
			pygame.draw.rect(screen, (255, 0, 0), (x+75, y+100, cellSize, cellSize), 2)


	def set(self, val):
		self.val = val

	def set_temp(self, val):
		self.temp = val
		

def is_valid(bo, pos, num):
	#for rows
	for i in range(len(bo[0])):
		if bo[pos[0]][i] == num and pos[1] != i:
			return False

	#for cols
	for i in range(len(bo)):
		if bo[i][pos[1]] == num and pos[0] != i:
			return False

	#for 3x3 blocks 
	block_x = pos[1]//3
	block_y = pos[0]//3

	for i in range(block_y*3, block_y*3 + 3):
		for j in range(block_x*3, block_x*3 + 3):
			if bo[i][j] == num and (i,j) != pos:
				return False
	return True

def is_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return (i, j)
	return None

def redraw_window(screen, board, time):	
	screen.fill((200, 190, 100))

	# Draw timer
	fnt = pygame.font.SysFont("Comfortaa", 25)
	text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
	screen.blit(text, (600 - 200, 40))

	if board.is_finished():
			text = fnt.render("!!COMPLETED!!", 1, (0,0,0))
			screen.blit(text, (600 - 440, 40))

	text = fnt.render("Press SPACE to start!", 1, (0,0,0))
	screen.blit(text, (600 - 440, 560))

	# Draw grid
	board.draw()

def format_time(secs):				#Timer
	sec = secs % 60
	minute = secs // 60
	hour = minute // 60

	counter = " " + str(minute) + ":" + str(sec)
	return counter


def main():

	screen = pygame.display.set_mode((600, 600))	#Screen size
	pygame.display.set_caption("Sudoku")			#Game name
	icon = pygame.image.load("sudoku.png")			#Load icon
	pygame.display.set_icon(icon)					#Set icon
	board = MainBlock(9, 9, 450, 450, screen)
	key = None
	run = True
	start = time.time()

	while run:
		play_time = round(time.time() - start)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					board.solver()

		redraw_window(screen, board, play_time)
		pygame.display.update()

main()
pygame.quit()
