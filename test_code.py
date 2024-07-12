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

# 定义一个空函数，后续用作createTrackbar的回调函数
def nothing(x):
    pass

# 加载图片
img = cv2.imread('your_image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建窗口
cv2.namedWindow('Image')

# 创建初始阈值
initial_threshold = 127
max_threshold = 255

# 创建滑动条
cv2.createTrackbar('Threshold', 'Image', initial_threshold, max_threshold, nothing)

while True:
    # 获取滑动条的当前值
    threshold = cv2.getTrackbarPos('Threshold', 'Image')

    # 应用阈值化
    _, binary_img = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # 查找轮廓
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历轮廓并绘制大于阈值的轮廓
    filtered_img = img.copy()
    min_area = cv2.getTrackbarPos('Min Area', 'Image')
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:
            cv2.drawContours(filtered_img, [contour], -1, (0, 255, 0), 2)

    # 显示图像
    cv2.imshow('Image', filtered_img)

    # 按下ESC键退出循环
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC键的ASCII码是27
        break

# 关闭窗口和释放资源
cv2.destroyAllWindows()
