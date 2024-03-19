import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill(THECOLORS['white'])
font = pygame.font.SysFont('couriernew', 40)
text = font.render(str('HELLO'), True, THECOLORS['green'])
screen.blit(text, (330, 100))

r = pygame.Rect(50, 50, 100, 200)
pygame.draw.rect(screen, (255, 0, 0), r, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()