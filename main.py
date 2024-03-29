from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Sneaky Snake")
screen.tracer(0)

line = Turtle()
line.penup()
line.color("white")
line.goto(-305, 269)
line.pendown()
line.goto(305, 269)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 277 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

    # if head collides with any segment in the tail:

screen.exitonclick()
