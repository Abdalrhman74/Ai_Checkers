import time

import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, WHITE
from game import Game
from minimax import minimax, minimax2

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def draw_menu(win, font, selected_option):
    win.fill((0, 0, 0))
    if selected_option == 0:
        option_texts = ['Easy']
    elif selected_option == 1:
        option_texts = ['Medium']
    elif selected_option == 2:
        option_texts = ['Hard']

    for idx, option_text in enumerate(option_texts):
        text = font.render(option_text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50 + idx * 50))
        win.blit(text, text_rect)
    pygame.display.update()


def menu_screen():
    run = True
    selected_option = 0
    pygame.font.init()
    font = pygame.font.SysFont(None, 48)

    while run:
        draw_menu(WIN, font, selected_option)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % 3
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % 3
                elif event.key == pygame.K_RETURN:
                    run = False
            if event.type == pygame.QUIT:
                run = False
                selected_option = -1

    return selected_option

counter1 = 0

def main():
    counter = 0
    menu_option = menu_screen()
    if menu_option == -1:
        pygame.quit()
        return
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    # initialize Pygame's font module
    pygame.font.init()
    # create a Pygame font object for displaying text
    font = pygame.font.SysFont(None, 48)

    while run:
        clock.tick(FPS)
        game.turn = BLACK
        if game.turn is not None:
            # Use the selected algorithm and difficulty level
            time.sleep(0.5)
            if menu_option == 0:
                value, new_board = minimax2(game.get_board(), 1, game.turn, game)
            elif menu_option == 1:
                value, new_board = minimax2(game.get_board(), 1, game.turn, game)
            elif menu_option == 2:
                value, new_board = minimax2(game.get_board(), 1, game.turn, game)
            game.ai_move(new_board)
        game.update()
        game.turn = WHITE
        counter += 1
        if game.turn is not None:
            time.sleep(0.5)
            # Use the selected algorithm and difficulty level
            if menu_option == 0:
                value, new_board = minimax(game.get_board(), 1, float('-inf'), float('inf'), game.turn, game)
            elif menu_option == 1:
                value, new_board = minimax(game.get_board(), 3, float('-inf'), float('inf'), game.turn, game)
            elif menu_option == 2:
                value, new_board = minimax(game.get_board(), 4, float('-inf'), float('inf'), game.turn, game)
            game.ai_move(new_board)
        game.update()

        # check if there is a winner
        winner = game.winner()

        if game.no_valid_moves_left(BLACK):
            winner = WHITE
        elif game.no_valid_moves_left(WHITE):
            winner = BLACK
        else:
            winner = None

        if winner is not None:
            if winner == BLACK:
                # create a text object to display the winner's color
                text = font.render(f"BLACK WINS !", True, (255, 255, 255))
                text_rect = text.get_rect(center=WIN.get_rect().center)
                WIN.blit(text, text_rect)
                pygame.display.update()
                time.sleep(2)
                return False
            elif winner == WHITE:
                text = font.render(f"WHITE WINS !", True, (255, 255, 255))
                text_rect = text.get_rect(center=WIN.get_rect().center)
                WIN.blit(text, text_rect)
                pygame.display.update()
                time.sleep(2)
                return False
            elif winner == "DRAW":
                text = font.render(f"draw !", True, (255, 255, 255))
                text_rect = text.get_rect(center=WIN.get_rect().center)
                WIN.blit(text, text_rect)
                pygame.display.update()
                time.sleep(2)
                return False
            else:
                continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    time.sleep(1.5)
    pygame.display.update()
    pygame.quit()

main()