import board
import displayio
import digitalio
from adafruit_st7735r import ST7735R  # Make sure you use the correct driver!

# Release previous displays
displayio.release_displays()

# SPI Setup
spi = board.SPI()
tft_dc = digitalio.DigitalInOut(board.D24)  # Data/Command
tft_cs = digitalio.DigitalInOut(board.CE0)  # Chip Select
tft_rst = digitalio.DigitalInOut(board.D25)  # Reset

# Set as output
tft_dc.switch_to_output()
tft_cs.switch_to_output()
tft_rst.switch_to_output()

# Create display bus
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

# Initialize Display
display = ST7735R(display_bus, width=128, height=160, rotation=90)  # Rotation 90 if needed

# Create Display Context
splash = displayio.Group()
display.root_group = splash

# Set Background Color
color_bitmap = displayio.Bitmap(128, 160, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000  # Red Background

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

print("Displaying Red Background")

while True:
    pass
