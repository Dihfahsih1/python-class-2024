import time

print("time is: %s" % time.ctime())

from turtle import*
import colorsys
bgcolor("black")
tracer (200)

def draw():
    h = 0
    for i in range(100):
        c=colorsys.hsv_to_rgb(h,1,1)
        h +=0.55
        up()
        goto(0,0)
        down()
        color("black")
        fillcolor (c)
        begin_fill()
        rt (200)
        circle(i, 2)
        fd (90)
        fd (i)
        lt(29)
        for j in range(19):
            fd(i)
            circle(j, 299, steps=11)
        end_fill()
draw()
done()


