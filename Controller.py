import pygame
class Controller:
    def __init__(self, ):
        self.event = None
        self.stute = {"w": False, "a": False, "s": False, "d": False, "esc": False, 
                      "space": False, "enter": False, "tab": False, "backspace": False,
                      "click": False, "click_right": False, "click_left": False,
                      }
    def update(self, event):
        self.event = event
        stute = {"w": False, "a": False, "s": False, "d": False, "esc": False,
                "space": False, "enter": False, "tab": False, "backspace": False,
                 "click": False, "click_right": False, "click_left": False,}
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
    def get_keydown(self):
        """ keyname is a string representing"""
        self.stute = {"w": False, "a": False, "s": False, "d": False, "esc": False, "space": False, "enter": False, "tab": False, "backspace": False}
        for event in self.event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.stute["w"] = True
                elif event.key == pygame.K_s:
                    self.stute["s"] = True
                elif event.key == pygame.K_a:
                    self.stute["a"] = True
                elif event.key == pygame.K_d:
                    self.stute["d"] = True
                elif event.key == pygame.K_ESCAPE:
                    self.stute["esc"] = True
                elif event.key == pygame.K_SPACE:
                    self.stute["space"] = True
                elif event.key == pygame.K_RETURN:
                    self.stute["enter"] = True
                elif event.key == pygame.K_TAB:
                    self.stute["tab"] = True
                elif event.key == pygame.K_BACKSPACE:
                    self.stute["backspace"] = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                if buttons[0]:
                    self.stute["click_right"] == True
                self.stute["click"] = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.stute["click_right"]
    def get_click(self, number = -1):
        if number == -1:
            for self.event in self.event
            if self.event.type == pygame.MOUSEBUTTONDOWN and self.
controller = Controller()