from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x0 > x1):
        temp = x1
        x1 = x0
        x0 = temp
        temp = y1
        y1 = y0
        y0 = temp
    x, y = x0, y0
    a = y1 - y0 # a = change in y
    b = -(x1 - x0)# change in x
    '''print "x is: " + str(x)
    print "y is: " + str(y)
    print "a is: " + str(a)
    print "b is: " + str(b)'''

    # check if vertical line
    if (b == 0):
        if (y < y1):
            while(y <= y1):
                plot(screen, color, x, y)
                y = y + 1
        if (y > y1):
            while(y1 <= y):
                plot(screen, color, x, y)
                y = y - 1
        return

    m = float(a) / float(-b) # slope
    #print "m (slope) is: " + str(m)

    # octant 1
    if (m >= 0 and m <= 1):
    #if (a <= -b):
        d = (2 * a) + b
        while(x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y = y + 1
                d += (2 * b)
            x = x + 1
            d += (2 * a)
        plot(screen, color, x, y)
    # octant 2
    if (m > 1):
    #if (a > -b):
        d = a + (2 * b)
        while(y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x = x + 1
                d += (2 * a)
            y = y + 1
            d += (2 * b)
        plot(screen, color, x, y)
    # octant 7
    if (m < -1):
    #if (m < 0 and m >= -1):
    #if (abs(a) <= abs(-b) and ((a < 0) or (-b < 0))):
        #print "lol"
        d = a - (2 * b)
        while(y > y1):
            plot(screen, color, x, y)
            if (d > 0):
                x = x + 1
                d += (2 * a)
            y = y - 1
            d -= (2 * b)
        plot(screen, color, x, y)
    # octant 8
    if (m < 0 and m >= -1):
    #if (m < -1):
    #if (abs(a) > abs(-b) and ((a < 0) or (-b < 0))):
        #print "oof"
        d = (2 * a) - b
        while(x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y = y - 1
                d -= (2 * b)
            x = x + 1
            d += (2 * a)
        plot(screen, color, x, y)
