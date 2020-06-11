import cv2 as cv
import os
from matplotlib import pyplot as plt
import numpy as np
path = 'D:\Code\study_opencv\images'


def open_img(img_name):
    image_path = os.path.join(path, img_name)
    img = cv.imread(image_path, 0)

    cv.namedWindow('dva', cv.WINDOW_NORMAL)
    # cv.imwrite('t.jpg', img)  # 保存图片
    cv.imshow('dva', img)
    cv.waitKey(0)  # 0直到按下任何键退出窗口 单位毫秒
    cv.destroyAllWindows()


def touch_key_control_img(img_name):
    img_path = os.path.join(path, img_name)
    img = cv.imread(img_path, 1)
    cv.imshow('image', img)

    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()
    elif k == ord('s'):
        cv.imwrite('save_test.jpg', img)
        cv.destroyAllWindows()


def plt_open(img_name):
    img_path = os.path.join(path, img_name)
    img = cv.imread(img_path, 0)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()


def draw_line():
    img = np.zeros((512, 512, 3), np.uint8)
    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    # 圆
    cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
    # 椭圆
    cv.ellipse(img, (256, 256), (100, 50), 10, 10, 360, (122, 110, 255), -1)
    font = cv.FONT_HERSHEY_SIMPLEX

    cv.putText(img, 'Gl', (10, 450), font, 3, (255, 255, 255), 10)

    # pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    # pts = pts.reshape((-1, 1, 2))
    winname = 'example'
    cv.namedWindow(winname)
    cv.imshow(winname, img)
    cv.waitKey(0)
    cv.destroyWindow(winname)

    # plt.imshow(img)
    # plt.xticks([]), plt.yticks([])
    # plt.show()


def event_():
    events = [i for i in dir(cv) if 'EVENT' in i]

    print(events)
    img = np.zeros((52, 52, 13), np.uint8)

    def draw_circle(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img, (x, y), 60, (255, 110, 110), -1)

    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    while 1:
        cv.imshow('image', img)
        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()


def event_drawing_rectangle_circle():
    # 当按下鼠标时变为 True
    drawing = False
    # 如果 mode 为true绘制矩形 当按下’m‘ 变成绘制曲线
    mode = True
    ix, iy = -1, -1
    img = np.zeros((512, 512, 3), np.uint8)
    img = np.zeros((512, 512, 3), np.uint8)
    # 创建回调函数
    def draw_circle_re(event, x, y, flags, param):

        global ix, iy
        global drawing, mode

        # 当按下左键是返回起始位置坐标
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        # 当按下鼠标左键并移动是绘制图形 event可以查看移动 flag是否按下
        elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
            if drawing == True:
                if mode == True:
                    cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                # 绘制圆圈 小圆点连在一起就成了线 3代表笔画的粗细
                cv.circle(img, (x, y), 3, (255, 0, 255), -1)

        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle_re)
    while True:
        cv.imshow('image', img)
        k = cv.waitKey(1)
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break


class EventDrawRectangleCircle():

    def __init__(self):
        self.drawing = False
        self.mode = True
        self.ix, self.iy = -1, -1
        self.img = np.zeros((512, 512, 3), np.uint8)

    def draw_re_ci(self, event, x, y, flag, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x, y
        elif event == cv.EVENT_MOUSEMOVE and flag == cv.EVENT_FLAG_LBUTTON:
            if self.drawing == True:
                if self.mode == True:
                    cv.rectangle(self.img, (self.ix, self.iy), (x, y), (255, 0, 255), 1)
                else:
                    # 曲线
                    cv.circle(self.img, (x, y), 3, (255, 0, 255), -1)
                    # 圆形
                    # r = int(np.sqrt((x - self.ix) ** 2 + (y - self.iy) ** 2))
                    # cv.circle(self.img, (x, y), r, (0, 0, 255), -1)
        elif event == cv.EVENT_LBUTTONUP:
            self.drawing = False

    def run_img(self):
        cv.namedWindow('image')
        cv.setMouseCallback('image', self.draw_re_ci)
        while True:
            cv.imshow('image', self.img)
            k = cv.waitKey(1)
            if k == ord('m'):
                self.mode = not self.mode
            elif k == 27:
                break


def main():
    # open_img('dva1.jpg')
    # touch_key_control_img('dva1.jpg')
    # plt_open('dva1.jpg')
    # draw_line()
    # event_()
    # event_drawing_rectangle_circle()
    d = EventDrawRectangleCircle()
    d.run_img()
    pass


if __name__ == '__main__':
    main()
