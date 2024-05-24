import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра ТИР")

icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")


running = True
while running:
     pass

pygame.quit()
