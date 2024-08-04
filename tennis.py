import pygame

# Initialize Pygame
pygame.init()

window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tennis Game")

ball_radius = 10
ball_color = (255, 255, 255)  # White
player_1_color = (255, 255, 255)  # White
player_2_color = (255, 255, 255)  # White
player_1_pos = [10, window_height // 2 - 25]
player_2_pos = [window_width - 20, window_height // 2 - 25]
ball_speed = [3, 3]

ball_pos = [window_width // 2, window_height // 2]

player_speed = 5
player_height = 50
player_width = 10
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    # Player 1 movement
    if keys[pygame.K_UP] and player_1_pos[1] > 0:
        player_1_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_1_pos[1] < window_height - player_height:
        player_1_pos[1] += player_speed
    
    # Player 2 movement
    if keys[pygame.K_e] and player_2_pos[1] > 0:
        player_2_pos[1] -= player_speed
    if keys[pygame.K_d] and player_2_pos[1] < window_height - player_height:
        player_2_pos[1] += player_speed

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]
    
    # Ball collision with top and bottom walls
    if ball_pos[1] <= 0 or ball_pos[1] >= window_height:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddles
    if (ball_pos[0] - ball_radius <= player_1_pos[0] + player_width and
        player_1_pos[1] <= ball_pos[1] <= player_1_pos[1] + player_height):
        ball_speed[0] = -ball_speed[0]

    if (ball_pos[0] + ball_radius >= player_2_pos[0] and
        player_2_pos[1] <= ball_pos[1] <= player_2_pos[1] + player_height):
        ball_speed[0] = -ball_speed[0]

    # Ball collision with left and right walls
    if ball_pos[0] <= 0 or ball_pos[0] >= window_width:
        ball_pos = [window_width // 2, window_height // 2]  # Reset the ball position
        ball_speed = [3, 3]  # Reset the ball speed

    window.fill((0, 0, 0))
    pygame.draw.circle(window, ball_color, ball_pos, ball_radius)
    pygame.draw.rect(window, player_1_color, pygame.Rect(player_1_pos[0], player_1_pos[1], player_width, player_height))
    pygame.draw.rect(window, player_2_color, pygame.Rect(player_2_pos[0], player_2_pos[1], player_width, player_height))

    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 frames per second

pygame.quit()
