import turtle

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order-1, size/3)
            turtle.left(angle)

# Create a turtle screen and set properties
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Koch Snowflake")

# Create a turtle for drawing
snowflake = turtle.Turtle()
snowflake.penup()
snowflake.goto(-150, 90)
snowflake.pendown()
snowflake.speed(0)  # Fastest drawing speed

# Draw the Koch Snowflake with 4 iterations
for _ in range(3):
    koch_snowflake(snowflake, 4, 300)
    snowflake.right(120)

# Close the turtle graphics window on click
screen.exitonclick()
