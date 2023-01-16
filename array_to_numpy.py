import numpy as np
from PIL import Image

data = np.zeros((5,4,3), dtypes=np.uint8)
data[:] = [255,255,0]

img = Image.fromarray((data, 'RGB'))
img.save('canvas.png')
