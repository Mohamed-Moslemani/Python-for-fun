import pygame
import random
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (0, 0, 0)
FPS = 60
MAX_BALLS = 100  # Maximum number of balls to prevent crashes

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing and Multiplying Balls - 3D Look")

# Ball class
class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        self.just_split = False  # Flag to prevent immediate splitting

        # Create a surface for the ball with per-pixel alpha
        self.surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.draw_3d_ball()

    def draw_3d_ball(self):
        # Draw a circle with radial gradient to simulate 3D effect
        for i in range(self.radius * 2):
            for j in range(self.radius * 2):
                # Calculate distance from center
                dx = i - self.radius
                dy = j - self.radius
                distance = math.hypot(dx, dy)
                if distance <= self.radius:
                    # Calculate shading based on distance
                    shading = max(0, min(255, int(255 * (1 - distance / self.radius))))
                    r = min(255, self.color[0] + shading)
                    g = min(255, self.color[1] + shading)
                    b = min(255, self.color[2] + shading)
                    alpha = max(0, min(255, int(255 * (1 - (distance / self.radius)))))
                    self.surface.set_at((i, j), (r, g, b, alpha))

    def move(self):
        # Move the ball
        self.x += self.speed_x
        self.y += self.speed_y

        # Reset the just_split flag after moving
        if self.just_split:
            self.just_split = False

        # Check collision with walls
        hit_wall = False

        # Left or Right wall
        if self.x - self.radius <= 0:
            self.x = self.radius  # Adjust position
            self.speed_x = abs(self.speed_x)  # Ensure speed is positive
            hit_wall = True
        elif self.x + self.radius >= WIDTH:
            self.x = WIDTH - self.radius  # Adjust position
            self.speed_x = -abs(self.speed_x)  # Ensure speed is negative
            hit_wall = True

        # Top or Bottom wall
        if self.y - self.radius <= 0:
            self.y = self.radius  # Adjust position
            self.speed_y = abs(self.speed_y)  # Ensure speed is positive
            hit_wall = True
        elif self.y + self.radius >= HEIGHT:
            self.y = HEIGHT - self.radius  # Adjust position
            self.speed_y = -abs(self.speed_y)  # Ensure speed is negative
            hit_wall = True

        return hit_wall

    def draw(self, screen):
        # Blit the pre-rendered 3D ball surface onto the screen
        screen.blit(self.surface, (int(self.x - self.radius), int(self.y - self.radius)))

# Function to generate random color
def random_color():
    # Ensure colors are not too dark for better visibility
    return (
        random.randint(100, 255),
        random.randint(100, 255),
        random.randint(100, 255)
    )

# Function to generate random speed avoiding zero
def random_speed():
    return random.choice([-5, -4, -3, 3, 4, 5])

# Main game loop
def main():
    clock = pygame.time.Clock()

    # Start with one ball
    balls = [Ball(WIDTH // 2, HEIGHT // 2, 20, random_speed(), random_speed(), random_color())]

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        new_balls = []  # To hold new balls created when a ball hits a wall

        # Iterate over the balls list
        for ball in balls[:]:
            hit_wall = ball.move()
            if hit_wall and not ball.just_split:
                # Prevent adding new balls if maximum is reached
                if len(balls) + len(new_balls) < MAX_BALLS:
                    # Create two new balls at the position of the original ball
                    new_ball1 = Ball(
                        ball.x,
                        ball.y,
                        ball.radius,
                        random_speed(),
                        random_speed(),
                        random_color()
                    )
                    new_ball2 = Ball(
                        ball.x,
                        ball.y,
                        ball.radius,
                        random_speed(),
                        random_speed(),
                        random_color()
                    )
                    # Set just_split flag to prevent immediate re-splitting
                    new_ball1.just_split = True
                    new_ball2.just_split = True

                    new_balls.extend([new_ball1, new_ball2])
                # Remove the original ball
                balls.remove(ball)
                continue  # Skip drawing the original ball

            ball.draw(screen)

        # Update the list of balls
        balls.extend(new_balls)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
