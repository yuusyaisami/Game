from Graphic import graphic # Mainファイルのgameを読み込むのではなく、Graphic.pyのgraphicを読み込んでください
from Graphic import Square # add_layerに追加するクラス
import pygame
class main():
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        graphic.add_layer(Square(pygame.Rect(100, 100, 100, 100), (255, 255, 255), 5), 0)
    