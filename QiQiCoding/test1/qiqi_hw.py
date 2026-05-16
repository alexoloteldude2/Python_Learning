from turtle import *
for i in range(0,6):
    seth(144*i)
    fd(100)
    fillcolor("blue")
    begin_fill()
    circle(10)
    end_fill()
done()