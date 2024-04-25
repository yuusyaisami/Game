from Scene import scene
from Graphic import graphic
from SceneBase import SceneBase
import Item
class main(SceneBase):
    def __init__(self):
        super().__init__()
        self.UI = [
            Item.Text((300, 200, 100, 32), "main_title", 32, (128, 128, 128), True),
            Item.Button((125, 300, 100, 50), "click_me", 32, (128, 128, 128), True),
        ]
    def update(self):
        for item in self.UI:
            item.update()
    def draw(self):
        for item in self.UI:
            item.draw()