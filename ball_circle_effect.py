import pygame
import math
import random

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Reflection with Gaps and Ball Collision")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Circle parameters
circle_center = (width // 2, height // 2)
circle_radius = 200
gap_size = 10

# Ball parameters
ball_radius = 10
ball_speed = 3
balls = [{'pos': [width // 2, height // 2], 'dir': [random.uniform(-1, 1), random.uniform(-1, 1)]}]

# Normalize direction
for ball in balls:
    magnitude = math.sqrt(ball['dir'][0]**2 + ball['dir'][1]**2)
    ball['dir'][0] /= magnitude
    ball['dir'][1] /= magnitude

gaps = []

# Function to draw the circle with gaps
def draw_circle_with_gaps():
    angle_gap_list = []
    for gap in gaps:
        start_angle = gap['start_angle']
        end_angle = gap['end_angle']
        angle_gap_list.append((start_angle, end_angle))
        
    start_angle = 0
    for gap in sorted(angle_gap_list):
        pygame.draw.arc(screen, WHITE, (circle_center[0] - circle_radius, circle_center[1] - circle_radius, 2*circle_radius, 2*circle_radius), start_angle, gap[0], 1)
        start_angle = gap[1]
    pygame.draw.arc(screen, WHITE, (circle_center[0] - circle_radius, circle_center[1] - circle_radius, 2*circle_radius, 2*circle_radius), start_angle, 2 * math.pi, 1)

def check_collision_and_reflect(ball):
    dx = ball['pos'][0] - circle_center[0]
    dy = ball['pos'][1] - circle_center[1]
    distance_from_center = math.sqrt(dx**2 + dy**2)

    if distance_from_center + ball_radius >= circle_radius:
        angle_of_collision = math.atan2(dy, dx)
        start_angle = angle_of_collision - gap_size / (2 * circle_radius)
        end_angle = angle_of_collision + gap_size / (2 * circle_radius)
        gaps.append({'start_angle': start_angle, 'end_angle': end_angle})

        normal = [dx / distance_from_center, dy / distance_from_center]
        dot_product = ball['dir'][0] * normal[0] + ball['dir'][1] * normal[1]
        ball['dir'][0] -= 2 * dot_product * normal[0]
        ball['dir'][1] -= 2 * dot_product * normal[1]

        magnitude = math.sqrt(ball['dir'][0]**2 + ball['dir'][1]**2)
        ball['dir'][0] /= magnitude
        ball['dir'][1] /= magnitude

        new_ball = {
            'pos': [circle_center[0], circle_center[1]],
            'dir': [random.uniform(-1, 1), random.uniform(-1, 1)]
        }
        magnitude = math.sqrt(new_ball['dir'][0]**2 + new_ball['dir'][1]**2)
        new_ball['dir'][0] /= magnitude
        new_ball['dir'][1] /= magnitude

        balls.append(new_ball)

-def check_ball_collision(ball1, ball2):
    dx = ball1['pos'][0] - ball2['pos'][0]
    dy = ball1['pos'][1] - ball2['pos'][1]
    distance_between_balls = math.sqrt(dx**2 + dy**2)

    if distance_between_balls <= 2 * ball_radius: 
        normal = [dx / distance_between_balls, dy / distance_between_balls]

        dot_product1 = ball1['dir'][0] * normal[0] + ball1['dir'][1] * normal[1]
        ball1['dir'][0] -= 2 * dot_product1 * normal[0]
        ball1['dir'][1] -= 2 * dot_product1 * normal[1]

        dot_product2 = ball2['dir'][0] * normal[0] + ball2['dir'][1] * normal[1]
        ball2['dir'][0] -= 2 * dot_product2 * normal[0]
        ball2['dir'][1] -= 2 * dot_product2 * normal[1]

        for ball in [ball1, ball2]:
            magnitude = math.sqrt(ball['dir'][0]**2 + ball['dir'][1]**2)
            ball['dir'][0] /= magnitude
            ball['dir'][1] /= magnitude

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    draw_circle_with_gaps()

    for i, ball in enumerate(balls):
        pygame.draw.circle(screen, RED, (int(ball['pos'][0]), int(ball['pos'][1])), ball_radius)
        ball['pos'][0] += ball['dir'][0] * ball_speed
        ball['pos'][1] += ball['dir'][1] * ball_speed

        check_collision_and_reflect(ball)

        for j in range(i + 1, len(balls)):
            check_ball_collision(ball, balls[j])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
