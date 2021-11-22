#!/usr/bin/env python3
import sys
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7789
import os


display_type = "dhmini"

x = 0 # horizontal position on display
y = 0 # vertical position on display

if display_type == "dhmini":
    disp = ST7789.ST7789(
        height=240,
        width=320,
        rotation=180,
        port=0,
        cs=1,
        dc=9,
        backlight=13,
        spi_speed_hz=60 * 1000 * 1000,
        offset_left=0,
        offset_top=0
   )

else:
    print ("Invalid display type!")

disp.begin()
def get_display(x, y, MESSAGE):
    # Initialize display.
    #disp.begin()
    WIDTH = disp.width
    HEIGHT = disp.height
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    t_start = time.time()
    #draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
    draw.text((x, y), MESSAGE, font=font, fill=(255, 255, 255))
    draw.text((0, 20), '--START', font=font, fill=(255, 255, 255))
    draw.text((0, 200), '--RESET', font=font, fill=(255, 255, 255))
    draw.text((240, 20), 'STOP--', font=font, fill=(255, 255, 255))
    draw.text((240, 200), 'OFF--', font=font, fill=(255, 255, 255))
    disp.display(img)

