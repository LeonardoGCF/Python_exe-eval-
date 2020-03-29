import turtle as t
import time

def drawGap():
    t.penup()
    t.fd(5)

def drawLine(draw):
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)

def drawDigits(digit):
    drawLine( True ) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine( False )
    drawLine( True ) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine( False )
    drawLine( True ) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine( False )
    drawLine( True ) if digit in [0, 2, 6, 8] else drawLine( False )

    t.left(90)

    drawLine( True ) if digit in [0, 4, 5, 6, 8, 9] else drawLine( False )
    drawLine( True ) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine( False )
    drawLine( True ) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine( False )

    t.left(180)
    t.penup()
    t.fd(20)

def drawDate (date):#Date 格式为 "%Y-%m=%d+"
    for i in date:
        if i == '-':
            t.pencolor( 'black' )
            t.write('年',font =("Arial",30, "normal") )
            t.penup()
            t.fd(40)
        elif i == '=':
            t.pencolor( 'black' )
            t.write('月',font =("Arial",30, "normal") )
            t.penup()
            t.fd(40)
        elif i == '+':
            t.pencolor( 'black' )
            t.write('日',font =("Arial",30, "normal") )

        else:
            t.pencolor( 'green' )
            drawDigits(eval(i))

#test
def drawNum(Num):
    for i in Num:
        drawDigits(eval(i))

def main():

    t.setup(1024, 800)
    t.penup()
    t.pensize(5)
    t.fd(-400)


    drawDate(time.strftime("%Y-%m=%d+", time.gmtime()))
    #drawNum('1234567890')

    t.hideturtle()
    t.done()

main()