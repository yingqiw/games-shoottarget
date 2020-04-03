import sys, pygame
import math

g = 9.8
screen_size = width, height = 640, 480

targetY = 150
targetX = 100

bullet_x = 100
bullet_y = 20

targetX_change = 0
targetY_change = 0

win = pygame.display.set_mode(screen_size)
white = (255, 255, 255)
black = (0, 0, 0)

'''def get_intervals(u, theta):
    t_flight = 2 * u * math.sin(theta) / g
    intervals = []
    start = 0
    interval = 0.005
    while start < t_flight:
        intervals.append(start)
        start = start + interval
    return intervals

def update_position(i, circle, intervals, u, theta):
    t = intervals[i]
    x = u * math.cos(theta) * t
    y = u * math.sin(theta) * t - 0.5 * g * t * t
    circle.center = x, y
    return circle,
'''

while 1:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                targetY_change = -.4

            if event.key == pygame.K_DOWN:
                targetY_change = .4

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                targetX_change = -.4

            if event.key == pygame.K_RIGHT:
                targetX_change = .4

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

    target = pygame.Rect(targetX, targetY, 50, 50)
    win.fill(black)
    win.fill(white, target)
    pygame.display.flip()
