from graphics import *

# Constants
GRID_SIZE = 3  # Number of rows and columns in the grid
GRID_PADDING = 50  # Padding between the edge of the window and the grid
CELL_SIZE = 100  # Size of each cell in the grid
WINDOW_SIZE = (2*GRID_PADDING + GRID_SIZE*CELL_SIZE, 2*GRID_PADDING + GRID_SIZE*CELL_SIZE)  # Size of the window

# Variables
current_player = "X"  # Current player (starts with X)
board = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Create an empty board

# Functions
def draw_grid():    
    """Draws the game grid"""
    for i in range(GRID_SIZE+1):
        # Draw horizontal lines
        h_line = Line(Point(GRID_PADDING, GRID_PADDING+i*CELL_SIZE), Point(WINDOW_SIZE[0]-GRID_PADDING, GRID_PADDING+i*CELL_SIZE))
        h_line.draw(win)
        
        # Draw vertical lines
        v_line = Line(Point(GRID_PADDING+i*CELL_SIZE, GRID_PADDING), Point(GRID_PADDING+i*CELL_SIZE, WINDOW_SIZE[1]-GRID_PADDING))
        v_line.draw(win)
        
def draw_symbol(row, col, symbol):
    """Draws a symbol (X or O) on the grid"""
    center = Point(GRID_PADDING + col*CELL_SIZE + CELL_SIZE/2, GRID_PADDING + row*CELL_SIZE + CELL_SIZE/2)
    if symbol == "X":
        line1 = Line(Point(center.getX()-CELL_SIZE/4, center.getY()-CELL_SIZE/4), Point(center.getX()+CELL_SIZE/4, center.getY()+CELL_SIZE/4))
        line2 = Line(Point(center.getX()+CELL_SIZE/4, center.getY()-CELL_SIZE/4), Point(center.getX()-CELL_SIZE/4, center.getY()+CELL_SIZE/4))
        line1.draw(win)
        line2.draw(win)
    elif symbol == "O":
        circle = Circle(center, CELL_SIZE/4)
        circle.draw(win)

def get_mouse_click():
    """Gets the next mouse click"""
    while True:
        click = win.getMouse()
        row = int((click.getY() - GRID_PADDING) / CELL_SIZE)
        col = int((click.getX() - GRID_PADDING) / CELL_SIZE)
        if row >= 0 and row < GRID_SIZE and col >= 0 and col < GRID_SIZE:
            return row, col

def check_win():
    """Checks if a player has won the game"""
    # Check rows
    for row in board:
        if all(cell == current_player for cell in row):
            return True
    
    # Check columns
    for col in range(GRID_SIZE):
        if all(board[row][col] == current_player for row in range(GRID_SIZE)):
            return True
    
    # Check diagonals
    if all(board[i][i] == current_player for i in range(GRID_SIZE)):
        return True
    if all(board[i][GRID_SIZE-1-i] == current_player for i in range(GRID_SIZE)):
        return True
    
    # No winner yet
    return False

# Initialize the graphics window
win = GraphWin("Tick-Tac-Toe", WINDOW_SIZE[0], WINDOW_SIZE[1])

# Draw the game grid
draw_grid()

# Game loop
while True:
    # Get the next player's move
    message = Text(Point(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]-GRID_PADDING/2), "Player {}'s turn".format(current_player))
    message.draw(win)
    row, col = get_mouse_click()
    
    # Check if the cell is already occupied
    if board[row][col] != "":
        message.setText("This cell is already occupied. Player {}'s turn".format(current_player))
        continue
    
    # Update the board and draw the symbol
    board[row][col] = current_player
    draw_symbol(row, col, current_player)
    
    # Check if the game is over
    if check_win():
        message.setText("Player {} wins!".format(current_player))
        break
    elif all(all(cell != "" for cell in row) for row in board):
        message.setText("It's a tie!")
        break
    
    # Switch to the other player
    current_player = "O" if current_player == "X" else "X"

# Wait for a mouse click before closing the window
win.getMouse()
win.close()



