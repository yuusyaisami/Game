import pygame
import Game
import Controller
pygame.init()
game = Game()
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
                
        game.update(screen)
        screen.fill((255, 255, 255))
        game.draw(screen)
        pygame.display.update()
        clock.tick(60)