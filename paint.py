import pygame

pygame.init()

run = True
new = pygame.mouse.get_pos()
two = pygame.mouse.get_pos()
color = (0, 0, 0)
rad = 1
press = False

sc = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Paint")
pygame.display.set_icon(pygame.image.load(r"Game\icons\13.png"))

sc.fill((255, 255, 255))

while run:
    pygame.time.delay(50)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                press = True
                rad = 1
                color = (0, 0, 0)
            if i.button == 3:
                press = True
                color = (255, 255, 255)
                rad = 15
            if i.button == 2:
                sc.fill((255, 255, 255))
                pygame.display.update()
        if i.type == pygame.MOUSEBUTTONUP:
            if i.button == 1:
                press = False
            if i.button == 3:
                press = False

    two = pygame.mouse.get_pos()

    if pygame.mouse.get_focused():
        if press:
            pygame.draw.line(sc, color, new, two, rad)

    new = two

    pygame.display.update()

pygame.quit()
