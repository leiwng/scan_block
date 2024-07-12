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

# 创建初始阈值
initial_bin_thresh = 127
initial_area_thresh = 40

# 创建滑动条
cv2.createTrackbar('Threshold', 'Image', initial_bin_thresh, 255, nothing)
cv2.createTrackbar('ContourArea', 'Image', initial_area_thresh, 500, nothing)

while True:
    # 获取滑动条的当前值
    bin_thresh = cv2.getTrackbarPos('Threshold', 'Image')
    area_thresh = cv2.getTrackbarPos('ContourArea', 'Image')

    # 应用阈值化
    _, binary_img = cv2.threshold(resized_img, bin_thresh, 255, cv2.THRESH_BINARY)

    # 查找轮廓
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    bin_img = cv2.threshold(gray_img, bin_thresh, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 去掉面积小于area_thresh的轮廓
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > area_thresh]
    # 求轮廓的Mask
    mask = np.zeros_like(gray_img)
    cv2.drawContours(mask, contours, -1, 255, -1)
    # 将该Mask应用到原图像上
    masked_img = cv2.bitwise_and(resized_img, resized_img, mask=mask)

    # 显示图像
    cv2.imshow('Image', masked_img)

    # 按下ESC键退出循环
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC键的ASCII码是27
        break

# 关闭窗口和释放资源
cv2.destroyAllWindows()
