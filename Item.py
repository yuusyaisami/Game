from Controller import controller
import Graphic
import pygame
class Item:
    def __init__(self, rect, type):
        self.rect = rect
        self.type = type
    def clicked(self ) -> bool:
        controller.get_keydown()
class Text(Item):
    def __init__(self, rect, text, color):
        super().__init__(rect, "text")
        self.text = text
        self.color = color
        self.font = "Sans"
        self.size = 32
    def draw(self):
        Graphic.graphic.add_layer(Graphic.Text(self.rect, self.text, self.color, self.size ), )