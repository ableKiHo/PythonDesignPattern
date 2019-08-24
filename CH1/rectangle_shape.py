class RectangleShape:

    #생성자
    def __init__(self, x, y, width, height):
        #멤버변수
        self.x = x
        self.y = y

        self.width = width
        self.height = height

    #메서드
    def draw(self):
        print("draw Rectangle")        

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
