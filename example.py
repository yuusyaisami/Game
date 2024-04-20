# サンプルコード
# Gameのインスタンスをwhile文(繰り返し)の中で実行する
# updateとdraw関数を実行してください
import pygame
from Game import Game
from Controller import Controller
pygame.init()
game = Game.Game("example_scene") # 読み込むファイルの名前を入力する
controller = Controller()
def main():
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    key_state_dict = {}
    while True:
        controller.update(pygame.event.get())
        key_state_dict = controller.get_keydown()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        game.update()
        screen.fill((255, 30, 30))
        game.draw(screen)
        pygame.display.update()
        clock.tick(60)
main()