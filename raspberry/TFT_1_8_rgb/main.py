import board
import displayio
import digitalio
from adafruit_st7735 import ST7735  # Make sure you use the correct driver!

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
display = ST7735(display_bus, width=160, height=128)  # Rotation 90 if needed

# Create Display Context
splash = displayio.Group()
# Set the root group for the display
display.root_group = splash

# Set Background Color
color_bitmap = displayio.Bitmap(160, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000  # Red Background

# Fill the bitmap with the color index
for y in range(128):
    for x in range(160):
        color_bitmap[x, y] = 0  # Use the index 0, which corresponds to red in the palette

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Clear the display before starting the loop
display.refresh()

print("Displaying Red Background")

while True:
    pass
