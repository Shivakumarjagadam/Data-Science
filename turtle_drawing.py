import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Drawing")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("green")

# Define the turtle shape
def draw_turtle():
    t.penup()
    t.goto(0, -50)
    t.pendown()
    
    # Draw the body
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
    # Draw the head
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    # Draw the legs
    positions = [(-50, -50), (50, -50), (-50, 50), (50, 50)]
    for pos in positions:
        t.penup()
        t.goto(pos)
        t.pendown()
        t.begin_fill()
        t.circle(20)
        t.end_fill()

# Draw the turtle
draw_turtle()

# Hide the turtle and finish
t.hideturtle()
turtle.done()
