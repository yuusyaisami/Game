from Scene import scene
from Graphic import graphic
from SceneBase import SceneBase
import Item
import pygame
class main(SceneBase):
    def __init__(self):
        super().__init__()
        self.UI = [
            Item.Text(pygame.Rect(300, 200, 100, 50), "main_title", 32, (128, 128, 128), True),
            Item.Button(pygame.Rect(300, 300, 150, 100), "click_me", 32, (128, 128, 128), True),
        ]
    def update(self):
        for item in self.UI:
            item.update()
    def draw(self):
        for item in self.UI:
            item.draw()