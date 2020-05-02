import cv2
import matplotlib.pyplot as plt


temp = r"C:/Users/INTEL/Desktop/rishabh/soc_project/ps0_python/Output/"

img = cv2.cvtColor(cv2.imread(temp+"ps0-1-a-1.tiff"), cv2.COLOR_BGR2RGB)


cv2.imwrite(temp+"ps0-2-a-1.png", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#plt.imsave(temp+("ps0-2-a-1.png"), img2)

r,g,b = cv2.split(img)


#plt.imsave(temp+("ps0-2-c-1.png"), r, cmap="Greys_r")

#plt.imsave(temp+("ps0-2-b-1.png"), g, cmap="Greys_r")
