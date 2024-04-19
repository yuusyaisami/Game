import pygame
class Controller:
    def __init__(self, ):
        self.event = None
    def update(self, event):
        self.event = event
    def get_keydown(self):
        """ keyname is a string representing"""
        stute = {"w": False, "a": False, "s": False, "d": False, "esc": False, "space": False, "enter": False, "tab": False, "backspace": False}
        for event in self.event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    stute["w"] = True
                elif event.key == pygame.K_s:
                    stute["s"] = True
                elif event.key == pygame.K_a:
                    stute["a"] = True
                elif event.key == pygame.K_d:
                    stute["d"] = True
                elif event.key == pygame.K_ESCAPE:
                    stute["esc"] = True
                elif event.key == pygame.K_SPACE:
                    stute["space"] = True
                elif event.key == pygame.K_RETURN:
                    stute["enter"] = True
                elif event.key == pygame.K_TAB:
                    stute["tab"] = True
                elif event.key == pygame.K_BACKSPACE:
                    stute["backspace"] = True
        return stute