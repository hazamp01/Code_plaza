import cv2
import numpy as np
from math import sqrt

X_data = []
files = "/Users/mohanpraveenhazaru/Documents/audit_log/gehc-ai-lf-inference-package/test/input/ptx/noptx-2.png"
X_data.append (cv2.imread (files))
min=np.min(X_data)
max=np.max(X_data)
mean = np.mean(X_data)
std=np.std(X_data)
# General formula for calculating standard deviation
# std = sqrt(mean(abs(min - max.mean())**2))
# Adjusted standard deviation
adjsted = max(std,1/np.sum(np.array(X_data).shape))
print('X_data shape:', np.array(X_data).shape)
print np.array(X_data).shape
print 1/np.sum(np.array(X_data).shape)
print mean
print std
print min
print max
