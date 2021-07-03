import cv2
import os
import time

video_path = r'video/'
savedpath = r'images/'

video_list = os.listdir(video_path)

count = 10
i = 0

for index, video_name in enumerate(video_list):
    j = 0
    video_path_ = os.path.join(video_path, video_name)
    save_path_ = savedpath
    if os.path.exists(save_path_):
        pass
    else:
        os.mkdir(save_path_)

    videoCapture = cv2.VideoCapture(video_path_)

    while True:

        success, frame = videoCapture.read()
        i += 1
        if (i % count == 0):
            j += 1
            savedname = video_name[:-4] + str(i).zfill(4) + '.jpg'
            cv2.imwrite(os.path.join(save_path_, savedname), frame)
            print('image of %s is saved' % (savedname))
        if not success:
            print('video is all read')
            break

    videoCapture.release()
    time.sleep(5)
