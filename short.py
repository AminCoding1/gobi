import turtle as tu

roo = tu.Turtle()
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Fractal Tree Pattern")
roo.left(90)
roo.speed(2000)


def draw(l, pensize, pencolor):
    if l < 10:
        return
    else:
        roo.pensize(pensize)
        roo.pencolor(pencolor)
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4, pensize, pencolor)
        roo.right(60)
        draw(3 * l / 4, pensize, pencolor)
        roo.left(30)
        roo.pensize(pensize)
        roo.backward(l)


# Yellow pattern
draw(20, 2, "yellow")

# Magenta pattern
roo.right(90)
draw(20, 2, "magenta")

# Red pattern
roo.left(270)
draw(20, 2, "red")

# White pattern
roo.right(90)
draw(20, 2, '#FFF8DC')

# Lightgreen pattern
draw(40, 3, "lightgreen")

# Red pattern
roo.right(90)
draw(40, 3, "red")

# Yellow pattern
roo.left(270)
draw(40, 3, "yellow")

# White pattern
roo.right(90)
draw(40, 3, '#FFF8DC')

# Cyan pattern
draw(60, 2, "cyan")

# Yellow pattern
roo.right(90)
draw(60, 2, "yellow")

# Magenta pattern
roo.left(270)
draw(60, 2, "magenta")

# White pattern
roo.right(90)
draw(60, 2, '#FFF8DC')

wn.exitonclick()
