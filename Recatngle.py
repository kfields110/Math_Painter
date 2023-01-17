class Rectangle:

    def __init__(self, height, width, color, x, y):
        self.height = height
        self.width = width
        self.color = color
        self.x = x
        self.y = y

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color