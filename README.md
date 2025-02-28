# Tic-Tac-Toe (CLI Version)

A simple command-line Tic-Tac-Toe game for two players. Players take turns entering their moves, and the game checks for a win or a draw.

## Features
- Two-player turn-based gameplay.
- Input validation to prevent incorrect or occupied moves.
- Supports **comma-separated** input (e.g., `1,2`).
- Displays the board after every move.
- Checks for win conditions and declares a winner or a draw.

## How to Play
1. Run the script using Python:
   ```sh
   python day7.py
   ```
2. Players take turns entering their moves using **comma-separated row and column numbers** (e.g., `1,2`).
3. The board updates after each move, showing the current state.
4. The game ends when a player wins or the board is full (draw).

## Input Format
- The game board follows a **1-based index**:
  ```
   1 | 2 | 3
  ---------
   4 | 5 | 6
  ---------
   7 | 8 | 9
  ```
- Enter your move as `row,column` (e.g., `1,2` places your mark in the first row, second column).

## Example Game Flow
```
Player X, enter your move (row and column, e.g., 1,2): 1,2
  | X |  
---------
  |   |  
---------
  |   |  

Player O, enter your move (row and column, e.g., 1,2): 2,2
  | X |  
---------
  | O |  
---------
  |   |  
```

## Requirements
- Python 3.x

## Future Enhancements
- Add an AI opponent for single-player mode.
- Implement a graphical interface using Tkinter or Pygame.

Enjoy playing Tic-Tac-Toe! Made BY Paras 🎮

