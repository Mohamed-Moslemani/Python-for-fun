import pygame
import time
import random
from pygame.locals import *
import os

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        
        self.background_image = self.load_image("src/bg.jpg", self.screen_width, self.screen_height)
        self.block = self.load_image("src/block.png", 50, 50)
        self.block_x, self.block_y = 100, 100

        excluded_files = {"block.png", "bg.jpg"}
        images_paths = [os.path.join('src', file) for file in os.listdir("src") if file not in excluded_files]
        self.images = [self.load_image(image_path, 50, 50) for image_path in images_paths]

    def load_image(self, path, width, height):
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, (width, height))
        return image

    def block_drawer(self):
        self.surface.blit(self.background_image, (0, 0))
        self.surface.blit(self.block, (self.block_x, self.block_y))
        pygame.display.flip()

    def check_collision(self, rect1, rect2):
        return rect1.colliderect(rect2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_UP:
                    self.block_y -= 10
                elif event.key == pygame.K_LEFT:
                    self.block_x -= 10
                elif event.key == pygame.K_RIGHT:
                    self.block_x += 10
                elif event.key == pygame.K_DOWN:
                    self.block_y += 10
        return True

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.block_drawer()
            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()
        quit()

if __name__ == "__main__":
    game = Game()
    game.run()
