class RoundRectangleShape:

    #클래스 변수
    shapeIdCounter = 0

    def __init__(self, x,y,width,height,arcWidth,arcHeight):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.arcHeight = arcHeight
        self.arcWidth = arcWidth

    def draw(self):
        print("draw RoundRectangle")

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y
    
    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def getArcWidth(self):
        return self.arcWidth

    def setArcWidth(self, arcWidth):
        self.arcWidth = arcWidth

    def getArcHeight(self):
        return self.getArcHeight

    def setArcHeight(self, arcHeight):
        self.arcHeight = arcHeight

    #클래스 메서드
    @classmethod
    def getShapeIdCounter(cls):
        cls.shapeIdCounter = cls.shapeIdCounter + 1
        return cls.shapeIdCounter

if __name__ == "__main__":
    print(RoundRectangleShape.shapeIdCounter)
    print(RoundRectangleShape.getShapeIdCounter())
    print(RoundRectangleShape.getShapeIdCounter())