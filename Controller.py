import pygame
class Controller:
    def __init__(self, ):
        self.event = None
        self.stute_all_clear()
    def stute_all_clear(self):
        self.stute = {"w": False, "a": False, "s": False, "d": False, "esc": False, 
                      "space": False, "enter": False, "tab": False, "backspace": False,
                      "click": False, "click_right": False, "click_left": False,
                      "hold_click": False, "hold_click_right": False, "hold_click_left": False,
                      "up_click": False, "up_click_right": False, "up_click_left": False
                      }
    def update(self, event):
        self.event = event
        self.stute_all_clear()
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
                    self.stute["click_left"] == True
                    self.stute["click"] = True
                if buttons[2]:
                    self.stute["click_right"] == True
                    self.stute["click"] = True
            if event.type == pygame.MOUSEBUTTONUP:
                buttons = pygame.mouse.get_pressed()
                if buttons[0]:
                    self.stute["up_click_left"] = True
                    self.stute["up_click"] = True
                if buttons[2]:
                    self.stute["up_click_right"] = True
                    self.stute["up_click"] = True

    def get_keydown(self, key) -> bool:
        """ keyname is a string representing"""
        try:
            return self.stute[key]
        except:
            print(f"{key}は存在しません")
            return False
    def get_click(self, name = "click_left"):
        try:
            return self.stute[name]
        except:
            print(f"{name}は存在しません")
            return False
    def collision_mouse(self, rect):
        return rect.collidepoint(pygame.mouse.get_pos())
    def collition_rect(self, rect1, rect2):
        return rect1.colliderect(rect2)
controller = Controller()