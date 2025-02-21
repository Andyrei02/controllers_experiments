import board
import displayio
import digitalio
from adafruit_st7735r import ST7735R

# Release previous displays
displayio.release_displays()

# SPI Setup
spi = board.SPI()
tft_dc = board.D24
tft_cs = board.CE0
tft_rst = board.D25

# Create display bus
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

# Initialize Display
display = ST7735R(display_bus, width=160, height=128)

# Create a Bitmap and Color Test
bitmap = displayio.Bitmap(160, 128, 65536)  # RGB565 max colors

# Manually set a pure red pixel at (10,10)
red_rgb565 = (31 << 11)  # Pure red in RGB565
bitmap[10, 10] = red_rgb565  

# Fill entire screen with red
for y in range(128):
    for x in range(160):
        bitmap[x, y] = red_rgb565  # Fill entire screen with red

# Create TileGrid to display the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=displayio.ColorConverter(input_colorspace=displayio.Colorspace.RGB565))
group = displayio.Group()
group.append(tile_grid)
display.root_group = group

while True:
    pass  # Keep showing the image
