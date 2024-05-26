import pygame
import random

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

# Время начала игры
start_ticks = pygame.time.get_ticks()

# Функция для отображения окна с кнопками
def show_game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Вы проиграли! Начать заново?", True, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    pygame.draw.rect(screen, (0, 255, 0), (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50))
    pygame.draw.rect(screen, (255, 0, 0), (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 110, 200, 50))

    yes_text = font.render("Да", True, (0, 0, 0))
    no_text = font.render("Нет", True, (0, 0, 0))

    screen.blit(yes_text, (SCREEN_WIDTH // 2 - yes_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(no_text, (SCREEN_WIDTH // 2 - no_text.get_width() // 2, SCREEN_HEIGHT // 2 + 110))

    pygame.display.update()

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
                start_ticks = pygame.time.get_ticks()  # Сбрасываем таймер при попадании

    # Проверка времени
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Преобразуем в секунды
    if seconds > 5:
        show_game_over()
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_input = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if SCREEN_WIDTH // 2 - 100 < mouse_x < SCREEN_WIDTH // 2 + 100:
                        if SCREEN_HEIGHT // 2 + 50 < mouse_y < SCREEN_HEIGHT // 2 + 100:
                            # Начать заново
                            target_x = random.randint(0, SCREEN_WIDTH - target_width)
                            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                            score = 0
                            start_ticks = pygame.time.get_ticks()
                            waiting_for_input = False
                        if SCREEN_HEIGHT // 2 + 110 < mouse_y < SCREEN_HEIGHT // 2 + 160:
                            # Выход из игры
                            running = False
                            waiting_for_input = False

    # Обновление позиции мишени
    target_x += direction_x * speed / 60  # Делим на 60, так как обновляем 60 раз в секунду
    target_y += direction_y * speed / 60

    # Проверка границ экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        direction_x = -direction_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        direction_y = -direction_y

    # Отображение мишени и счета
    screen.blit(target_img, (target_x, target_y))
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()