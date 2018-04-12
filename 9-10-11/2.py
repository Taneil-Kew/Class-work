
"""2. Change the traffic light program so that changes occur automatically, driven by a timer."""
import turtle

wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
yay = turtle.Turtle()
bob = turtle.Turtle()
guest = turtle.Turtle()
hunt = turtle.Turtle()




def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

def draw_housing2():
    """ Draw a nice housing to hold the traffic lights """
    yay.pensize(3)
    yay.color("black", "darkgrey")
    yay.penup()
    yay.backward(180)
    yay.pendown()
    yay.begin_fill()
    yay.forward(80)
    yay.left(90)
    yay.forward(275)
    yay.circle(40, 180)
    yay.forward(275)
    yay.left(90)
    yay.end_fill()


draw_housing()
draw_housing2()

tess.penup()

tess.forward(40)
tess.left(90)
tess.forward(50)

tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
yay.penup()
yay.forward(40)
yay.left(90)
yay.forward(50)
yay.shape("circle")
yay.shapesize(3)
yay.fillcolor("gray")

bob.penup()
bob.goto(yay.position()[0], (yay.position()[1] + 75))
bob.shape('circle')
bob.shapesize(3)
bob.fillcolor("gray")

guest.penup()
guest.goto(bob.position()[0], (bob.position()[1] + 75))
guest.shape('circle')
guest.shapesize(3)
guest.fillcolor('gray')

hunt.penup()
hunt.goto(guest.position()[0], (guest.position()[1] + 75))
hunt.shape('circle')
hunt.shapesize(3)
hunt.fillcolor('gray')


state_num = 0
state_num_1 = 0


def timer():
    global state_num
    if state_num == 0:
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
    wn.ontimer(timer, "10000")


def timer2():
    global state_num_1
    if state_num_1 == 0:
        guest.fillcolor('gray')
        yay.fillcolor('green')
        state_num_1 = 1
    elif state_num_1 == 1:
        yay.fillcolor('gray')
        bob.fillcolor('green')
        hunt.fillcolor('orange')
        state_num_1 = 2
    elif state_num_1 == 2:
        bob.fillcolor('gray')
        hunt.fillcolor('gray')
        guest.fillcolor('red')
        state_num_1 = 0
    wn.ontimer(timer2, "10000")


timer()
timer2()

wn.mainloop()