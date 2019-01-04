import pygame

pygame.init()

window_width = 800
window_height = 500

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gatcha Game")

clock = pygame.time.Clock()

back = pygame.image.load("background.jpg")

run = False

while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    window.blit(back, (0,0))
    pygame.display.update()