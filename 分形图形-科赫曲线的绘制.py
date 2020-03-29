import turtle as t

def koch( size, n ):
    # size= the size of the original line
    # n = the order
    if n == 0 :
        t.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            t.left(angle)
            koch(size/3, n-1)

def main():
    t.setup( 1024, 800 )
    t.penup()
    t.pensize( 5 )
    t.goto( -200 , 100)
    t.pendown()
    t.pencolor('black')

    level = 3
    koch(400, level)
    t.right(120)
    koch(400, level)
    t.right(120)
    koch(400,level)

    t.hideturtle()
    t.done()


main()