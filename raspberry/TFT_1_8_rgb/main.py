import board
import displayio
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
display = ST7735R(display_bus, width=160, height=128)

# Create display group
group = displayio.Group()

# Test different colors (in 565 format)
# Red should be 0xF800 in RGB565
# Green should be 0x07E0 in RGB565
# Blue should be 0x001F in RGB565

red_rect = displayio.Rect(0, 0, 160, 42, fill=0xF800)  # Expected Red (RGB565)
green_rect = displayio.Rect(0, 42, 160, 42, fill=0x07E0)  # Expected Green (RGB565)
blue_rect = displayio.Rect(0, 84, 160, 42, fill=0x001F)  # Expected Blue (RGB565)

group.append(red_rect)
group.append(green_rect)
group.append(blue_rect)

display.root_group = group  # Send to display

while True:
    pass  # Keep running
