import numpy as np
import cv2 as cv
import os 
counter = 0
env = list(os.walk('insects'))
# print(env)

def parser():
    total = []
    for s in env:
        total.append(np.squeeze(s[-1]))

    total = np.squeeze(total)
    vid_paths = []
    # print(total[0])
    for s in total[0]:
        if s[-4:] == '.mp4':
            vid_paths.append('insects/'+s)
    return vid_paths

raw_videos = parser()

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
