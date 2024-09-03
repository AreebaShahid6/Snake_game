from turtle import Screen
from snake import Snake
from food import Food    
from scoreboard import Score  
import time
#screen
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)     # Add a delay for smooth movement
    snake.move() # Movement of snake
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()  #extension of snake
        score.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]: #using slice it can skip the head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
my_screen.exitonclick()

