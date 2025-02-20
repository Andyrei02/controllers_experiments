import time
import board
import busio
import adafruit_dht
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class Dispaly:
    def __init__(self, oled, font_path=None):
        self.oled = oled
        self.font = ImageFont.truetype(font_path) if font_path else ImageFont.load_default()
        
    
    def show(self, x, y, text) :
        image = Image.new("1", (self.oled.width, self.oled.height))
        draw = ImageDraw.Draw(image)
        
        draw.text((x, y), text, self.font)
        
        self.oled.image(image)
        self.oled.show()
    
    def clear():
        self.oled.fill(0)
        self.oled.show()


def get_sensor_data(dht_device):
    temperature = dht_device.temperature
    humidity = dht_device.humidity
    return temperature, humidity


def main():
    # Initialize the OLED display (adjust width and height as needed)
    WIDTH = 128
    HEIGHT = 64
    
    # Initialize DHT11 sensor (GPIO4)
    dht_device = adafruit_dht.DHT11(board.D4)
    
    # Uses I2C interface
    i2c = board.I2C()  
    oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
    
    # Load custom font
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)

    dispaly = Display(oled)

    try:    
        run = True
        while run:
            temp, humidity = get_sensor_data(dht_device)
            temperature = f"Temp: {temp}C"
            humidity = f"Humidity: {humidity}%"
            print(temperature)
            print(humidity)
            
            dispaly.show((10, 10), temperature)
            dispaly.show((10, 30), humidity)
    except KeyboardInterrupt:
        print("\n[INFO] Program interrupted! Clearing display...")
        dispaly.clear()
        print("[INFO] Display cleared. Exiting.")
    

if __name__ == "__main__":
    main()
