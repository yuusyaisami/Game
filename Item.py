from Controller import controller
from Scene import scene
import Graphic
import pygame
class Item:
    def __init__(self, rect, type, color, s_hover = False, order = -1): # rect type colorは必須引数
        self.rect = rect
        self.type = type
        self.color = color
        self.def_color = color
        self.s_hover = s_hover
        self.order = order
    def update(self):
        if self.s_hover:
            if self.hover():
                self.set_hover_color(30)
            else:
                self.reset_hover_color()
    def clicked(self ) -> bool:
        if controller.get_click():
            return controller.collision_mouse(self.rect)
    def hover(self) -> bool:
        return controller.collision_mouse(self.rect)
    def set_hover_color(self, downvalue): # このプログラム嫌い
        r, g, b = self.def_color
        r = r - downvalue
        g = g - downvalue
        b = b - downvalue
        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0
        self.color = (r, g, b)
    def reset_hover_color(self):
        self.color = self.def_color
    def background(self):
        pass # 必要なitemのみ使用する
class Text(Item):
    def __init__(self, rect, text, text_size, color,s_hover,  order = -1):
        super().__init__(rect, "text", color,s_hover,  order)
        self.text = text
        self.font = "Sans"
        self.size = text_size
    def draw(self):
        Graphic.graphic.add_layer(Graphic.Text(self.rect, self.text, self.color, self.size ), self.order)

class CheckBox(Item):
    def __init__(self, rect, text, color, checked = False, order = -1):
        super().__init__(rect, "checkbox",color, True,order)
        self.text = text
        self.checked = checked
    def update(self):
        if self.clicked():
            self.checked = not self.checked
    def draw(self):
        if not self.checked:
            Graphic.graphic.add_layer(Graphic.Square(self.rect, self.color ,-5, 5), self.order)
        else:
            Graphic.graphic.add_Layer(Graphic.Square(self.rect, self.color, -5, 0), self.order)
class Button(Item):
    def __init__(self, rect, text, text_size, color, s_hover, order=-1):
        super().__init__(rect, "button", color, s_hover=s_hover, order=order)
        self.text = text
        self.font = "Sans"
        self.size = text_size
    def draw(self):
        Graphic.graphic.add_layer(Graphic.Square(self.rect, self.color ,-5, 5), self.order)
        Graphic.graphic.add_layer(Graphic.Text(self.rect, self.text, self.color, self.size ), self.order)