import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tennis Game")

# Colors
ball_color = (255, 255, 255)  # White
player_color = (255, 255, 255)  # White
circle_color = (255, 255, 255)  # White
line_color = (255, 255, 255)  # White

# Ball properties
ball_radius = 10
ball_pos = [window_width // 2, window_height // 2]
ball_speed = [4, 4]

# Player properties
player_width = 10
player_height = 50
player_speed = 5
player_1_pos = [10, window_height // 2 - player_height // 2]
player_2_pos = [window_width - 20, window_height // 2 - player_height // 2]

circle_radius = 80
circle_pos = [window_width // 2, window_height // 2]

line_width = 2
line_start = [window_width // 2, 0]
line_end = [window_width // 2, window_height]

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

# Initialize the scores
player_1_score = 0
player_2_score = 0

# Game loop
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

    if ball_pos[0] <= 0:
        player_2_score += 1
        ball_pos = [window_width // 2, window_height // 2]
        ball_speed = [3, 3]
    if ball_pos[0] >= window_width:
        player_1_score += 1
        ball_pos = [window_width // 2, window_height // 2]
        ball_speed = [3, 3]

    window.fill((0, 0, 0))
    pygame.draw.circle(window, ball_color, ball_pos, ball_radius)
    pygame.draw.rect(window, player_color, pygame.Rect(player_1_pos[0], player_1_pos[1], player_width, player_height))
    pygame.draw.rect(window, player_color, pygame.Rect(player_2_pos[0], player_2_pos[1], player_width, player_height))
    pygame.draw.circle(window, circle_color, circle_pos, circle_radius, 2)
    pygame.draw.line(window, line_color, line_start, line_end, line_width)

    score_text = font.render(f"{player_1_score} - {player_2_score}", True, (255, 255, 255))
    window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
