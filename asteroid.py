import pygame
import sys
import time
import random
import math

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()

pygame.display.set_caption('Space')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

myFont = pygame.font.SysFont('arial', 30, True, False)

imgShuttle = pygame.image.load('ss.png')

clock = pygame.time.Clock()

shuttle_rect = imgShuttle.get_rect()
shuttle_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

asteroids = []
num_asteroids = 5
asteroid_radius = 15
for _ in range(num_asteroids):
    asteroid_x = random.randint(1, SCREEN_WIDTH)
    asteroid_y = random.randint(1, SCREEN_HEIGHT)
    asteroid_speed = random.randint(1, 7)
    asteroid_direction = random.uniform(0, 2 * math.pi)
    asteroid = {
        'rect': pygame.Rect(asteroid_x, asteroid_y, asteroid_radius * 2, asteroid_radius * 2),
        'speed': asteroid_speed,
        'direction': asteroid_direction
    }
    asteroids.append(asteroid)

startTime = time.time()

while True:
    clock.tick(30)

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        shuttle_rect.x -= 3
    if keys[pygame.K_RIGHT]:
        shuttle_rect.x += 3
    if keys[pygame.K_UP]:
        shuttle_rect.y -= 3
    if keys[pygame.K_DOWN]:
        shuttle_rect.y += 3
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()

    pygame.draw.circle(screen, (255, 255, 255), shuttle_rect.center, max(
        shuttle_rect.width, shuttle_rect.height) / 2 + 10, 2)

    for asteroid in asteroids:
        asteroid['rect'].x += asteroid['speed'] * math.cos(asteroid['direction'])
        asteroid['rect'].y += asteroid['speed'] * math.sin(asteroid['direction'])

        if asteroid['rect'].left > SCREEN_WIDTH or asteroid['rect'].right < 0:
            asteroid['direction'] = math.pi - asteroid['direction']
        if asteroid['rect'].top > SCREEN_HEIGHT or asteroid['rect'].bottom < 0:
            asteroid['direction'] = -asteroid['direction']

        pygame.draw.circle(screen, (255, 255, 255), asteroid['rect'].center, asteroid_radius)

        if asteroid['rect'].colliderect(shuttle_rect):
            endTime = time.time()
            time_diff = str(endTime - startTime)
            print("Game Over!")
            print("Elapsed Time:", time_diff)
            pygame.quit()
            sys.exit()

    time_diff = str(time.time() - startTime)
    currentTime_text = myFont.render(time_diff, 1, (255, 255, 255))
    screen.blit(currentTime_text, [SCREEN_WIDTH - 70, 20])

    screen.blit(imgShuttle, shuttle_rect)

    pygame.display.update()