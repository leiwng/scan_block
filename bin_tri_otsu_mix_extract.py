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


import os

import cv2
import numpy as np

# 图片
# img_fp = r'D:\users_dir\lei.wng@outlook.com\Downloads\5x\ALL\tissue\微信图片_20240711115933.jpg'
# img_fp = r'D:\users_dir\lei.wng@outlook.com\Downloads\5x\ALL\tissue\微信图片_20240711163410.jpg'

img_dir_fp = r'D:\users_dir\lei.wng@outlook.com\Downloads\5x\ALL\HE 阳2'

area_thresh = 80

for fn in [filename for filename in os.listdir(img_dir_fp) if filename.endswith('.jpg')]:
    img_fp = os.path.join(img_dir_fp, fn)

    # 只取原图的文件名，扩展名不要，也不要前面的路径
    fn = img_fp.split(os.sep)[-1].split('.')[0]

    # 加载图像
    img = cv2.imdecode(np.fromfile(img_fp, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 应用阈值化处理来分割图像-TRIANGLE
    _, thresholded = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_TRIANGLE)

    # 保存thresholded
    fn_ext = f'{fn}_10_THRESH_TRI.png'
    fp = os.path.join(os.path.dirname(img_fp), fn_ext)
    cv2.imencode(".png", thresholded)[1].tofile(fp)

    # 查找轮廓
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > area_thresh]

    # 创建一个全黑的图像用来绘制轮廓
    mask_tri = np.zeros_like(gray)

    # 填充找到的轮廓
    cv2.drawContours(mask_tri, contours, -1, (255), thickness=cv2.FILLED)

    # 保存mask
    fn_ext = f'{fn}_20_MASK_THRESH_TRI.png'
    fp = os.path.join(os.path.dirname(img_fp), fn_ext)
    cv2.imencode(".png", mask_tri)[1].tofile(fp)


    # 应用阈值化处理来分割图像-OTSU
    _, thresholded = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 保存thresholded
    fn_ext = f'{fn}_11_THRESH_OTSU.png'
    fp = os.path.join(os.path.dirname(img_fp), fn_ext)
    cv2.imencode(".png", thresholded)[1].tofile(fp)

    # 查找轮廓
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > area_thresh]

    # 创建一个全黑的图像用来绘制轮廓
    mask_otsu = np.zeros_like(gray)

    # 填充找到的轮廓
    cv2.drawContours(mask_otsu, contours, -1, (255), thickness=cv2.FILLED)

    # 保存mask
    fn_ext = f'{fn}_21_MASK_THRESH_OTSU.png'
    fp = os.path.join(os.path.dirname(img_fp), fn_ext)
    cv2.imencode(".png", mask_otsu)[1].tofile(fp)

    # 合并mask
    mask = cv2.bitwise_or(mask_tri, mask_otsu)
    # 保存mask
    fn_ext = f'{fn}_23_MASK_OR.png'
    fp = os.path.join(os.path.dirname(img_fp), fn_ext)
    cv2.imencode(".png", mask)[1].tofile(fp)

    # 使用掩码提取感兴趣的区域
    result = cv2.bitwise_and(img, img, mask=mask)

    # SAVE
    # 保存result
    fn_ext = f'{fn}_30_RESULT_BIN.png'
    fp = os.path.join(os.path.dirname(img_fp), fn_ext)
    cv2.imencode(".png", result)[1].tofile(fp)

# 显示结果
# cv2.imshow('Original', img)
# cv2.imshow('Thresholded', thresholded)
# cv2.imshow('Mask', mask)
# cv2.imshow('Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
