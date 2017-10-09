import turtle as t

#初始化

t.hideturtle()
t.speed(10)

#红旗旗面

t.penup()

t.goto(-300,200)

t.pendown()

t.color('red','red')

t.begin_fill()
t.forward(600)
t.right(90)
t.forward(400)
t.right(90)
t.forward(600)
t.right(90)
t.forward(400)
t.end_fill()

#第一颗星

t.penup()

t.goto(-200,160)

t.pendown()

t.right(162)
t.color('yellow','yellow')
t.begin_fill()
for i in range(5):
    t.forward(114)
    t.right(144)
t.end_fill()

#第二颗星

t.penup()

t.goto(-120,151)

t.pendown()

t.left(120)

t.begin_fill()
for i in range(5):
    t.forward(38)
    t.right(144)
t.end_fill()

#第三颗星

t.penup()

t.goto(-78.125,114.5)

t.pendown()

t.right(20)

t.begin_fill()
for i in range(5):
    t.forward(38)
    t.right(144)

t.end_fill()

#第四颗星

t.penup()

t.goto(-78.125,62.5)

t.pendown()

t.right(25)

t.begin_fill()
for i in range(5):
    t.forward(38)
    t.right(144)

t.end_fill()

#第五颗星

t.penup()

t.goto(-119.8,36.5)

t.pendown()

t.right(25)

t.begin_fill()
for i in range(5):
    t.forward(38)
    t.right(144)

t.end_fill()
