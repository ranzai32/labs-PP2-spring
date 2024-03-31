import pygame
import time
import random

pygame.init()

# Установка цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

WIDTH, HEIGHT = 600, 400

# Установка экрана
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Змейка")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)
level_font = pygame.font.SysFont('ubuntu', 30)

def print_score(score):
    text = score_font.render("Score " + str(score), True, orange)
    screen.blit(text, [0,0])
    
def print_level(level):
    text = level_font.render("Level: " + str(level), True, orange)
    screen.blit(text, [WIDTH - 150, 0])
    
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():
    global snake_speed
    
    game_over = False 
    game_close = False
    
    x = WIDTH / 2 
    y = HEIGHT / 2
    
    x_speed = 0
    y_speed = 0
    
    snake_pixels = []
    snake_length = 1
    
    target_x = round(random.randrange(0, WIDTH-snake_size)/ 10.0) * 10.0
    target_y = round(random.randrange(0, HEIGHT-snake_size)/ 10.0) * 10.0
    
    level = 1
    
    while not game_over:
        
        while game_close:
            screen.fill(black)
            game_over_message = message_font.render("Game Over", True, red)
            screen.blit(game_over_message, [WIDTH / 3, HEIGHT / 3])
            print_score(snake_length - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                    
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                    
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
                    
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        x += x_speed
        y += y_speed
        
        screen.fill(black)
        pygame.draw.rect(screen, orange, [target_x, target_y, snake_size, snake_size])
        
        snake_pixels.append([x,y])
        
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]
            
        for pixel in snake_pixels[:-1]:
            if pixel == [x,y]:
                game_close = True
        
        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)
        print_level(level)
        
        pygame.display.update()
        
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, WIDTH-snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, HEIGHT-snake_size) / 10.0) * 10.0
            snake_length += 1
            level += 1
            snake_speed += 2  # Увеличиваем скорость змеи
            
        clock.tick(snake_speed)

    pygame.quit() 
    quit()

run_game()       
          