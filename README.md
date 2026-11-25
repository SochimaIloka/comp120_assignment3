# Brick Blitz

## Group Members
- Sochima Iloka
- Jayden Wittock
- Kenneth Ezinma

## GitHub Repository
https://github.com

## Game Description & Objective
Brick Blitz is an arcade-style Python game built with Tkinter. The player controls a horizontal paddle to bounce a ball upward and break all bricks on the screen without letting the ball fall below the paddle.

## Game Rules
- The ball bounces off the left, right, and top walls, the paddle, and the bricks.
- Destroying a brick awards 10 points.
- Letting the ball fall below the paddle deducts 1 life (3 lives total).
- Clear all bricks to win; lose all 3 lives for Game Over.

## Instructions for Running the Game
1. Ensure Python 3 is installed (Tkinter is included by default).
2. Open a terminal in the project folder.
3. Run: `python main.py`

## Game Controls & Playing Instructions
- Press **Spacebar** to start the game.
- Press **Left Arrow (`<-`)** to move the paddle left.
- Press **Right Arrow (`->`)** to move the paddle right.

## Main Classes & Responsibilities
- **`GameObject` (`game_objects.py`):** Abstract base class storing canvas references and defining the abstract `move()` method.
- **`Paddle` (`game_objects.py`):** Controls player paddle movement within screen boundaries.
- **`Ball` (`game_objects.py`):** Handles ball velocity, wall bouncing, and resetting after a missed ball.
- **`Brick` (`game_objects.py`):** Represents breakable brick targets on the canvas.
- **`ScoreManager` (`score_manager.py`):** Safely tracks and updates the player's score and remaining lives.
- **`BrickBlitzGame` (`game.py`):** Manages the Tkinter GUI, game loop, collision detection, and win/loss states.

## Four OOP Principles Demonstrated
- **Abstraction:** `GameObject` inherits from `ABC` and uses `@abstractmethod` on `move()` to enforce a common interface without implementing movement details.
- **Inheritance:** `Paddle`, `Ball`, and `Brick` inherit shared attributes (`canvas`, `item_id`) and `get_coords()` from `GameObject`.
- **Polymorphism:** `Paddle`, `Ball`, and `Brick` each override `move()` differently—`Paddle` moves on key presses, `Ball` moves continuously, and `Brick` remains stationary.
- **Encapsulation:** `ScoreManager` protects `__score` and `__lives` as private attributes, allowing updates only through `add_points()`, `lose_life()`, `get_score()`, and `get_lives()`.

## Python Libraries Used
- `tkinter` (Graphical User Interface)
- `abc` (Abstract Base Classes)

## Group Member Contributions
- **Sochima Iloka:** Designed `GameObject`, `Paddle`, `Ball`, and `Brick` classes (`game_objects.py`), set up GitHub repository, milestone, and issues.
- **Jayden Wittock:** Implemented `BrickBlitzGame` game loop, collision detection, and GUI controls (`game.py`), and conducted gameplay testing.
- **Kenneth Ezinma:** Built `ScoreManager` with encapsulation (`score_manager.py`), entry point (`main.py`), and project documentation (`README.md`).
