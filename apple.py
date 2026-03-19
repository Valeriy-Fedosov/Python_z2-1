import random
from par import WIDTH, HEIGHT, SNAKE_BLOCK, SNAKE_SPEED

# Класс Яблоко
class Apple:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH - SNAKE_BLOCK) // SNAKE_BLOCK) * SNAKE_BLOCK,
                          random.randint(0, (HEIGHT - SNAKE_BLOCK) // SNAKE_BLOCK) * SNAKE_BLOCK)

    def respawn(self):
        self.position = (random.randint(0, (WIDTH - SNAKE_BLOCK) // SNAKE_BLOCK) * SNAKE_BLOCK,
                         random.randint(0, (HEIGHT - SNAKE_BLOCK) // SNAKE_BLOCK) * SNAKE_BLOCK)
