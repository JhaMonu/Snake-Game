import turtle
from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
screen.listen()
food = Food()
score = Scoreboard()

screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")


game_is_on = True
while game_is_on:
    if (snake.new_square[0]. xcor() >280 or snake.new_square[0]. xcor()<-280 or snake.new_square[0]. ycor() >280
            or snake.new_square[0]. ycor() < -280):


        game_is_on = False
        turtle.color("White")
        turtle.hideturtle()
        turtle.write(f"Game over ",  align="center",font=("Arial",20,"normal"))

    # if (snake.new_square[0]==)


    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.new_square[0].distance(food) < 15:
        food.food_refesh()
        score.increse_score()
        snake.exend_snake()


    for square in snake.new_square[1:]:
        if snake.new_square[0].distance(square)<10:
            game_is_on = False
            turtle.color("white")
            turtle.write(f"Game over ", align="center", font=("Arial", 20, "normal"))

screen.exitonclick()