from Canvas import Canvas
from Recatngle import Rectangle
from Square import Square

canvas = Canvas(20,30, color=(255,255,255))
r1 = Rectangle(x=1,y=6,width= 10, height=20, color=(100,200,125))
r1.draw(canvas)
s1 = Square(x=1, y=3, side_length=10, color=(150,22,200))
s1.draw(canvas)


canvas.make('canvas.png')