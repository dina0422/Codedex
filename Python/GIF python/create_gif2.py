import imageio.v3 as iio
from PIL import Image #for image manipulation
import numpy as np #for array manipulation 

filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
images = []

for filename in filenames:
    img = Image.open(filename).convert('RGBA')  # Convert all images to RGBA
    # print(f"{filename} shape: {img.shape}")  # Found out that 1 image had 3 channels (RGB) and another two with 4
    img_array = np.array(img)  # Convert PIL Image to NumPy array
    images.append(img_array)

iio.imwrite('nyan-cat.gif', images, duration=500, loop=0)