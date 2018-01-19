import turtle
import random
myturt = turtle.Turtle()
wn = turtle.Screen()

myturt.shape("square")
myturt.penup()
tfood_id = []
tfood_coord=[]
for i in range(random.randint(11,36)):
    food = (random.randint(-300,300),random.randint(-300,300))
    myturt.setpos(food[0],food[1])
    this_stamp = myturt.stamp()
    tfood_coord.append((food[0],food[1]))
    tfood_id.append(this_stamp)

               
count = 0               
for i in tfood_id:
    print(tfood_coord[count])
    myturt.clearstamp(tfood_id[count])
    count += 1



myturt.setpos(0,0)
myturt.pendown()
myturt.shape("arrow")