import cv2
import matplotlib.pyplot as plt


temp = r"C:/Users/INTEL/Desktop/rishabh/soc_project/ps0_python/Output/"

img1 = cv2.cvtColor(cv2.imread(temp + "ps0-1-a-1.tiff"), cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(cv2.imread(temp + "ps0-1-a-2.tiff"), cv2.COLOR_BGR2RGB)

img1_width, img1_height = img1.shape[:2]
img2_width, img2_height = img2.shape[:2]

img3 = img2.copy()

img1_start_x = int(img1_width / 2 - 50)
img1_start_y = int(img1_height / 2 - 50)

img2_start_x = int(img2_width / 2 - 50)
img2_start_y = int(img2_height / 2 - 50)

img3[img2_start_x:img2_start_x+100, img2_start_y:img2_start_y+100] = img1[img1_start_x:img1_start_x+100, img1_start_y: img1_start_y+100]



plt.imsave(temp+"ps0-3-a-1.png", img3)



