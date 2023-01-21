import cv2
import numpy as np
canvas = np.zeros([600, 600])
canvas[100:500, 100:400] = 255
cv2.imshow("strings", canvas)
cv2.waitKey(0)