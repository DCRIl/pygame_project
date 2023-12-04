import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = screen.get_size()
running = True
x = 0
circle_xy = [0.5 * w - 20, 0.8 * h - 20]
clock = pygame.time.Clock()
FALL = pygame.USEREVENT + 1
pygame.time.set_timer(FALL, 1)
motionx1 = "STOP"
motionx2 = "STOP"
motiony1 = "STOP"
motiony2 = "STOP"
object = [0.1 * w, 0.4 * h, 0.1 * w, 0.4 * h]
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                motionx1 = "LEFT"
            if event.key == pygame.K_a:
                motionx2 = "RIGHT"
            if (event.key == pygame.K_w or event.key == pygame.K_SPACE) and x == 0:
                x = 10
            if event.key == pygame.K_s:
                motiony2 = "DOWN"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                motionx1 = "STOP"
            if event.key == pygame.K_a:
                motionx2 = "STOP"
            if event.key == pygame.K_s:
                motiony2 = "STOP"
        if event.type == FALL:
            if circle_xy[1] < 0.8 * h - 20:
                circle_xy[1] += 1
    if motionx1 == "LEFT":
        circle_xy[0] += 5
    if motionx2 == "RIGHT":
        circle_xy[0] -= 5
    if x > 0:
        circle_xy[1] -= 10
        x -= 0.5
    if motiony2 == "DOWN":
        circle_xy[1] += 5
    if circle_xy[0] < 0.3 * w:
        circle_xy[0] += 5
        object[0] += 5
    if circle_xy[0] > 0.7 * w:
        circle_xy[0] -= 5
        object[0] -= 5
    if circle_xy[1] < 0.3 * h:
        circle_xy[1] += 5
        object[1] += 5
    if circle_xy[1] > 0.9 * h:
        circle_xy[1] -= 5
        object[1] -= 5
    pygame.draw.rect(screen, "white", (0, 0.8 * h, w, 0.2 * h))
    pygame.draw.rect(screen, "white", object)
    pygame.draw.circle(screen, "red", circle_xy, 20)
    pygame.draw.rect(screen, "green", (0.3 * w, 0.3 * h, 0.4 * w, 0.6 * h), 2)
    clock.tick(120)
    pygame.display.flip()
pygame.quit()