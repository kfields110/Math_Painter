class Square:

    def __init__(self, side_length, x, y, color):
        self.side_length = side_length
        self.x = x
        self.y = y
        self.color = color

    def draw(self,canvas):
        canvas.data[self.x: self.x + self.side_length, self.y: self.y + self.side_length] = self.color