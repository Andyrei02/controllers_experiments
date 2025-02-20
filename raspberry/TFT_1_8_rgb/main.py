import time
import board
import displayio
import digitalio
from adafruit_st7735r import ST7735R
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
import terminalio
import sys


class TFT_Display:
    def __init__(self, width=161, height=130, rotation=90, text="Hello, World!", speed=0.05):
        # Release any previous displays
        displayio.release_displays()

        # SPI setup
        self.spi = board.SPI()
        self.tft_dc = board.D24  # Data/Command pin
        self.tft_cs = board.CE0  # Chip Select pin
        self.tft_rst = board.D25  # Reset pin

        self.width = width
        self.height = height
        self.text = text
        self.speed = speed

        # Create display bus
        self.display_bus = displayio.FourWire(self.spi, command=self.tft_dc, chip_select=self.tft_cs, reset=self.tft_rst)

        # Initialize Display
        self.display = ST7735R(self.display_bus, width=self.width, height=self.height, rotation=rotation)
        
        # Create Display Context
        self.splash = displayio.Group()
        self.display.root_group = self.splash

        # Set the background color (Red in RGB565)
        self.set_background_color()

        # Create a label with text
        self.text_area = label.Label(terminalio.FONT, text=self.text)
        self.text_area.x = 10  # Set initial X position
        self.text_area.y = 10  # Set initial Y position
        self.splash.append(self.text_area)

    def set_background_color(self):
        # Set a red background color
        color_bitmap = displayio.Bitmap(self.width, self.height, 65536)
        red_color = (31 << 11) | (0 << 5) | (0)  # Red in RGB565
        for y in range(self.height):
            for x in range(self.width):
                color_bitmap[x, y] = red_color

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=None)
        self.splash.append(bg_sprite)

    def animate_text(self):
        # Animate the text by moving it across the screen
        try:
            while True:
                for x in range(self.width):
                    self.text_area.x = x
                    time.sleep(self.speed)  # Adjust speed by changing the sleep duration
        except KeyboardInterrupt:
            # Gracefully exit on Ctrl+C
            print("\nAnimation stopped. Exiting...")
            sys.exit(0)


# Example of how to use the class
if __name__ == "__main__":
    tft_display = TFT_Display(width=161, height=130, rotation=90, text="Hello, Andrei!", speed=0.05)
    tft_display.animate_text()
