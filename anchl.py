# print('hello world')
# array = [1,2,3,4,5,6,7,'hello',0,8765]
# array.append('Anchl')
# print(array)
# array = [1,2,3,4,5,6,7,'hello',0,8765]
# array.append("Anchl")
# print(array)
# array = [1,2,3,4,'hello',9987]
# b = array
# print(b.append('world'))
# print(array)
# array = [1,2,3,4,'hello',9987]
# b = array
# print(b.copy())
# print(array)
# array =[1,2,3,4,5,56,'hey',0]
# (array.remove(5))
# print(array)
# array =[1,2,3,4,5,56,'hey',0]
# (array.pop(4))
# print(array)
# 1.code

# from turtle import *
# import colorsys
# bgcolor('black')
# tracer (500)
# def draw():
#     h = 0
#     for i in range(100):
#         c = colorsys.hsv_to_rgb(h,1,1)
#         h += 0.5
#         up()
#         goto(0,0)
#         down()
#         color('black')
#         fillcolor (c)
#         begin_fill()
#         rt (98)
#         circle(i, 12)
#         fd (290)
#         fd(i)
#         lt (29)
#         for j in range(129):
#             fd(i)
#             circle(j, 299, steps=2)
#             end_fill()
# draw()
# done()
#  
# 2.code

# import math 
# from turtle import *
# def hearta(k):
#     return 15*math.sin(k)**3
# def heartb(k):
#     return 12*math.cos(k)-5*\
#            math.cos(2*k)-2*\
#            math.cos(3*k)-\
#            math.cos(4*k)
# speed(60000)
# bgcolor("black")
# for i in range(600):
#     goto(hearta(i)*20,heartb(i)*20)
#     for j in range(5):
#         color("#f73487")
#         goto(0,0)
# done()  
#    
# code 3

# import turtle as t
# t.speed (0)
# t.bgcolor('purple')
# t.hideturtle()
# for i in range(300):
#     t.circle(i - 5)
#     t.left(5)
#     t.done
# 
# code 4

# import turtle as t
# t.speed(0)
# t.bgcolor('black')
# t.pencolor('orange')
# def square(x, y):
#     for j in range(4):
#         t.forward(x)
#         t.right(y)
# for i in range(80):
#     square(170,90)
#     t.right(5)
#     t.circle(50)
#     t.right(50)
#     t.hideturtle()
# t.done()

# code 5

# from turtle import*
# speed(0)
# bgcolor('black')
# colors = ['orange','white']
# hideturtle()
# for i in range(122):
#     goto(0, 0)
#     color(colors[i % 2])
#     forward(130)
#     left(3)
#     circle(40)
#     forward(130)
#     right(180)
# done()

# from turtle import*
# import colorsys
# speed(0)
# bgcolor('black')
# h = 0
# for i in range(16):
#     for j in range(18):
#     c = colorsys.hsv_to_rgb(h, 1, 1)
#     color(c)
#     h += 0.005
#     rt(90)
#     circle(150 - j * 6, 90)
#     lt(90)
#     circle(150 - j * 6, 90)
#     rt(180)
# circle(40,24)
# done()


