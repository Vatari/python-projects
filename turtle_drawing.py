import turtle

my_turtle = turtle.Turtle()
turtle.bgcolor("black")

my_turtle.color("cyan")
my_turtle.shape("turtle")

my_turtle.speed(10)

for i in range(36):
    my_turtle.forward(i * 10)
    my_turtle.right(144)

my_turtle.penup()
my_turtle.goto(0, -200)
my_turtle.pendown()

my_turtle.color('white')
my_turtle.write("Welcome", align="center", font=("Arial", 30, "bold"))

my_turtle.hideturtle()
turtle.exitonclick()
