import board
import displayio
from adafruit_st7735 import ST7735


# SPI Setup
spi = board.SPI()
# dc = digitalio.DigitalInOut(board.D24)  # Data/Command pin
tft_dc = board.D25  # Reset pin
tft_cs = board.D8  # Chip Select

displayio.release_displays()
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D25)

display = ST7735(display_bus, width=128, height=160)

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(128, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000

bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)

while True:
    pass