from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
'''XRES = 500
YRES = 500

draw_line(0, 0, XRES-1, YRES-1, screen, color);
draw_line(0, 0, XRES-1, YRES / 2, screen, color);
draw_line(XRES-1, YRES-1, 0, YRES / 2, screen, color);

color[2] = 255;
draw_line(0, YRES-1, XRES-1, 0, screen, color);
draw_line(0, YRES-1, 500, YRES/2, screen, color);
draw_line(XRES-1, 0, 0, YRES/2, screen, color);

color[0] = 255;
color[1] = 0;
color[2] = 0;
draw_line(0, 0, XRES/2, YRES-1, screen, color);
draw_line(XRES-1, YRES-1, XRES/2, 0, screen, color);

color[2]= 255;
draw_line(0, YRES-1, XRES/2, 0, screen, color);
draw_line(XRES-1, 0, XRES/2, YRES-1, screen, color);

color[2] = 0;
color[1] = 255;
draw_line(0, YRES/2, XRES-1, YRES/2, screen, color);
draw_line(XRES/2, 0, XRES/2, YRES-1, screen, color);'''

y = 480
while(y >= 0):
    draw_line(0, y, 500, y, screen, color)
    y = y - 20

x = 0
while(x <= 500):
    draw_line(x, 0, x, 500, screen, color)
    x = x + 20

color = [ 255, 255, 0 ]
draw_line(0, 0, 500, 500, screen, color)
draw_line(0, 500, 500, 0, screen, color)
display(screen)
save_extension(screen, 'img.png')
