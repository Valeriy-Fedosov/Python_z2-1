from par import WIDTH, HEIGHT, SNAKE_BLOCK, SNAKE_SPEED 

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = 'RIGHT'
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        if self.direction == 'UP':
            head_y -= SNAKE_BLOCK
        elif self.direction == 'DOWN':
            head_y += SNAKE_BLOCK
        elif self.direction == 'LEFT':
            head_x -= SNAKE_BLOCK
        elif self.direction == 'RIGHT':
            head_x += SNAKE_BLOCK

        new_head = (head_x, head_y)
        self.positions.insert(0, new_head)

        if not self.grow:
            self.positions.pop()
        else:
            self.length += 1
            self.grow = False

    def change_direction(self, new_direction):
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True
