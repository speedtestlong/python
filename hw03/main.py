import turtle as t

#初始化
t.hideturtle()
t.speed(10)

#画五角星的函数

def start(x,y,r,f):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.right(r)
    t.color('yellow','yellow')
    t.begin_fill()
    for i in range (5):
        t.forward(f)
        t.right(144)
    t.end_fill()

#画旗面的函数

def rectangle(x,y,c,k):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color('red','red')
    t.begin_fill()
    for i in range(1):
        t.forward(c)
        t.right(90)
        t.forward(k)
        t.right(90)
        t.forward(c)
        t.right(90)
        t.forward(k)
    t.end_fill()

rectangle(-300,200,600,400)
start(-200,160,162,114)
start(-120,151,240,38)
start(-78.125,114.5,20,38)
start(-78.125,62.5,25,38)
start(-119.8,36.5,25,38)
