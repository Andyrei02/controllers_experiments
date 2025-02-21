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
pygame_screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create a visible Pygame window
pygame.display.set_caption("TFT Display Simulation")

# Virtual surface for drawing (same size as TFT)
pygame_screen = pygame.Surface((WIDTH, HEIGHT))

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
x = 0
while running:
    pygame_surface.fill((0, 0, 0))  # Clear virtual surface
    pygame_screen.fill((0, 0, 0))   # Clear desktop window

    # Draw a moving yellow circle (animation)
    pygame.draw.circle(pygame_surface, (255, 255, 0), (x, HEIGHT // 2), 10)
    pygame.draw.circle(pygame_screen, (255, 255, 0), (x, HEIGHT // 2), 10)  # Draw on desktop

    # Send frame to TFT display
    update_display()

    # Update Pygame desktop window
    pygame.display.flip()

    # Move the circle
    x += 2
    if x > WIDTH:
        x = 0  # Reset position

    # Handle events (for closing the Pygame window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.05)  # Adjust animation speed

pygame.quit()
