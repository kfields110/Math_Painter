import numpy as np
from PIL import Image

class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)

