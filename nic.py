import pygame
from par import *
#

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Функция для ввода никнейма
def input_nickname():
    nickname = ''
    input_active = True
    font_style = pygame.font.SysFont("bahnschrift", 25)
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Нажатие Enter завершает ввод
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:  # Удаление символа
                    nickname = nickname[:-1]
                else:
                    nickname += event.unicode  # Добавление символа

        screen.fill(BLUE)
        text_surface = font_style.render(f"Ведите nickname: {nickname}", True, WHITE)
        screen.blit(text_surface, [WIDTH // 6, HEIGHT // 3])
        
        pygame.display.update()

    return nickname
