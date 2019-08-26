from CH1.rectangle_shape import RectangleShape

class RoundRectangleShape(RectangleShape):

    def __init__(self,arcWidth,arcHeight):
        self.arcHeight = arcHeight
        self.arcWidth = arcWidth

    def draw(self):
        print("draw RoundRectangle")

    def getArcWidth(self):
        return self.arcWidth

    def setArcWidth(self, arcWidth):
        self.arcWidth = arcWidth

    def getArcHeight(self):
        return self.getArcHeight

    def setArcHeight(self, arcHeight):
        self.arcHeight = arcHeight