import sys
import pygame
import time

pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 829, 836 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clock")

# Load the background image
background_image = pygame.image.load('main-clock.png')  # Replace 'background.jpg' with your background image path

# Set up the clock
clock = pygame.time.Clock()

# Function to rotate and blit the image
def blitRotate(surf, image, pos, originPos, angle):
    # Offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # Rotated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # Rotated image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # Get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # Rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
  

try:
    image = pygame.image.load('right-hand.png')
    image2 = pygame.image.load('left-hand.png')
except:
    text = pygame.font.SysFont('Times New Roman', 50).render('image', False, (255, 255, 0))
    image = pygame.Surface((text.get_width() + 1, text.get_height() + 1))
    pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
    image.blit(text, (1, 1))
w, h = image.get_size()

done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Get the current time
    current_time = time.localtime()
    seconds_angle = current_time.tm_sec * 6  # 360 degrees / 60 seconds = 6 degrees per second
    minutes_angle = current_time.tm_min * 6  # 360 degrees / 60 minutes = 6 degrees per minute

    # Fill the screen with the background image
    screen.blit(background_image, (0, 0))

    # Rotate and blit the image
    pos = (screen.get_width() / 2, screen.get_height() / 2)
    blitRotate(screen, image, pos, (w / 2, h / 2), minutes_angle)
    pos2 = (screen.get_width() / 2, 836 / 2)
    blitRotate(screen, image2, pos2, (w / 2, h / 2), seconds_angle)

    pygame.display.flip()


pygame.quit()
sys.exit()

