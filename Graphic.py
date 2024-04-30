import pygame
pygame.init()
class Graphic:
    """Graphicのメインクラス Game.pyに存在します"""
    def __init__(self):
        self.img = {} # imageの名前はファイルの名前と同じにする 違っても問題はない
        self.font = {}
        self.font["Sans32"] = (pygame.font.SysFont("Sans.otf", 32))

        self.layer = []
    def add_layer(self, Layers_class, order):
        """Add a new layer , Layer_class : Image, Text, Square and so on"""
        Layers_class.order = order
        self.layer.append(Layers_class)
    def add_img(self, img_name, img_path, w = -1):
        if img_name not in self.img:
            if w == -1:
                self.img[img_name] = pygame.image.load(img_path)
            else:
                self.img[img_name] = pygame.transform.scale(pygame.image.load(img_path), (w, h))
    def get_font(self, name, size):
        for font in self.font:
            if font == name + str(size):
                return self.font[font]
        self.font[font.name + str(size)] = pygame.font.SysFont(font.name + ".otf", size)
        return self.font[font.name + str(size)]
    def draw(self, screen):
        max = 0
        for m in range(len(self.layer)):
            if self.layer[m].order > max:
                max = self.layer[m].order
        for i in range(max + 1):
            self.__drawLayer__(i, screen)
        self.__drawLayer__(-1, screen)
        self.layer = []
    def __drawLayer__(self, order, screen):
        for layer in self.layer:
            if layer.order == order:
                # -------------------------------------------クラスの描写----------------------------------------------------------- #
                if layer.type == "image":
                    screen.blit(self.img[layer.img_name], (layer.rect.x, layer.rect.y))
                if layer.type == "text":
                    x = layer.rect.x
                    y = layer.rect.y
                    if layer.set_center:
                        font = self.get_font(layer.text_font, layer.text_size)
                        x = layer.rect.center[0] - (font.size(layer.text)[0] / 2)
                        y = layer.rect.center[1] - (font.size(layer.text)[1] / 2)
                        screen.blit(self.get_font(layer.text_font, layer.text_size).render(layer.text, True, layer.color), (x, y))
                if layer.type == "square":
                    pygame.draw.rect(screen, layer.color, layer.rect, layer.width, layer.radius)
                if layer.type == "circle":
                    pygame.draw.circle(screen, layer.color, layer.rect.center, layer.radius, layer.width)
                # ----------------------------------------------------------------------------------------------------------------- # 
    def clear_img(self):
        self.img = {}
# --------------Layerのベースクラス-------------------
class Layer:
    def __init__(self, rect, order=-1):
        self.rect = rect
        self.order = order
#-----------------------------------------------------


#---------------------Layerクラス----------------------
class Image(Layer):
    def __init__(self, rect, img_name, ):
        super().__init__(rect)
        self.type = "image"
        self.img_name = img_name
class Text(Layer):
    def __init__(self, rect, text, color = (0, 0, 0), text_size = 16, text_font = "Sans", set_center = False):
        super().__init__(rect)
        self.type = "text"
        self.text = text
        self.text_size = text_size
        self.text_font = text_font
        self.color = color
        self.set_center = set_center
class Square(Layer):
    def __init__(self, rect, color, radius = -1, width = 0):
        super().__init__(rect)
        self.type = "square"
        self.color = color
        self.radius = radius
        self.width = width
class circle(Layer):
    def __init__(self, rect, color, radius = -1, width = 0):
        super().__init__(rect)
        self.type = "circle"
        self.color = color
        self.radius = radius
        self.width = width

graphic = Graphic()