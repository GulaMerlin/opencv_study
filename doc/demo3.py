import cv2 as cv
import os
from matplotlib import pyplot as plt
import numpy as np
path = 'D:\Code\study_opencv\images'
img_path = os.path.join(path, 'dva1.jpg')
img = cv.imread(img_path)


print(img.item(10, 10, 2))

img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

# 获取图像的形状
print(img.shape)

# 像素数目
print(img.size)
# 图像数据类型
print(img.dtype)

# 拆分通道
(b, g, r) = cv.split(img)
# cv.imshow('b', b)
# cv.imshow('r', r)
# cv.imshow('g', g)

print(b, g, r)
# 合并通道
img = cv.merge([b, g, r])
# 0,1,2通道归零
img[:, :, 0] = 0

# cv.namedWindow('image')
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()


BLUE=[255,0,0]
img1=cv.imread(img_path)
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231), plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236), plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()