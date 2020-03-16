import turtle
turtle.setup(950,350,200,200)#窗口大小
turtle.penup()
turtle.fd(-250)#起始坐标
turtle.pendown()
turtle.pensize(10)#粗细
turtle.pencolor("blue")#颜色
turtle.seth(-40)#运动方向
for i in range(4):#sin函数周期
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(400)
turtle.circle(70,300)
turtle.fd(40*2/3)
turtle.done()