import importlib
import threading
import sys
# ロードし描写するときの各モジュールには必ず各クラスのSceneクラスをmainにすること
# Sceneクラスはupdate関数とdraw関数を必要とする

class Scene: 
    def __init__(self):
        self.scene = [] # 描写するクラスを入れる example( Main() Level1() )
    def LoadScene(self, loadFile):
        """描写するファイルの名前をloadFileに入れる(.pyは抜き、ファイルには必ずMainクラスまたはmainクラスが存在することを条件とする)"""
        self.scene = []
        module_name = loadFile
        sys.path
        module = importlib.import_module(module_name)
        try:
            self.scene.append(module.Main())
        except:
            try:
                self.scene.append(module.main())
            except:
                print(f"ファイル{loadFile}.main()の読み込みに失敗しました")
                exit()
    def update(self):
        for scene in self.scene:
            scene.update()
    def draw(self):
        for scene in self.scene:
            scene.draw()
scene = Scene()