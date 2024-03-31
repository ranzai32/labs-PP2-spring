import pygame
import sys
import random
import time

pygame.init()

# Настройки FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Размеры экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Создание экрана
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Загрузка фонового изображения и масштабирование его под размер экрана
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (80, 90))  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)    

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)

    def explode(self):
        # Здесь можно добавить анимацию взрыва
        pass

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (80, 90))  
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.health = 100  # Уровень здоровья игрока

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0  # Здесь можно добавить дополнительные действия при потере всего здоровья

# Создание спрайтов        
P1 = Player()
E1 = Enemy()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Установка начальной скорости движения
SPEED = 5

# Добавление нового пользовательского события для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    # Обработка всех событий  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 1
        if event.type == pygame.QUIT:
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

    # Обработка коллизий между игроком и врагами
    collisions = pygame.sprite.spritecollide(P1, enemies, True)
    for enemy in collisions:
        P1.damage(10)  # Уменьшение здоровья игрока
        enemy.explode()  # Анимация взрыва врага

    # Отображение уровня здоровья игрока
    font = pygame.font.SysFont(None, 24)
    health_text = font.render("Health: " + str(P1.health), True, RED)
    DISPLAYSURF.blit(health_text, (10, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)
