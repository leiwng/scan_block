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

# 将BGR图像转换为HSV色彩空间
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义HSV中紫色的范围
lower_purple = np.array([125, 40, 40])
upper_purple = np.array([155, 255, 255])

# 根据HSV阈值创建掩码
mask = cv2.inRange(hsv_img, lower_purple, upper_purple)

# 使用掩码提取紫色区域
purple_region = cv2.bitwise_and(img, img, mask=mask)

# 查找轮廓
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 在原图上绘制轮廓
for contour in contours:
    if cv2.contourArea(contour) > 100:  # 过滤小轮廓
        cv2.drawContours(img, [contour], -1, (0, 255, 0), 3)

# 显示图像
cv2.imshow('Original Image', img)
cv2.imshow('Purple Region', purple_region)
cv2.waitKey(0)
cv2.destroyAllWindows()
