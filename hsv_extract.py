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

# 读取医学图像
img = cv2.imdecode(np.fromfile(img_fp, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

# 将图像转换为HSV色彩空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 红色的HSV阈值范围
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# 创建掩码
mask = cv2.inRange(img_hsv, lower_red, upper_red)

# 应用掩码到原始图像上
red_tissue = cv2.bitwise_and(img, img, mask=mask)

# 显示结果
cv2.imshow('Red Tissue', red_tissue)
cv2.waitKey(0)
cv2.destroyAllWindows()
