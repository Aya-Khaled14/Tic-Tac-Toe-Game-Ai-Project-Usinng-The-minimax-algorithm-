import pygame
import sys
import random

# Game settings
WIDTH, HEIGHT = 300, 300
GRID_SIZE = 3
SQUARE_SIZE = WIDTH // GRID_SIZE
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (255, 0, 0)  # Player - X
AI_COLOR = (0, 0, 255)      # AI - O

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe - X vs O")
clock = pygame.time.Clock()

# Game board initialization
board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = 'X'  # Player starts first

# Draw grid
def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
            if board[row][col] == 'X':
                pygame.draw.line(screen, PLAYER_COLOR, (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + 10), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 10, row * SQUARE_SIZE + SQUARE_SIZE - 10), 3)
                pygame.draw.line(screen, PLAYER_COLOR, (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + SQUARE_SIZE - 10), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 10, row * SQUARE_SIZE + 10), 3)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, AI_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3, 3)

# Check for winner
def check_winner():
    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

# Check for draw
def check_draw():
    for row in board:
        if None in row:
            return False
    return True

# Handle player event
def handle_event(event):
    global current_player
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
        if board[row][col] is None and current_player == 'X':
            board[row][col] = 'X'
            winner = check_winner()
            if winner:
                display_winner(winner)  # Display winner
                return  # End game after winner is found
            if check_draw():
                display_draw()  # Display draw
                return  # End game after draw
            current_player = 'O'  # Switch turn to AI

# Minimax AI algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner()
    if winner == 'X':
        return -10
    elif winner == 'O':
        return 10
    elif check_draw():
        return 0
    
    if is_maximizing:
        max_eval = -float('inf')
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if board[row][col] is None:
                    board[row][col] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = None
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if board[row][col] is None:
                    board[row][col] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = None
                    min_eval = min(min_eval, eval)
        return min_eval

# AI move
def ai_move():
    best_move = None
    best_value = -float('inf')
    
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] is None:
                board[row][col] = 'O'
                move_value = minimax(board, 0, False)
                board[row][col] = None
                if move_value > best_value:
                    best_value = move_value
                    best_move = (row, col)
    
    if best_move:
        row, col = best_move
        board[row][col] = 'O'
        winner = check_winner()
        if winner:
            display_winner(winner)  # Display winner
            return  # End game after AI wins
        if check_draw():
            display_draw()  # Display draw
            return  # End game after draw
        global current_player
        current_player = 'X'  # Switch turn to player after AI move

# Display winner message
def display_winner(winner):
    font = pygame.font.Font(None, 36)
    if winner == 'X':
        text = font.render("Player wins (X)!", True, PLAYER_COLOR)
    else:
        text = font.render("AI wins (O)!", True, AI_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()  # Update the screen with the message
    pygame.time.wait(2000)  # Wait for 2 seconds before closing the game
    pygame.quit()
    sys.exit()  # Close the game after displaying the winner

# Display draw message
def display_draw():
    font = pygame.font.Font(None, 36)
    text = font.render("It's a Draw!", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()  # Update the screen with the message
    pygame.time.wait(2000)  # Wait for 2 seconds before closing the game
    pygame.quit()
    sys.exit()  # Close the game after displaying the draw

# Main game loop
def main():
    global current_player
    while True:
        screen.fill(BLACK)
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            handle_event(event)
        
        if current_player == 'O':  # AI's turn
            ai_move()
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()