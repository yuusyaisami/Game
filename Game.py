import Graphic
import Scene
import threading
class Game:
    def __init__(self, initScene = None):
        self.graphic = Graphic.graphic # 参照
        self.scene = Scene.scene
        self.thread = threading.Thread(target=self.background)
        if initScene:
            self.scene.LoadScene(initScene)
    def update(self):
        self.scene.update()
    def background(self):
        self.scene.background()
    def draw(self, scene):
        self.scene.draw()
        self.graphic.draw(scene)