import turtle

def make_square(irving):
    length = int(input('Size of square:'))

    for i in range(4):
         make_line_and_turn(irving, length)


def make_line_and_turn(irving, length):
    irving.forward(length)
    irving.left(90)


window = turtle.Screen()
irving = turtle.Turtle()
make_square(irving)
turtle.mainloop()


