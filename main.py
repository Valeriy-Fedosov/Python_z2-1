import pygame
import time
import random
import sqlite3
from snake import Snake
from apple import Apple
from par import *
from nic import *

# Инициализация Pygame
pygame.init()

# Основная функция игры
def game_loop(nickname):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Змейка')

    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()
    score = 0

    font_style = pygame.font.SysFont("Bad Script", 30)
    font_style1 = pygame.font.SysFont("Bad Script", 25)

    def display_score(score):
        value = font_style.render(f"Score: {score}", True, WHITE)
        screen.blit(value, [0, 0])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nickname = input_nickname() 
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                   snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')

        snake.move()

        # Проверка столкновения с яблоком
        if snake.positions[0] == apple.position:
            snake.grow_snake()
            apple.respawn()
            score += 1  # Увеличиваем счет

        # Проверка столкновения со стенами или собой
        head_x, head_y = snake.positions[0]
        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or snake.positions[0] in snake.positions[1:]):
            

            conn = sqlite3.connect('lider.db')
            cursor = conn.cursor()

            que_create = '''
                CREATE TABLE IF NOT EXISTS class (
                id INTEGER PRIMARY KEY,
                nicname NEXT,
                score INTEGER)
                '''
            
            # Проверим есть ли такая запись в базе данных, если есть, то ее обновим
            cursor.execute(f"SELECT nicname FROM Users WHERE nicname=(nicname)")

            # добавляем новую запись в таблицу users
            if cursor.fetchone() is None:
                cursor.execute('INSERT INTO users (nicname, score) VALUES (?, ?)', (nicname, score))
                cursor.close()
                conn.close()
            else:
                cursor.execute('UPDATE Users SET score = ? WHERE nicname = ?', ('nicname', score))
                cursor.close()
                conn.close()
                break

        screen.fill(BLUE)
        for pos in snake.positions:
            pygame.draw.rect(screen, GREEN, [pos[0], pos[1], SNAKE_BLOCK, SNAKE_BLOCK])
        
        pygame.draw.rect(screen, RED, [apple.position[0], apple.position[1], SNAKE_BLOCK, SNAKE_BLOCK])
        
        display_score(score)  # Отображаем счет
        
        # Отображаем никнейм
        nickname_surface = font_style.render(f"Nickname: {nickname}", True, WHITE)
        screen.blit(nickname_surface, [100, 0])

        # Отображение лидеров
        conn = sqlite3.connect('lider.db')
        cursor = conn.cursor()
        cursor.execute('SELECT nicname, score FROM Users ORDER BY score DESC')
        results = cursor.fetchall()
        for i in range(5):
             lider_surface = font_style1.render(f": {results[i]}", True, WHITE)
             screen.blit(lider_surface, [600, 18 * i])

        cursor.close()
        conn.close()

        
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    pygame.quit()

if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Змейка')
        
    nickname = input_nickname()  # Получаем никнейм
    
    if nickname:  
        game_loop(nickname)
        
