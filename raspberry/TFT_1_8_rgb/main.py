import time
import board
import displayio
import digitalio
from adafruit_st7735r import ST7735R
from adafruit_display_text import label
import terminalio
import sys
import os


class TFT_Display:
    def __init__(self, width=161, height=130, rotation=90, text="25°C", text2="60%", speed=0.05):
        # Release any previous displays
        displayio.release_displays()
        current_path = os.path.abspath(os.getcwd())
        self.temp_ico_path = os.path.join(current_path, "temp_icon.bmp")

        # SPI setup
        self.spi = board.SPI()
        self.tft_dc = board.D24  # Data/Command pin
        self.tft_cs = board.CE0  # Chip Select pin
        self.tft_rst = board.D25  # Reset pin

        self.width = width
        self.height = height
        self.text = text
        self.text2 = text2
        self.speed = speed

        # Create display bus
        self.display_bus = displayio.FourWire(self.spi, command=self.tft_dc, chip_select=self.tft_cs, reset=self.tft_rst)

        # Initialize Display
        self.display = ST7735R(self.display_bus, width=self.width, height=self.height, rotation=rotation)
        
        # Create Display Context
        self.splash = displayio.Group()
        self.display.root_group = self.splash

        # Set the background color (Red)
        self.set_background_color()

        # Create labels for temperature and humidity
        self.text_area1 = label.Label(terminalio.FONT, text=self.text, color=0xFFFF)  # White text
        self.text_area1.x = 50  # Position next to icon
        self.text_area1.y = 30

        self.text_area2 = label.Label(terminalio.FONT, text=self.text2, color=0xFFFF)
        self.text_area2.x = 50
        self.text_area2.y = 70

        self.splash.append(self.text_area1)
        self.splash.append(self.text_area2)

        # Load and display icons
        self.load_icons()

    def set_background_color(self):
        """Fill the background with a solid color."""
        color_bitmap = displayio.Bitmap(self.width, self.height, 65536)
        red_color = (31 << 11) | (0 << 5) | (0)  # Red in RGB565
        for y in range(self.height):
            for x in range(self.width):
                color_bitmap[x, y] = red_color

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=None)
        self.splash.append(bg_sprite)

    def load_icons(self):
        """Load and display BMP icons."""
        try:
            # Temperature icon
            temp_bitmap = displayio.OnDiskBitmap(self.temp_ico_path)  # Path to your BMP
            temp_tilegrid = displayio.TileGrid(temp_bitmap, pixel_shader=temp_bitmap.pixel_shader)
            temp_tilegrid.x = 10
            temp_tilegrid.y = 20
            self.splash.append(temp_tilegrid)

            # Humidity icon
            humid_bitmap = displayio.OnDiskBitmap(self.temp_ico_path)
            humid_tilegrid = displayio.TileGrid(humid_bitmap, pixel_shader=humid_bitmap.pixel_shader)
            humid_tilegrid.x = 10
            humid_tilegrid.y = 60
            self.splash.append(humid_tilegrid)

        except Exception as e:
            print("Error loading icons:", e)

    def animate_text(self):
        """Move text for animation effect."""
        try:
            while True:
                for x in range(self.width - 50):
                    self.text_area1.x = 50 + x
                    self.text_area2.x = 50 + x
                    time.sleep(self.speed)  # Adjust speed
        except KeyboardInterrupt:
            print("\nAnimation stopped. Exiting...")
            sys.exit(0)


# Example usage
if __name__ == "__main__":
    tft_display = TFT_Display(text="25°C", text2="60%")
    tft_display.animate_text()
