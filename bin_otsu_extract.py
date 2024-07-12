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

import cv2
import numpy as np

# 图片
# img_fp = r'D:\users_dir\lei.wng@outlook.com\Downloads\5x\ALL\tissue\微信图片_20240711115933.jpg'
img_fp = r'D:\users_dir\lei.wng@outlook.com\Downloads\5x\ALL\tissue\微信图片_20240711163410.jpg'

# 加载图像
img = cv2.imdecode(np.fromfile(img_fp, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 应用阈值化处理来分割图像
_, thresholded = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# _, thresholded = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)

# 查找轮廓
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 创建一个全黑的图像用来绘制轮廓
mask = np.zeros_like(gray)

# 填充找到的轮廓
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 500:  # 根据区域大小过滤小轮廓
        cv2.drawContours(mask, [contour], -1, (255), thickness=cv2.FILLED)

# 使用掩码提取感兴趣的区域
result = cv2.bitwise_and(img, img, mask=mask)

# 显示结果
cv2.imshow('Original', img)
cv2.imshow('Thresholded', thresholded)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
