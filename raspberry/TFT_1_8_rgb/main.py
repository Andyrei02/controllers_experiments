import time
import board
import displayio
import pygame
from adafruit_st7735r import ST7735R

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 160, 128  # Match TFT size
pygame_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TFT Display Simulation")
pygame_surface = pygame.Surface((WIDTH, HEIGHT))

# Release previous displays
displayio.release_displays()

# SPI Setup
spi = board.SPI()
tft_dc = board.D24
tft_cs = board.CE0
tft_rst = board.D25

# Create display bus
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7735R(display_bus, width=WIDTH, height=HEIGHT)

# Force display to GBR mode (if needed)
display.bus.send(0x36, b'\x00')  # Try b'\x00' for RGB, b'\x08' for BGR


def update_display():
    """Convert Pygame surface to TFT-compatible GBR565 format."""
    global pygame_surface

    # Convert Pygame surface to pixel array
    pixel_data = pygame.surfarray.array3d(pygame_surface)

    # Create Bitmap
    bitmap = displayio.Bitmap(WIDTH, HEIGHT, 65536)

    # Fill the bitmap with GBR565 corrected colors
    for y in range(HEIGHT):
        for x in range(WIDTH):
            r, g, b = pixel_data[x, y]  # Get RGB values
            color = ((g & 0xF8) << 8) | ((b & 0xFC) << 3) | (r >> 3)  # GBR565 Fix
            bitmap[x, y] = color

    # Send bitmap to display
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=None)
    display.root_group = displayio.Group()
    display.root_group.append(tile_grid)


# Main loop (Animation)
running = True
x = 0
while running:
    pygame_surface.fill((0, 255, 0))  # Green background
    pygame_screen.fill((0, 0, 0))  # Black background on desktop

    # Draw a moving RED circle (previously broken!)
    pygame.draw.circle(pygame_surface, (255, 0, 0), (x, HEIGHT // 2), 10)  # Red Circle
    pygame.draw.circle(pygame_screen, (255, 0, 0), (x, HEIGHT // 2), 10)  # Show on Desktop

    # Send to TFT
    update_display()
    pygame.display.flip()

    # Move circle
    x += 2
    if x > WIDTH:
        x = 0  # Reset position

    # Handle exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.05)

pygame.quit()
