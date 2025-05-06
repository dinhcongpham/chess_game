# Pygame Chess Game

This project is a two-player chess game developed using the Pygame library in Python. The game features a simple graphical interface and implements basic chess rules, allowing two players to compete against each other on the same computer.

## Key Features

The project successfully implements the following core chess game functionalities:

* **Check Detection:** The system can identify when a King is under attack by an opponent's piece and displays a warning.
* **Castling:** Supports the castling rule for both White and Black Kings, allowing simultaneous movement of the King and Rook according to the rules.
* **Legal Move Generation:** Accurately calculates and displays the squares where a selected piece can move legally, adhering to the movement rules of each piece type (Pawn, Knight, Bishop, Rook, Queen, King) and preventing moves to squares occupied by friendly pieces.
* **Visualization of Captured Pieces:** Pieces removed from the board are displayed in a separate area next to the board, helping players keep track of the number and type of pieces captured by each side.

## Installation

To run this game, you need to have Python and the Pygame library installed.

1.  **Install Python:**
    If you don't have Python installed, download and install the appropriate version for your operating system from the official website:
    [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  **Install Pygame:**
    Open your Terminal or Command Prompt and run the following command to install the Pygame library:
    ```bash
    pip install pygame
    ```

3.  **Download Source Code and Assets:**
    Download the `main.py` file (containing the game's source code) and ensure you have an `assets/images` folder containing the image files for the chess pieces (e.g., `black bishop.png`, `white king.png`, etc.). Place `main.py` and the `assets` folder in the same directory for your project. The directory structure should look like this:

    ```
    your_project_folder/
    ├── main.py
    └── assets/
        └── images/
            ├── black bishop.png
            ├── black king.png
            ├── black knight.png
            ├── black pawn.png
            ├── black queen.png
            ├── black rook.png
            ├── white bishop.png
            ├── white king.png
            ├── white knight.png
            ├── white pawn.png
            ├── white queen.png
            └── white rook.png
    ```
    *(Note: Based on the code, the game uses image files from the `assets/images` directory. Make sure you have all these image files.)*

## How to Run

Once you have completed the installation and file setup, open your Terminal or Command Prompt, navigate to your `your_project_folder` directory, and run the following command:

```bash
python main.py
```


## Code Structure

The `main.py` file contains the entire game logic, organized into the following main functions:

* `init_game_variable()`: Initializes all global variables and the initial state of the board, piece positions, captured pieces lists, turn step, etc.
* `draw_board()`: Draws the chess board interface, grid lines, and the area for displaying game status/captured pieces.
* `draw_pieces()`: Draws all the chess pieces at their current positions on the board.
* `check_options(pieces, locations, turn)`: A general function to calculate all possible moves for all pieces of a specific color (White or Black).
* `check_pawn()`, `check_rook()`, `check_king()`, `check_queen()`, `check_bishop()`, `check_knight()`: Helper functions for `check_options` to calculate moves specific to each piece type.
* `check_valid_moves()`: Filters the possible moves to show only the legal moves for the currently selected piece.
* `draw_valid(moves)`: Draws the small dots on the board to indicate the valid moves for the selected piece.
* `draw_captured()`: Draws the captured pieces in the dedicated display area.
* `draw_check()`: Draws a visual effect (e.g., a red border) around the King if it is in check.
* `draw_game_over()`: Displays the game over screen and the winner.
* Main game loop (`while run:`): This is the central control of the game, handling user events (like mouse clicks, key presses), updating the game state based on player actions, and calling the drawing functions to update the display.