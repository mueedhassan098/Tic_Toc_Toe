import pygame  # Import the pygame library for handling game graphics and events

# Initialize the pygame modules
pygame.init()

# ---------- CONSTANTS SECTION ----------

# Set the width and height of the game window
WIDTH, HEIGHT = 600, 600

# Set the thickness of the lines used for the grid
LINE_WIDTH = 15

# Define the size of the game board (3x3 for Tic-Tac-Toe)
BOARD_ROWS, BOARD_COLS = 3, 3

# Size of each square on the board
SQUARE_SIZE = WIDTH // BOARD_COLS

# Radius and width for drawing circles (O)
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15

# Width for drawing the X lines
CROSS_WIDTH = 25

# Define color constants using RGB tuples
BG_COLOR = (28, 170, 156)         # Background color
LINE_COLOR = (23, 145, 135)       # Grid line color
CIRCLE_COLOR = (239, 231, 200)    # Color of O
CROSS_COLOR = (66, 66, 66)        # Color of X

# ---------- DISPLAY SETUP ----------

# Create the game window using the specified width and height
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the game window
pygame.display.set_caption("Tic-Tac-Toe")

# Fill the window with the background color
screen.fill(BG_COLOR)

# ---------- GAME STATE ----------

# Create a 3x3 board initialized with None values
# This represents an empty board
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# ---------- FUNCTION DEFINITIONS ----------

def draw_grid():
    """Draw grid lines on the game board."""
    for i in range(1, BOARD_ROWS):
        # Draw horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        # Draw vertical lines
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    """Draw Xs and Os on the board based on player moves."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "O":
                # Draw a circle for player O
                pygame.draw.circle(
                    screen,
                    CIRCLE_COLOR,
                    (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH
                )
            elif board[row][col] == "X":
                # Calculate start and end points for drawing X
                start_desc = (
                    col * SQUARE_SIZE + SQUARE_SIZE // 4,
                    row * SQUARE_SIZE + SQUARE_SIZE // 4
                )
                end_desc = (
                    col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4,
                    row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4
                )
                # Draw the first diagonal line of X
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                # Draw the second diagonal line of X (crossing the first)
                pygame.draw.line(screen, CROSS_COLOR, (start_desc[0], end_desc[1]), (end_desc[0], start_desc[1]), CROSS_WIDTH)

def check_winner(player):
    """Check if the given player (X or O) has won."""
    # Check all rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check all columns
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            return True
    # Check diagonal (top-left to bottom-right)
    if all(board[i][i] == player for i in range(BOARD_ROWS)):
        return True
    # Check diagonal (top-right to bottom-left)
    if all(board[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)):
        return True
    return False  # Return False if no win is detected

# ---------- INITIAL DRAW ----------

# Draw the grid lines before the game starts
draw_grid()

# Set the initial player (X starts first)
player_turn = "X"

# Control variable to keep the game loop running
running = True

# ---------- GAME LOOP ----------

while running:
    # Loop through all events (like clicks or quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If window is closed, stop the game loop
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position where the mouse was clicked
            x, y = event.pos

            # Determine the row and column based on click position
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE

            # Only allow move if the clicked cell is empty
            if board[row][col] is None:
                # Place the current player's symbol on the board
                board[row][col] = player_turn

                # Redraw the board with the new move
                draw_figures()

                # Check if current player has won
                if check_winner(player_turn):
                    print(f"{player_turn} wins!")  # Print the winner to console
                    running = False               # Stop the game loop

                # Switch turns between X and O
                player_turn = "O" if player_turn == "X" else "X"

    # Update the display to reflect new drawings
    pygame.display.update()

# Quit pygame after exiting the game loop
pygame.quit()
