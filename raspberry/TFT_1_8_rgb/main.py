import time
import board
import digitalio
import adafruit_st7735

# SPI Setup
spi = board.SPI()
dc = digitalio.DigitalInOut(board.D24)  # Data/Command pin
rst = digitalio.DigitalInOut(board.D25)  # Reset pin
cs = digitalio.DigitalInOut(board.CE0)  # Chip Select

# Set pin directions
dc.direction = digitalio.Direction.OUTPUT
rst.direction = digitalio.Direction.OUTPUT
cs.direction = digitalio.Direction.OUTPUT

# Initialize display
disp = adafruit_st7735.ST7735(spi, rst=rst)

# Clear screen (black)
disp.fill(0)

# Display text
from adafruit_display_text import label
import terminalio

text_area = label.Label(terminalio.FONT, text="Hello, World!", color=0xFFFF, x=10, y=10)
disp.show(text_area)

time.sleep(5)  # Keep text visible for 5 seconds
