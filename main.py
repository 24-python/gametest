import pygame
import random
import math

pygame.init()

# Основные параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

# Изображение мишени
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# Переменная для хранения счета
score = 0

# Шрифт для отображения счета
font = pygame.font.Font(None, 36)

# Скорость мишени в пикселях в секунду (1 см ≈ 38 пикселей)
speed = 38

# Переменные для направления движения мишени
direction_x = random.choice([-1, 1])
direction_y = random.choice([-1, 1])

# Переменная для отслеживания времени
clock = pygame.time.Clock()

# Основной цикл игры
running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1  # Увеличиваем счет при попадании

    # Обновление позиции мишени
    target_x += direction_x * speed / 60  # Делим на 60, так как обновляем 60 раз в секунду
    target_y += direction_y * speed / 60

    # Проверка границ экрана и смена направления при столкновении
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        direction_x *= -1
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        direction_y *= -1

    # Отображение мишени
    screen.blit(target_img, (target_x, target_y))

    # Отображение счета
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))

    pygame.display.update()

    # Ограничение FPS до 60 кадров в секунду
    clock.tick(60)

pygame.quit()