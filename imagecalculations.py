import cv2
import numpy as np
from math import sqrt
from PIL import Image

X_data = []
files = "/Users/mohanpraveenhazaru/Documents/audit_log/gehc-ai-lf-inference-package/test/input/ptx/noptx-2.png"
image = Image.open("/Users/mohanpraveenhazaru/Desktop/face.png")
resize_image = image.resize(256, 256)

X_data.append(cv2.imread(files))
min = np.min(X_data)
max = np.max(X_data)
mean = np.mean(X_data)
std = np.std(X_data)
# std = sqrt(mean(abs(min - max.mean())**2))
# adjsted = max(std,1/np.sum(np.array(X_data).shape))
# print('X_data shape:', np.array(X_data).shape)
print np.array(X_data).shape
print 1 / np.sum(np.array(X_data).shape)
print mean
print std
print min
print max
