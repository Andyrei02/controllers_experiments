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




# Create an image with Pillow
image = Image.new("RGB", (160, 128), (255, 0, 0))  # Red background (RGB format)
draw = ImageDraw.Draw(image)

# Optionally, draw text or additional shapes here
# draw.text((10, 10), "Hello", fill="white")

# Convert the Pillow image to a format compatible with displayio
bitmap = displayio.Bitmap(160, 128, 65536)  # 16-bit color depth
for y in range(128):
    for x in range(160):
        r, g, b = image.getpixel((x, y))
        # Convert RGB to 5-6-5 16-bit format (RGB565)
        color = ((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3)
        bitmap[x, y] = color

# Create a palette for the 16-bit colors
palette = displayio.Palette(1)
palette[0] = 0xFF0000  # Red in RGB565 format

# Create a TileGrid to display the bitmap
tilegrid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Append the tilegrid to the splash group to display it
splash.append(tilegrid)

print("Displaying Red Background")

while True:
    pass
