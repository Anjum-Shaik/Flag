import turtle
s=turtle.screen()
f=turtle.Turtle()
f.penup()
f.goto(-180,60)
#for filling orange color
f.pendown()
f.begin_fill()
f.fillcolor("orange")
f.left(90)
f.forward(90)
f.right(90)
f.forward(400)
f.right(90)
f.forward(90)
f.right(90)
f.forward(400)
f.end_fill()

#for white
f.left(90)
f.forward(90)
f.left(90)
f.forward(400)
f,left(90)
f.forward(90)
f.left(90)
f.forward(400)
f.left(90)
f.forward(90)

#for green color

f.begin_fill()
f.fillcolor("green")
f.forward(90)
f.left(90)
f.forward(400)
f.left(90)
f.forward(90)
f.left(90)
f.forward(400)
f.end_fill()

#for ashoka chakra it fills blue color

f.penup()
f.goto(23,32)
f.pendown()
f.begin_fill()
f.fillcolor("blue")
f.circle(20)
f.end_fill()
#this is must to hold the screen
turtle.done()


