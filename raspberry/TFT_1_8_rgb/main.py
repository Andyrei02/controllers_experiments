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
red_bgr565 = (31 << 11)  # Still using red in place of blue
bitmap[10, 10] = red_bgr565

# Fill screen using BGR565
for y in range(128):
    for x in range(160):
        bitmap[x, y] = red_bgr565

display.show(bitmap)
while True:
    pass
