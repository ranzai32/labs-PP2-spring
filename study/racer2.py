# Импорт библиотек
import pygame, sys
from pygame.locals import *
import random, time
 
# Инициализация Pygame
pygame.init()
 
# Настройка FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Определение цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Другие переменные, используемые в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
 
# Создание белого экрана
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Загрузка и масштабирование фона
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (80, 90))  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)    
 
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (80, 90))  
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
# Создание спрайтов        
P1 = Player()
E1 = Enemy()
 
# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
# Добавление нового пользовательского события
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
# Игровой цикл
while True:
       
    # Обработка всех событий  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 1
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    # Заливка экрана белым цветом
    DISPLAYSURF.fill(WHITE)
    
    # Отображение фона
    DISPLAYSURF.blit(background, (0, 0))
 
    # Движение и перерисовка всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    # Если произошло столкновение между игроком и врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        font = pygame.font.SysFont(None, 48)  
        text_surface = font.render('Game Over', True, RED) 
        DISPLAYSURF.blit(text_surface, (115, 250)) 
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()  
         
    pygame.display.update()
    FramePerSec.tick(FPS)

