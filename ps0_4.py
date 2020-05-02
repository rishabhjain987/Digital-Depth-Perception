import cv2
from matplotlib import pyplot as plt
import numpy as np


temp = r"C:/Users/INTEL/Desktop/rishabh/soc_project/ps0_python/Output/"
img = cv2.cvtColor(cv2.imread(temp+"ps0-1-a-1.tiff"), cv2.COLOR_BGR2RGB)

r,g,b = cv2.split(img)
print( np.min(g), np.max(g), np.mean(g), np.std(g) )

img2 = g.copy()

mean = np.mean(g)
standrad_deviation = np.std(g)

img2[:] = (((img2[:] - mean)/standrad_deviation) * 10) + mean
plt.imsave(temp+"ps0-4-b-1.png", img2)

rows, cols = g.shape
M = np.float32([[1,0,-2],[0,1,0]])
img3 = cv2.warpAffine(g, M, (cols, rows))
plt.imsave(temp+"ps0-4-c-1.png", img3)

img4 = g - img3
plt.imsave(temp+"ps0-4-d-1.png", img4)


