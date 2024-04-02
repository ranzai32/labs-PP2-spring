import pygame 
import random
pygame.init()

W, H = 1280, 720
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

ball2 = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx2, dy2 = -1, 1

ball3 = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx3, dy3 = 1, 1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

#bonus blocks
bonus_block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(random.randrange(0,10)) for j in range (random.randrange(0,4))]
bonus_color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 

#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(8) for j in range (3)]
for b in block_list:
    if b in bonus_block_list:
        block_list.remove(b)
        
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 

#unremoveble blocks
unremoveble_block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(1) for j in range (4)]
for b in unremoveble_block_list:
    if b in bonus_block_list or block_list:
        unremoveble_block_list.remove(b)

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] #drawing blocks
    [pygame.draw.rect(screen, bonus_color_list[color], block)
     for color, block in enumerate (bonus_block_list)] #drawing blocks
    [pygame.draw.rect(screen, 'white', block)
     for color, block in enumerate (unremoveble_block_list)] #drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    ball2.x += ballSpeed * dx2
    ball2.y += ballSpeed * dy2

    ball3.x += ballSpeed * dx3
    ball3.y += ballSpeed * dy3

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50: 
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
        
    if ball2.centerx < ballRadius or ball2.centerx > W - ballRadius:
        dx2 = -dx2
    if ball2.centery < ballRadius + 50: 
        dy2 = -dy2
    if ball2.colliderect(paddle) and dy2 > 0:
        dx2, dy2 = detect_collision(dx2, dy2, ball2, paddle)
        
    if ball3.centerx < ballRadius or ball3.centerx > W - ballRadius:
        dx3 = -dx3
    if ball3.centery < ballRadius + 50: 
        dy3 = -dy3
    if ball3.colliderect(paddle) and dy3 > 0:
        dx3, dy3 = detect_collision(dx3, dy3, ball3, paddle)
    
    # block_list
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()
    #bonus block_list
    hitIndex1 = ball.collidelist(bonus_block_list)
    
    block_execution_time = 5000
    # bonus block execution time
    if hitIndex1 != -1:
        hitRect = bonus_block_list.pop(hitIndex)
        hitColor = bonus_color_list.pop(hitIndex)
        start_time = pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()
        paddleW = 3 * paddleW
        if start_time - current_time  == block_execution_time:
            paddleW = 150
            
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        #tripple balls
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball2.center, ballRadius)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball3.center, ballRadius)
        game_score += 1
        collision_sound.play()
    # unremovble block_list 
    hitIndex2 = ball.collidelist(unremoveble_block_list)

    if hitIndex2 != -1:  
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        collision_sound.play()
    
    ballSpeed += 0.005
    
    while paddleW <= 100:
        paddleW -= 0.5
    
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)
