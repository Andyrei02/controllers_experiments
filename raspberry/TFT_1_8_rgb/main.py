import board
import displayio
import digitalio
from adafruit_st7735r import ST7735R
from adafruit_display_shapes.rect import Rect

# Release previous displays (important if restarting)
displayio.release_displays()

# SPI Setup
spi = board.SPI()  # Default SPI pins
tft_dc = board.D24  # Data/Command pin
tft_cs = board.CE0  # Chip Select
tft_rst = board.D25  # Reset pin

# Create display bus
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

# Initialize Display (160x128 resolution, adjust for your display)
display = ST7735R(display_bus, width=160, height=128)

# **STEP 1: TEST PURE RED USING RGB565**
# **Use BGR565 (Blue instead of Red)**
red_bgr565 = 0x001F  # This is red in BGR565
red_rect = Rect(0, 0, 160, 128, fill=red_bgr565)
group = displayio.Group()
group.append(red_rect)
display.root_group = group


# **Keep the display running**
while True:
    pass
