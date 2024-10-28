import pygame
import math

pygame.init()

screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Rolling Square")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

square_size = 100
angle = 0 
angular_speed = 2  

center_x, center_y = screen_size[0] // 2, screen_size[1] // 2

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    corners = []
    for i in range(4):
        theta = math.radians(angle + i * 90)
        x = center_x + square_size / 2 * math.cos(theta)
        y = center_y + square_size / 2 * math.sin(theta)
        corners.append((x, y))

    pygame.draw.polygon(screen, BLUE, corners)

    angle += angular_speed
    if angle >= 360:
        angle -= 360

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
