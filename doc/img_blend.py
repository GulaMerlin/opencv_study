import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os, re, pathlib
# bath_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bath_path = pathlib.Path.cwd().parent
path = pathlib.Path(bath_path, 'images')


def img_blend():
    img_path1 = os.path.join(path, 'cat1.jpg')
    img_path2 = os.path.join(path, 'Hart1.jpg')

    img1 = cv.imread(img_path1)
    img2 = cv.imread(img_path2)
    h, w, _ = img1.shape
    #  压缩文件使得两张图片相同
    img2 = cv.resize(img2, (w, h), interpolation=cv.INTER_AREA)

    dst = cv.addWeighted(img1, 0.8, img2, 0.2, 0)
    all_add = cv.add(img1, img2)
    cv.imshow('dst', dst)
    cv.imshow('all_add', all_add)
    cv.waitKey(0)
    cv.destroyAllWindows()


def img_anwei():
    img_path2 = os.path.join(path, 'dva1.jpg')
    img_path1 = os.path.join(path, 'toum.jpg')

    img1 = cv.imread(img_path1)
    img2 = cv.imread(img_path2)
    h, w, _ = img1.shape
    img1 = cv.resize(img1, (1512, 1512), interpolation=cv.INTER_AREA)
    # 选择ROI
    rows, cols, channels = img2.shape
    roi = img1[0: rows, 0: cols]

    # 创建一个logo的掩码并创建它的反掩码

    # 将BGR格式转换成灰度图片
    # cv2读取维BGR格式
    # cv2.COLOR_BGR2RGB 将BGR格式转换成RGB格式
    # cv2.COLOR_BGR2GRAY 将BGR格式转换成灰度图片

    img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

    # • cv2.THRESH_BINARY（黑白二值）
    # • cv2.THRESH_BINARY_INV（黑白二值反转）
    # • cv2.THRESH_TRUNC （得到的图像为多像素值）
    # • cv2.THRESH_TOZERO
    # • cv2.THRESH_TOZERO_INV
    # 该函数有两个返回值，第一个retVal（得到的阈值值（在后面一个方法中会用到）），第二个就是阈值化后的图像。
    ret, mask = cv.threshold(img2gray, 200, 255, cv.THRESH_BINARY)

    mask_inv = cv.bitwise_not(mask)

    # 在ROI中去掉logo区域
    img1_bg = cv.bitwise_and(roi, roi, mask=mask)
    img2_fg = cv.bitwise_and(img2, img2, mask=mask_inv)

    dst = cv.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols] = dst

    cv.imshow('res', img1)
    # cv.imshow('res1', img1_bg)
    # cv.imshow('res2', img2_fg)
    # cv.imshow('res3', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()




def main():
    # img_blend()
    img_anwei()


if __name__ == '__main__':
    main()
