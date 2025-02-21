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

from adafruit_display_shapes.rect import Rect

group = displayio.Group()
red_rect = Rect(0, 0, 160, 128, fill=0xF800)  # Red in RGB565
group.append(red_rect)
display.show(group)

while True:
    pass  # Keep showing the image
