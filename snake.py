import pygame
import random
import os
from pygame.locals import *

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

        self.image_positions = [(random.randint(0, self.screen_width - 50), random.randint(0, self.screen_height - 50)) for _ in self.images]
        self.image_timers = [pygame.time.get_ticks() + random.randint(5000, 15000) for _ in self.images]
        self.active_images = [False] * len(self.images)

    def load_image(self, path, width, height):
        try:
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, (width, height))
            return image
        except pygame.error as e:
            print(f"Unable to load image at {path}: {e}")
            return None

    def block_drawer(self):
        self.surface.blit(self.background_image, (0, 0))
        self.surface.blit(self.block, (self.block_x, self.block_y))
        current_time = pygame.time.get_ticks()
        for i, image in enumerate(self.images):
            if image and self.active_images[i]:
                self.surface.blit(image, self.image_positions[i])
            elif current_time >= self.image_timers[i]:
                self.active_images[i] = True
                self.surface.blit(image, self.image_positions[i])
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

            block_rect = self.block.get_rect(topleft=(self.block_x, self.block_y))
            for i, pos in enumerate(self.image_positions):
                if self.active_images[i]:
                    image_rect = self.images[i].get_rect(topleft=pos)
                    if self.check_collision(block_rect, image_rect):
                        print(f"Collision detected with image {i} at position {pos}!")
                        self.active_images[i] = False
                        self.image_timers[i] = pygame.time.get_ticks() + random.randint(5000, 15000)  # Reset timer for reappearance

            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()
        quit()

if __name__ == "__main__":
    game = Game()
    game.run()
