import board
import displayio
import digitalio
from adafruit_st7735r import ST7735R  # Make sure you use the correct driver!

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

# Create a solid red color fill directly on the display
fill_color = 0xFF0000  # Red color

# Fill the display with the red color
display.fill(fill_color)

print("Displaying Red Background")

while True:
    pass
