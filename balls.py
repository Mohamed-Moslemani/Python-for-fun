import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x = -self.speed_x
            return True  
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y = -self.speed_y
            return True  
        return False

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def main():
    clock = pygame.time.Clock()
    balls = [Ball(WIDTH // 2, HEIGHT // 2, 20, 5, 5, random_color())]  

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        new_balls = []
        for ball in balls:
            if ball.move():  
                new_balls.append(Ball(ball.x, ball.y, ball.radius, -ball.speed_x, ball.speed_y, random_color()))
                new_balls.append(Ball(ball.x, ball.y, ball.radius, ball.speed_x, -ball.speed_y, random_color()))
            ball.draw()

        balls.extend(new_balls)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
