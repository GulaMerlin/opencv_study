import pathlib

import cv2 as cv
import os
from matplotlib import pyplot as plt
import numpy as np
bath_path = pathlib.Path.cwd().parent
path = pathlib.Path(bath_path, 'images')


class MPalette(object):

    def __init__(self):
        self.img = np.zeros((100, 512, 3), np.uint8)
        cv.namedWindow('image')

        cv.createTrackbar('R', 'image', 0, 255, lambda x: None)
        cv.createTrackbar('G', 'image', 0, 255, lambda x: None)
        cv.createTrackbar('B', 'image', 0, 255, lambda x: None)

        self.switch = '0:OFF\n1:ON'
        cv.createTrackbar(self.switch, 'image', 0, 1, lambda x: None)

    def run_palette(self):
        while True:
            cv.imshow('image', self.img)
            k = cv.waitKey(1)
            if k == 27:
                break
            r = cv.getTrackbarPos('R', 'image')
            g = cv.getTrackbarPos('G', 'image')
            b = cv.getTrackbarPos('B', 'image')
            s = cv.getTrackbarPos(self.switch, 'image')
            if s == 0:
                self.img[:] = 0
            else:
                self.img[:] = [r, g, b]
        cv.destroyAllWindows()


class PalettePen(object):

    def __init__(self):
        self.img = np.zeros((512, 512, 3), np.uint8)
        # 鼠标按下状态
        self.drawing = False
        # 改变绘制形式
        self.mode = True
        self.ix, self.iy = -1, -1
        # 颜色控制
        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')
        self.color = (b, g, r)

    # 回调函数
    def draw_circle(self, event, x, y, flag, param):

        if event == cv.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x, y
        elif event == cv.EVENT_MOUSEMOVE and flag == cv.EVENT_FLAG_LBUTTON:
            if self.drawing:
                if self.mode:
                    cv.rectangle(self.img, (self.ix, self.iy), (x, y), self.color, -1)
                else:
                    cv.circle(self.img, (x, y), 3, self.color, -1)
        elif event == cv.EVENT_LBUTTONUP:
            self.drawing = False

    def run(self):
        cv.namedWindow('image')
        cv.createTrackbar('R', 'image', 0, 255, lambda x: None)
        cv.createTrackbar('G', 'image', 0, 255, lambda x: None)
        cv.createTrackbar('B', 'image', 0, 255, lambda x: None)
        cv.setMouseCallback('image', self.draw_circle)

        while True:
            cv.imshow('image', self.img)
            k = cv.waitKey(1)
            if k == 27:
                break
            elif k == ord('m'):
                self.mode = not self.mode


if __name__ == '__main__':

    # t = MPalette()
    # t.run_palette()
    p = PalettePen()
    p.run()
