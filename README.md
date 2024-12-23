# Tic-Tac-Toe Game (Player vs AI)
# X-O-game-Ai-Project-

This project is a graphical **Tic-Tac-Toe** game built using Python and the Pygame library. It features a player-versus-AI setup where the player (X) competes against an AI opponent (O) on a 3x3 grid.

---

## Features

- **Dynamic Gameplay**: A 3x3 Tic-Tac-Toe grid with real-time player and AI turns.
- **AI Logic**: The AI opponent is implemented using the **minimax algorithm** to make optimal moves.
- **Graphical Interface**: The game includes a grid, markers (X and O), and result messages rendered using Pygame.
- **Win and Draw Detection**: Automatic checking for game-ending conditions with visual feedback.

---

## How It Works

1. **Game Board**: A 3x3 grid represented by a 2D list, with each square being clickable for the player.
2. **AI Decision-Making**:
   - The AI uses the **minimax algorithm** to evaluate all possible board states.
   - It chooses the move that maximizes its chances of winning while minimizing the player's chances.
3. **Win/Draw Conditions**:
   - **Win**: Three consecutive Xs or Os in a row, column, or diagonal.
   - **Draw**: All cells filled without a winner.

---

## Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
   cd tic-tac-toe
