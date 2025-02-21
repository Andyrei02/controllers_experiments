import time
import board
import displayio
import digitalio
import pygame
from adafruit_st7735r import ST7735R

# Initialize Pygame
pygame.init()

# Set Pygame drawing size (match your TFT size)
WIDTH, HEIGHT = 161, 130
pygame_screen = pygame.Surface((WIDTH, HEIGHT))  # Virtual screen

# Release previous displays
displayio.release_displays()

# SPI Setup
spi = board.SPI()
tft_dc = board.D24
tft_cs = board.CE0
tft_rst = board.D25

# Create display bus
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

# Initialize Display
display = ST7735R(display_bus, width=WIDTH, height=HEIGHT, rotation=90)

# Function to update TFT with Pygame surface
def update_display():
    global pygame_screen

    # Convert Pygame surface to raw pixels
    pixel_data = pygame.image.tostring(pygame_screen, "RGB")  # Convert to raw RGB data

    # Create a Bitmap to store pixel data
    bitmap = displayio.Bitmap(WIDTH, HEIGHT, 65536)
    
    # Fill the bitmap with pixel data
    for y in range(HEIGHT):
        for x in range(WIDTH):
            r, g, b = pixel_data[(y * WIDTH + x) * 3:(y * WIDTH + x + 1) * 3]
            color = ((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3)  # Convert to RGB565
            bitmap[x, y] = color
    
    # Display the new frame
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=None)
    display.root_group = displayio.Group()
    display.root_group.append(tile_grid)

# Main loop (Animation)
running = True
while running:
    pygame_screen.fill((0, 0, 0))  # Clear screen (black)

    # Draw a moving circle (example animation)
    for i in range(50):
        pygame_screen.fill((0, 0, 0))  # Clear previous frame
        pygame.draw.circle(pygame_screen, (255, 255, 0), (i * 2, HEIGHT // 2), 10)  # Yellow circle

        update_display()  # Send frame to TFT
        time.sleep(0.05)  # Adjust speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
