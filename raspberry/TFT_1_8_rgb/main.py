import time
import board
import displayio
import digitalio
from adafruit_st7735r import ST7735R
from adafruit_display_text.bitmap_font import BitmapFont  # Correct import
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect


# Release previous displays
displayio.release_displays()

# SPI Setup
spi = board.SPI()
tft_dc = board.D24  # Data/Command
tft_cs = board.CE0  # Chip Select
tft_rst = board.D25  # Reset

# Create display bus
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

# Initialize Display
display = ST7735R(display_bus, width=160, height=128, rotation=90)  # Rotation 90 if needed
# Create Display Context
splash = displayio.Group()
# Set the root group for the display
display.root_group = splash




# Set a background color
color_bitmap = displayio.Bitmap(160, 128, 65536)
red_color = (31 << 11) | (0 << 5) | (0)  # Red in RGB565
for y in range(128):
    for x in range(160):
        color_bitmap[x, y] = red_color

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=None)
splash.append(bg_sprite)

# Load the default font from the library
font = BitmapFont("/usr/local/lib/python3.11/site-packages/adafruit_display_text/font/arial14.bdf")  # Adjust the path accordingly

# Create a label with the text
text_area = label.Label(font, text="Hello, World!")
text_area.y = 50  # Start position

# Add the label to the display group
splash.append(text_area)

# Animation loop (moving text across the screen)
while True:
    for x in range(160):
        text_area.x = x
        time.sleep(0.02)  # Adjust speed by changing the sleep duration
        

print("Displaying Red Background")

while True:
    pass
