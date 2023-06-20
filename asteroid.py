import pygame
import sys
import time
import random
import math

# 화면 크기 설정
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# pygame 초기화
pygame.init()

# 게임 창 제목 설정
pygame.display.set_caption('SpaceShuttle')

# 화면 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 폰트 설정
myFont = pygame.font.SysFont('arial', 30, True, False)

# 우주선 이미지 로드
imgShuttle = pygame.image.load('ss.png')

# 게임 시간 설정
clock = pygame.time.Clock()

# 우주선 위치 설정
shuttle_rect = imgShuttle.get_rect()
shuttle_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# 운석 생성
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

# 게임 시작 시간 설정
startTime = time.time()

# 게임 루프
while True:
    # FPS 설정
    clock.tick(30)

    # 화면 검은색으로 채우기
    screen.fill((0, 0, 0))

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키보드 입력 처리
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

    # 우주선 외곽선 그리기
    pygame.draw.circle(screen, (255, 255, 255), shuttle_rect.center, max(
        shuttle_rect.width, shuttle_rect.height) / 2 + 10, 2)

    # 운석 이동 및 충돌 처리
    for asteroid in asteroids:
        asteroid['rect'].x += asteroid['speed'] * math.cos(asteroid['direction'])
        asteroid['rect'].y += asteroid['speed'] * math.sin(asteroid['direction'])

        # 운석이 화면 밖으로 나갈 경우 방향 전환
        if asteroid['rect'].left > SCREEN_WIDTH or asteroid['rect'].right < 0:
            asteroid['direction'] = math.pi - asteroid['direction']
        if asteroid['rect'].top > SCREEN_HEIGHT or asteroid['rect'].bottom < 0:
            asteroid['direction'] = -asteroid['direction']

        # 운석 그리기
        pygame.draw.circle(screen, (255, 255, 255), asteroid['rect'].center, asteroid_radius)

        # 우주선과 충돌 시 게임 종료 및 경과 시간 출력
        if asteroid['rect'].colliderect(shuttle_rect):
            endTime = time.time()
            time_diff = str(endTime - startTime)
            print("Game Over!")
            print("Elapsed Time:", time_diff)
            pygame.quit()
            sys.exit()

    # 경과 시간 출력
    time_diff = str(time.time() - startTime)
    currentTime_text = myFont.render(time_diff, 1, (255, 255, 255))
    screen.blit(currentTime_text, [SCREEN_WIDTH - 70, 20])

    # 우주선 그리기
    screen.blit(imgShuttle, shuttle_rect)

    # 화면 업데이트
    pygame.display.update()