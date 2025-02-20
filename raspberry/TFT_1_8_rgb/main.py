import board
import displayio
import digitalio
from adafruit_st7735r import ST7735R
from PIL import Image, ImageDraw


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




# Create a bitmap for a red background (RGB565)
color_bitmap = displayio.Bitmap(160, 128, 65536)  # 16-bit color depth

# Fill the bitmap with red color in RGB565
red_color = (31 << 11) | (0 << 5) | (0)  # Red in RGB565 (5 bits for Red, 6 for Green, 5 for Blue)

for y in range(128):
    for x in range(160):
        color_bitmap[x, y] = red_color

# Create a TileGrid from the bitmap and add it to the splash group
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=None)
splash.append(bg_sprite)


print("Displaying Red Background")

while True:
    pass
