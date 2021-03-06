import numpy as np
import cv2 as cv
import os 
counter = 0
env = list(os.walk('images'))
# print(env)

def parser():
    total = []
    for s in env:
        total.append(np.squeeze(s[-1]))

    total = np.squeeze(total)
    vid_paths = []
    # print(total[0])
    for s in total:
        # print(s)
        if s[-4:] == '.png':
            vid_paths.append('images/'+s)
    return vid_paths

raw_videos = parser()
def vds(counter):
    for i in raw_videos:
        cap = cv.VideoCapture(i)
        for fp in range(10000):
            try:
                # print(i)
                ret,frame = cap.read()
                # cv.imshow('vid',frame)
                cv.imwrite(f'insects/photos/{counter}.png',frame)
                cv.waitKey(1)
                counter += 1
            except:
                pass
def imgs():
    import cv2 as cv
    for i in raw_videos:
        img = cv.imread(i)
        w,h,ch = img.shape
        # print(img.shape)
        img = cv.resize(img,(256,256))
        cv.imwrite(i,img)

imgs()