import time
import board
import digitalio
import adafruit_st7735

# SPI Setup
spi = board.SPI()  # Default SPI
dc = digitalio.DigitalInOut(board.D24)  # Data/Command pin
rst = digitalio.DigitalInOut(board.D25)  # Reset pin
cs = digitalio.DigitalInOut(board.CE0)  # Chip Select

# Initialize display
disp = adafruit_st7735.ST7735(spi, dc=dc, rst=rst, width=128, height=160)

# Clear screen with black
disp.fill(0)

# Display text
from adafruit_display_text import label
import terminalio
from adafruit_display_shapes.rect import Rect

text_area = label.Label(terminalio.FONT, text="Hello, World!", color=0xFFFF, x=10, y=10)
disp.show(text_area)

time.sleep(5)  # Keep text visible for 5 seconds
