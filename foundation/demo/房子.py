import turtle
# 前置
p = turtle.Pen()
# 作者要说的话
for i in range(6):
    print('请把画板最大化，否则会影响画面效果！')
# 设置笔的速度
p.speed(10)
# 开始画画
p.pencolor("#F4A460")
p.penup()
p.goto((-240), (-200))
p.pendown()
p.begin_fill()
p.fillcolor("#F4A460")
p.goto(240, (-200))
p.left(90)
p.goto(240, 50)
p.left(90)
p.goto((-240), 50)
p.left(90)
p.goto((-240), (-200))
p.penup()
p.goto((-200), 10)
p.end_fill()
p.pendown()
# 开始画窗户
p.pencolor("#000000")
p.begin_fill()
p.fillcolor("#FFFFFF")
for i in range(4):
    p.forward(60)
    p.left(90)
p.end_fill()
p.penup()
p.forward(30)
p.left(90)
p.pendown()
p.forward(60)
p.penup()
for i in range(2):
    p.left(90)
    p.forward(30)
p.left(90)
p.pendown()
p.forward(60)
p.penup()
# 开始画门
p.pencolor("#FFFFFF")
p.goto(60, (-200))
p.begin_fill()
p.pendown()
p.right(180)
p.pendown()
p.forward(150)
p.right(90)
p.forward(75)
p.right(90)
p.forward(150)
p.fillcolor("#FFFFFF")
p.end_fill()
# 画门把手
p.right(180)
p.forward(75)
p.penup()
p.left(90)
p.forward(10)
p.pendown()
# 画圆
p.begin_fill()
p.fillcolor("#000000")
p.circle(10)
p.end_fill()
p.penup()
# 开始画屋顶
p.goto((-240), 50)
p.pendown()
p.setheading(45)
p.pencolor("#808080")
p.begin_fill()
p.fillcolor("#808080")
p.forward(341)
p.right(90)
p.forward(341)
p.end_fill()

# 停止画面
turtle.done()