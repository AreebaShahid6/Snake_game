# Snake_game
<img width="447" alt="snake" src="https://github.com/user-attachments/assets/88f81ea6-6c9e-44f8-8709-b5ab4149a9e3">

### Description
- **Overview**: A classic Snake game implemented using Python's `turtle` graphics library. The game features a controllable snake that grows when it consumes food and ends if it collides with the wall or its own tail.
- **Features**:
  - **Movement**: Control the snake using arrow keys (Up, Down, Left, Right).
  - **Food Consumption**: The snake grows longer and the score increases each time it eats the food.
  - **Collision Detection**:
    - Ends the game if the snake hits the wall.
    - Ends the game if the snake collides with its own tail.
  - **Score Tracking**: Displays the current score and a "Game Over" message when the game ends.

### Libraries Used
- **turtle**: For graphics and game functionality.
  - Provides the drawing and movement capabilities used in the game.
- **time**: For adding delays to control the game's speed.
  - Used to create a smooth movement of the snake by controlling the update rate.

### How to Run
1. **Ensure you have Python installed**: This project requires Python to run.
2. **Install the necessary libraries**:
   - This project uses built-in libraries (`turtle` and `time`), so no additional installation is needed.
3. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Snake-Game.git
   ```
4. **Navigate to the project directory**:
   ```bash
   cd Snake-Game
   ```
5. **Run the game**:
   ```bash
   python main.py
   ```

### Files Included
- **`main.py`**: The main script that sets up the game window, initializes the game components, and runs the game loop.
- **`snake.py`**: Defines the `Snake` class with methods for movement and growth.
- **`food.py`**: Defines the `Food` class with methods for food placement and refreshing.
- **`scoreboard.py`**: Defines the `Score` class with methods for updating and displaying the score.

### Contribution
Feel free to contribute to this project by submitting issues or pull requests. Suggestions and improvements are welcome!
