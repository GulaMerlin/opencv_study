import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os
path = 'D:\Code\study_opencv\images'


def main():
    img_path1 = os.path.join(path, 'cat1.jpg')
    img_path2 = os.path.join(path, 'Hart1.jpg')
    img1 = cv.imread(img_path1)
    img2 = cv.imread(img_path2)

    h, w, _ = img1.shape
    #  压缩文件使得两张图片相同
    img2 = cv.resize(img2, (w, h), interpolation=cv.INTER_AREA)

    dst = cv.addWeighted(img1, 0.6, img2, 0.4, 0)
    cv.imshow('dst', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
