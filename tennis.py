import pygame

# Initialize Pygame
pygame.init()

window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tennis Game")

ball_radius = 10
ball_color = (255, 255, 255)  # White
player_1 = (255, 255, 255)  # White
player_2 = (255, 255, 255)  # White
player_1_pos = (10, window_height // 2)
player_2_pos = (window_width - 10, window_height // 2)
ball_speed = [1, 1]

ball_pos = (window_width // 2, window_height // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    window.fill((0, 0, 0)) 
    pygame.draw.circle(window, ball_color, ball_pos, ball_radius)
    pygame.draw.rect(window, player_1, pygame.Rect(player_1_pos[0], player_1_pos[1], 10, 50))
    pygame.draw.rect(window, player_2, pygame.Rect(player_2_pos[0], player_2_pos[1], 10, 50))
    ball_pos = (ball_pos[0] + ball_speed[0], ball_pos[1] + ball_speed[1])
    if ball_pos[1] <= 0 or ball_pos[1] >= window_height:
        ball_speed[1] = -ball_speed[1]
    if ball_pos[0] <= 0 or ball_pos[0] >= window_width:
        ball_speed[0] = -ball_speed[0]
    


    pygame.display.flip()

pygame.quit()