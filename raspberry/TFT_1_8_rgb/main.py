import time
import board
import digitalio
import adafruit_st7735
from PIL import Image, ImageDraw, ImageFont

# Setup SPI interface
spi = board.SPI()  # Hardware SPI
cs = digitalio.DigitalInOut(board.CE0)  # Chip Select
dc = digitalio.DigitalInOut(board.D24)  # Data/Command
rst = digitalio.DigitalInOut(board.D25)  # Reset

# Initialize Display
disp = adafruit_st7735.ST7735(spi, cs=cs, dc=dc, rst=rst, width=128, height=160)

# Create a blank image
image = Image.new("RGB", (128, 160), "black")
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 18)

# Display text
draw.text((10, 60), "Hello, Pi!", font=font, fill="white")

# Show image on display
disp.image(image)

# Keep the text on screen
time.sleep(10)
