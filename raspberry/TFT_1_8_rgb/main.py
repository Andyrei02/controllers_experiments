import board
import displayio
import digitalio
from adafruit_st7735r import ST7735R
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
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

# Load the font
font = bitmap_font.load_font("/lib/font/arial.bdf")  # Change the path to your font file

# Create a label with the text you want to display
text_area = label.Label(font, text="Hello, World!")
text_area.x = 20  # X position
text_area.y = 50  # Y position

# Add the label to the display group
splash.append(text_area)


print("Displaying Red Background")

while True:
    pass
