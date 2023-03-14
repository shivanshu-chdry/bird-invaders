import pygame #Import pygame


pygame.init() #Initialize pygame


screen = pygame.display.set_mode((800,600)) #Display screen
pygame.display.set_caption("Bird Invader")

#Slingshot
slingshot = pygame.image.load("slingshot.png")
slingshotX = 370
slingshotY = 480
slingshotX_change = 0

#Bird
bird = pygame.image.load("bird.png")
birdX = 370
birdY = 120
bird_x_dir = 0.3

#Stone
stone = pygame.image.load("stone.png")
stoneX = 0
stoneY = 475
stoneX_change = 0
stoneY_change = 0.4
fire_state = "ready"

#Weapon function
def weapon(x,y):
    screen.blit(slingshot, (x, y)) #Draws slingshot.png at the given (X,Y) axis.

def enemy(x,y):
    screen.blit(bird, (x, y))

def rock(x,y):
    global fire_state
    fire_state = "fire"
    screen.blit(stone, (x, y))

running = True

#Game loop
while running:

    screen.fill((255,255,255))
    screen.blit(stone, (380, stoneY))
    stoneX = slingshotX + 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Quit event
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

    if fire_state == "fire":
        rock(slingshotX, stoneY)
        stoneY -= stoneY_change

    enemy(birdX, birdY)
    weapon(slingshotX,slingshotY) #Calls weapon function

    pygame.display.update()

