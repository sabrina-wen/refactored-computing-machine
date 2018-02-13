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

    if (b > 0):
        draw_line(x0, y0, x1, y1, screen, color)
    # octant 1
    if (a <= -b):
        d = (2 * a) + b
        while(x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y = y + 1
                d += (2 * b)
            x = x + 1
            d += (2 * a)
    # octant 2
    if (a > -b):
        d = a + (2 * b)
        while(y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x = x + 1
                d += (2 * a)
            y = y + 1
            d += (2 * b)
    # octant 7
    if (a <= b ):
        d = a - (2 * b)
        while(y < y1):
            plot(screen, color, x, y)
            if (d > 0):
                x = x + 1
                d += (2 * a)
            y = y - 1
            d -= (2 * b)
    # octant 8
    if (a >= b and a < 0):
        d = (2 * a) + b
        while(x < x1):
            plot(screen, color, x, y)
            if (d < 0):
                y = y - 1
                d -= (2 * b)
            x = x + 1
            d += (2 * a)
