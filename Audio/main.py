import pygame

pygame.init()
pygame.mixer.init()

Window = (800, 600)

pygame.display.set_mode(Window)

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
