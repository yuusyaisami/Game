import importlib

# ロードし描写するときの各モジュールには必ず各クラスのSceneクラスをmainにすること
# Sceneクラスはupdate関数とdraw関数を必要とする

class Scene: 
    def __init__(self):
        self.scene = [] # 描写するクラスを入れる example( Main() Level1() )
    def LoadScene(self, loadFile, loadClassName):
        self.scene = []
        module_name = f"{loadFile}"
        module = importlib.import_module(module_name)
        self.scene.append(module.Scene())
