import cv2
import numpy as np
before=cv2.imread('screenshot.png')
after=before.copy()
b_channel, g_channel, r_channel = cv2.split(after)
alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255
for i in range(1000):
    if b_channel[500,i]!=0:
        start=i
        break
for i in range(1000):
    if b_channel[500,2399-i]!=0:
        end=2399-i
        break
alpha_channel[:,:]=0
alpha_channel[:,start:end]=255
saved = cv2.merge((b_channel[:,start:end], g_channel[:,start:end], r_channel[:,start:end], alpha_channel[:,start:end]))

cv2.imwrite("noback.png", saved)
cv2.destroyAllWindows()

#x:350,2000
#y1260x2400