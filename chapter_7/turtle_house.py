import turtle
santa = turtle.Turtle()
wn = turtle.Screen()

def house(side,turt):
    diag = (side**2 * 2 )**.5
    roof = (side**2/2)**.5
    path = [(45,diag),(90,roof),(90,roof),(45,side),(90,side),(90,side),(90,side),(135,diag)]

    for angle, dist in path:
        santa.left(angle)
        santa.forward(dist)
        
house(500,santa)