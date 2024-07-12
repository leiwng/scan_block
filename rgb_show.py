# -*- coding: utf-8 -*-
"""模块注释

Author: Lei Wang
Date: April 24, 2024
"""
__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"

import numpy as np
import cv2

# 加载图片
# img_fp = r'D:\users_dir\D:\users_dir\lei.wng@outlook.com\Downloads\5x\ALL\其他\20240711-163843.jpg'
# img_fp = r'D:\users_dir\lei.wng@outlook.com\Downloads\5x\ALL\Feulgen 阳1\82.jpg'
img_fp = r'D:\users_dir\lei.wng@outlook.com\Downloads\5x\ALL\tissue\微信图片_20240711163410.jpg'
img = cv2.imdecode(np.fromfile(img_fp, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
resized_img = cv2.resize(img, (1280, 1280))

# Split channels
b, g, r = cv2.split(resized_img)

# Create zeros matrix for other channels
zeros = np.zeros_like(b)

# Merge each channel with zeros for visualization
blue_channel = cv2.merge((b, zeros, zeros))
green_channel = cv2.merge((zeros, g, zeros))
red_channel = cv2.merge((zeros, zeros, r))

# Display each channel
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
