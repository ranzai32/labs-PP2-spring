import pygame

SIZE_BLOCK = 20
WIDTH, HEIGHT = 400, 600
FRAME_COLOR = (0, 255, 204)
BLUE = (204, 255, 255)
WHITE = (255, 255, 255)
COUNT_BLOCK = 20
MARGIN = 1

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Snake Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    screen.fill(FRAME_COLOR)
    for row in range(COUNT_BLOCK):
        for column in range(COUNT_BLOCK):
            if column % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [10+column*SIZE_BLOCK + MARGIN * (column+ 1), 20+row*SIZE_BLOCK+MARGIN*(row+1), SIZE_BLOCK, SIZE_BLOCK])
    
    pygame.display.flip()
    