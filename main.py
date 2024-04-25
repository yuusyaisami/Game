import pygame
from Game import Game
from Controller import controller
pygame.init()
game = Game.Game("Scene/MenuScene") # 読み込むファイルの名前を入力する
def main():
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    while True:
        controller.update(pygame.event.get())
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