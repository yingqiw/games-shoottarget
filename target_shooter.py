import sys, pygame
import math

screen_width = 640
screen_height = 480
win = pygame.display.set_mode((screen_width, screen_height))
white = (255, 255, 255)
black = (0, 0, 0)

# target
targetY = 150
targetX = 100
targetX_change = 0
targetY_change = 0

# bullet
velocity = 10
theta = 20
time = 0
bullet_x = 0
bullet_y = screen_height
bullet_state = "ready"


def update_position(t):
    g = 9.8 / 100
    global bullet_x
    global bullet_y
    global bullet_state
    global velocity
    global theta
    if bullet_state is "fire":
        bullet_x = velocity * math.cos(theta) * t
        bullet_y = velocity * math.sin(theta) * t - 0.5 * g * t * t
        bullet_y = screen_height - bullet_y
        #print(str(bullet_x) + "   " + str(bullet_y))
    if bullet_x > screen_width or bullet_x < 0 or bullet_y > screen_height or bullet_y < -1:
        bullet_state = "ready"
        bullet_x = 0
        bullet_y = screen_height


def fire_bullet():
    global bullet_x
    global bullet_y
    global bullet_state
    global time
    if bullet_state is "ready":
        time = 0
        bullet_state = "fire"


while 1:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                targetY_change = -.4

            if event.key == pygame.K_DOWN:
                targetY_change = .4

            if event.key == pygame.K_LEFT:
                targetX_change = -.4

            if event.key == pygame.K_RIGHT:
                targetX_change = .4

            if event.key == pygame.K_SPACE:
                fire_bullet()

            if event.key == pygame.K_w:
                theta += 0.1
            if event.key == pygame.K_s:
                theta -= 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                targetX_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_DOWN:
                targetY_change = 0

    if targetY <= 0:
        targetY = 0
    if targetY >= 430:
        targetY = 430
    if targetX >= 590:
        targetX = 590
    if targetX <= 320:
        targetX = 320

    targetX += targetX_change
    targetY += targetY_change

    if bullet_state is "fire":
        time = time + 0.05
        update_position(time)

    bullet = pygame.Rect(bullet_x, bullet_y, 10, 10)
    print(str(bullet_x) + "   " + str(bullet_y))
    target = pygame.Rect(targetX, targetY, 50, 50)
    win.fill(black)
    win.fill(white, target)
    win.fill(white, bullet)
    pygame.display.flip()
