import turtle

def draw_fractal(length, depth):
    if depth == 1:
        jonney.forward(length)
    else:
        draw_fractal(length, depth-1)
    jonney.right(60)
    if depth == 1:
        jonney.forward(length)
    else:
        draw_fractal(length, depth-1)
    jonney.left(120)
    if depth == 1:
        jonney.forward(length)
    else:
        draw_fractal(length, depth-1)
    jonney.right(60)
    if depth == 1:
        jonney.forward(length)
    else:
        draw_fractal(length, depth-1)



def draw_snowflake(length, depth):
    draw_fractal(length, depth-1)
    jonney.left(120)
    draw_fractal(length, depth-1)
    jonney.left(120)
    draw_fractal(length, depth-1)

jonney = turtle.Turtle()
jonney.penup()
jonney.goto(-200,0)
jonney.pendown()
draw_snowflake(5,5)
turtle.exitonclick()
