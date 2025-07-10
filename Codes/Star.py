import turtle
colors =('yellow','white','green','pink','orange','yellow')
turtle.bgcolor('black')
turtle.speed(111)
for i in range(200):
    turtle.color(colors[i%6])
    turtle.forward(i*4)
    turtle.left(150)
    turtle.width(2)
