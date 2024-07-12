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
img_fp = r'D:\users_dir\lei.wng@outlook.com\Downloads\5x\ALL\其他\20240711-163843.jpg'
# img_fp = r'D:\users_dir\lei.wng@outlook.com\Downloads\5x\ALL\Feulgen 阳1\82.jpg'
# img = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imdecode(np.fromfile(img_fp, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
resized_img = cv2.resize(img, (1280, 1280))

# 创建窗口
cv2.namedWindow('Image')

def on_window_resize(event, x, y, flags, param):
    global resized_img
    if event == cv2.EVENT_RESIZE:
        # 获取新的窗口尺寸
        new_width = cv2.getWindowImageRect('Image')[2]
        new_height = cv2.getWindowImageRect('Image')[3]

        # 根据新的窗口尺寸重新调整图片大小
        resized_img = cv2.resize(img, (new_width, new_height))

        # 显示调整后的图片
        cv2.imshow('Image', resized_img)

# 注册窗口调整大小的回调函数
# cv2.setMouseCallback('Image', on_window_resize)

# 创建初始阈值
initial_threshold = 127

# 创建滑动条
cv2.createTrackbar('Threshold', 'Image', initial_threshold, 255, nothing)

while True:
    # 获取滑动条的当前值
    threshold = cv2.getTrackbarPos('Threshold', 'Image')

    # 应用阈值化
    _, binary_img = cv2.threshold(resized_img, threshold, 255, cv2.THRESH_BINARY)

    # 显示图像
    cv2.imshow('Image', binary_img)

    # 按下ESC键退出循环
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC键的ASCII码是27
        break

# 关闭窗口和释放资源
cv2.destroyAllWindows()
