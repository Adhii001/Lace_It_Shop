import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario Clone")

# Player class
class Player(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5
        self.jump_power = 10
        self.gravity = 0.5
        self.velocity_y = 0
        self.on_ground = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -self.jump_power
            self.on_ground = False

        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Check if on the ground
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.on_ground = True
            self.velocity_y = 0

# Platform class
class Platform(pygame.sprite.Sprite):
    def _init_(self, x, y, width, height):
        super()._init_()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Main game loop
def main():
    clock = pygame.time.Clock()
    player = Player()
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()

    all_sprites.add(player)

    # Create platforms
    platform1 = Platform(100, 500, 200, 20)
    platform2 = Platform(400, 400, 200, 20)
    platform3 = Platform(200, 300, 200, 20)

    platforms.add(platform1, platform2, platform3)
    all_sprites.add(platform1, platform2, platform3)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game logic
        all_sprites.update()

        # Check for collisions
        hits = pygame.sprite.spritecollide(player, platforms, False)
        if hits:
            player.rect.bottom = hits[0].rect.top
            player.on_ground = True
            player.velocity_y = 0

        # Draw everything
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Ensure the script runs directly
if __name__ == "_main_":
    main()