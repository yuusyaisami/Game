import Graphic
import Scene
class Game:
    def __init__(self, initScene = None):
        self.graphic = Graphic.graphic # 参照
        self.scene = Scene.Scene()
        if initScene:
            self.scene.LoadScene(initScene)
    def update(self):
        self.scene.update()
    def draw(self, scene):
        self.scene.draw()
        self.graphic.draw(scene)