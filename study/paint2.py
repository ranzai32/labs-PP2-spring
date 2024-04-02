import pygame
pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
active_size = 0 # Дефолтные значения для кисти
active_color = 'white' # Начальный цвет, порядок очень важен, так как если указать его позже наша программа выдаст ошибку
painting = []
tool = "brush"

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Paint")

def draw_menu(color, size):
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0,70), (WIDTH, 70))
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35,35), 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95,35), 15)
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155,35), 10)
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215,35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush] # Создали список для наших кистей, потому что нам придется их выбирать
    
    pygame.draw.circle(screen, color, (400,35),30)
    circle_button = pygame.draw.rect(screen, 'black', [250, 10, 50, 50]) 
    pygame.draw.circle(screen, 'white', (275, 35), 20)
    rectangle_button = pygame.draw.rect(screen, 'black', [310, 10, 50, 50]) 
    pygame.draw.rect(screen, 'white', [315, 15, 40, 40]) 
    
    blue = pygame.draw.rect(screen, (0,0,255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255,0,0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0,255,0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255,255,0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0,255,255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255,0,255), [WIDTH - 85, 35, 25, 25])
    white = pygame.draw.rect(screen, (255,255,255), [WIDTH - 110, 10, 25, 25])  
    black = pygame.draw.rect(screen, (0,0,0), [WIDTH - 110, 35, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, white, black]
    rgb_list = [(0,0,255), (255,0,0), (0,255,0), (255,255,0), (0,255,255), (255,0,255), 
                (255,255,255), (0,0,0)]
    tool_list = [circle_button, rectangle_button]
    
    return brush_list, color_rect, rgb_list, tool_list # Возвращаем значение кистей, цветов

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2], paints[i][3])

running = True
while running:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size, tool))
    draw_painting(painting)
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, active_size)
    brushes, colors, rgbs, tool = draw_menu(active_color, active_size)
         
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
                    
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
    pygame.display.flip()
    
pygame.quit()
