import turtle
santa = turtle.Turtle()
wn = turtle.Screen()

s = 100
r = (s**2/2)**.5
d = (2 * s**2)**.5

path = [(90,s),(-45,r),(-90,r),(-45,s),(-135,d),(-135,s),(-135,d),(135,s)]

for angle,dist in path:
    santa.left(angle)
    santa.fd(dist)
       
    