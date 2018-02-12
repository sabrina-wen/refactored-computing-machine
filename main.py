from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

y = 480
while(y >= 0):
    draw_line(0, y, 500, y, screen, color)
    y = y - 20

x = 0
while(x <= 500):
    draw_line(x, 0, x, 500, screen, color)
    x = x + 20

color = [ 255, 255, 0 ]
draw_line(220, 220, 300, 300, screen, color)
draw_line(380, 220, 300, 300, screen, color)
draw_line(220, 220, 380, 220, screen, color)
display(screen)
save_extension(screen, 'img.png')