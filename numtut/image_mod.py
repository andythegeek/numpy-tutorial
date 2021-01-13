import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread("numtut/kitty.jpg")
print(type(img))
print(img.shape)

# Blue image
#output = img.copy() # The original image is read-only!
#output[:, :, :2] = 0
#mpimg.imsave("blue.jpg", output)

# Gray image
#averages = img.mean(axis=2) # Take the average of each R, G, and B
#mpimg.imsave("bad-gray.jpg", averages, cmap="gray")

weights = np.array([0.3, 0.59, 0.11])
grayscale = img @ weights
mpimg.imsave("good-gray.jpg", grayscale, cmap="gray")