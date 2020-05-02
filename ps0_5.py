import cv2
from matplotlib import pyplot as plt
import numpy as np

PATH = r"C:/Users/INTEL/Desktop/rishabh/soc_project/ps0_python/Output/"

img = cv2.cvtColor(cv2.imread(PATH+"ps0-1-a-1.tiff"), cv2.COLOR_BGR2RGB)

row, col, ch = img.shape

r,g,b = cv2.split(img)

mean = 0
var = 100
sigma = var**0.5
gauss = np.random.normal(mean, sigma, (row, col))
gauss = gauss.reshape(row, col)

print(gauss)

r1 = r + gauss


print(r1.size, g.size, b.size)
print(r1.shape, g.shape, b.shape)

r = r.astype(float) / 255
r1 = r1.astype(float) /255

g = g.astype(float) /255
g1 = g + gauss
g1 = g1.astype(float)/255


b = b.astype(float) /255
b1 = b + gauss
b1 = b1.astype(float) /255

img1 = cv2.merge((r1,g,b))

img2 = cv2.merge((r,g,b1))

img3 = cv2.merge((r,g1,b))

plt.imsave(PATH+"ps0-5-a-1.png", img1)

plt.imsave(PATH+"ps0-5-b-1.png", img2)

