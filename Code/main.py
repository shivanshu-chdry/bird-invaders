import pygame 
import math
import random


pygame.init()


screen = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("Bird Invader")

#Slingshot
slingshot = pygame.image.load("slingshot.png")
slingshotX = 345
slingshotY = 480
slingshotX_change = 0

#Birds
bird = pygame.image.load("bird.png")
birdX = 370
birdY = 120
bird_x_dir = 0.5

birdX2 = 200
birdY2 = 120
bird_x_dir2 = 0.5

birdX3 = 540
birdY3 = 120
bird_x_dir3 = 0.5

#Stone
stone = pygame.image.load("stone.png")
stoneX = 0
stoneY = 475
stoneX_change = 0
stoneY_change = 0.6
fire_state = "ready"


butterfly = pygame.image.load("butterfly.png")
butterflyX = 820
original = butterflyX
butterflyY = 120
butterflyX_change = 0.4

butterflyX2 = 1100
original2 = butterflyX2

butterflyX3 = 1380
original3 = butterflyX3



score = 0

#Weapon function
def weapon(x,y):
    screen.blit(slingshot, (x, y)) 

def enemy(x,y):
    screen.blit(bird, (x, y))

def enemy2(x,y):
    screen.blit(bird, (x, y))

def enemy3(x,y):
    screen.blit(bird, (x, y))

def rock(x,y):
    global fire_state
    fire_state = "fire"
    screen.blit(stone, (x, y))

def collision1(birdX, birdY, stoneX, stoneY):
    distance = math.sqrt((math.pow(birdX - stoneX, 2)) + (math.pow(birdY - stoneY, 2)))
    if distance < 35:
        return True
    else:
        return False

def collision2(birdX2, birdY2, stoneX, stoneY):
    distance = math.sqrt((math.pow(birdX2 - stoneX, 2)) + (math.pow(birdY2 - stoneY, 2)))
    if distance < 35:
        return True
    else:
        return False
    
def collision3(birdX3, birdY3, stoneX, stoneY):
    distance = math.sqrt((math.pow(birdX3 - stoneX, 2)) + (math.pow(birdY3 - stoneY, 2)))
    if distance < 35:
        return True
    else:
        return False
    
def innocent(x, y):
    screen.blit(butterfly, (x, y))

def innocent2(x, y):
    screen.blit(butterfly, (x, y))

def innocent3(x, y):
    screen.blit(butterfly, (x, y))


running = True

#Game loop
while running:

    screen.fill((255,255,255))
    stoneX = slingshotX + 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                slingshotX_change = -0.3
            if event.key == pygame.K_RIGHT:
                slingshotX_change = 0.3
            if event.key == pygame.K_SPACE:
                rock(slingshotX, stoneY)
            
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                slingshotX_change = 0
        

    slingshotX += slingshotX_change

    birdX += bird_x_dir
    birdX2 += bird_x_dir2
    birdX3 += bird_x_dir3

    butterflyX -= butterflyX_change
    butterflyX2 -= butterflyX_change
    butterflyX3 -= butterflyX_change

    if slingshotX < 5:
        slingshotX = 5

    if slingshotX > 735:
        slingshotX = 735

    if birdX < 5:
        birdX = 5
        bird_x_dir *= -1

    if birdX > 735:
        birdX = 735
        bird_x_dir *= -1

    if birdX2 < 5:
        birdX2 = 5
        bird_x_dir2 *= -1

    if birdX2 > 735:
        birdX2 = 735
        bird_x_dir2 *= -1

    if birdX3 < 5:
        birdX3 = 5
        bird_x_dir3 *= -1

    if birdX3 > 735:
        birdX3 = 735
        bird_x_dir3 *= -1


    if butterflyX < 5:
        butterflyX = original

    if butterflyX2 < 5:
        butterflyX2 = original2

    if butterflyX3 < 5:
        butterflyX3 = original3


    if fire_state == "fire":
        rock(slingshotX + 10, stoneY)
        stoneY -= stoneY_change

    if stoneY <= 0:
        stoneY = 475
        fire_state = "ready"




    Collision = collision1(birdX, birdY, stoneX, stoneY)
    Collision2 = collision2(birdX2, birdY2, stoneX, stoneY)
    Collision3 = collision3(birdX3, birdY3, stoneX, stoneY)

    InnocentCollision = collision1(butterflyX, butterflyY, stoneX, stoneY)
    InnocentCollision2 = collision2(butterflyX2, butterflyY, stoneX, stoneY)
    InnocentCollision3 = collision3(butterflyX3, butterflyY, stoneX, stoneY)

    if Collision:
        fire_state = "ready"
        stoneY = 475
        birdX = random.randint(0,800)
        score += 1
        print(score)
    if Collision2:
        fire_state = "ready"
        stoneY = 475
        birdX2 = random.randint(0,800)
        score += 1
        print(score)
    if Collision3:
        fire_state = "ready"
        stoneY = 475
        birdX3 = random.randint(0,800)
        score += 1
        print(score)

    if InnocentCollision:
        running = False

    if InnocentCollision2:
        running = False

    if InnocentCollision3:
        running = False
    

    enemy(birdX, birdY)
    enemy2(birdX2, birdY2)
    enemy3(birdX3, birdY3)

    weapon(slingshotX,slingshotY)

    innocent(butterflyX, butterflyY)
    innocent(butterflyX2, butterflyY)
    innocent(butterflyX3, butterflyY)

    pygame.display.update()

gameover = True

while gameover:

    screen.fill((255,255,255))
    stoneX = slingshotX + 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameover = False

    screen.fill((255,255,255))
    over = pygame.font.Font("freesansbold.ttf",45)
    overfont = over.render("GAME OVER", True, (0,0,0))
    screen.blit(overfont, (260,300))

    pygame.display.update()