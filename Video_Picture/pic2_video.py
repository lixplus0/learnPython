# -*- encoding: utf-8 -*-
import os
import glob
import numpy as np
import cv2

def cv_imread(imgfile):
    '''解决中文路径和名称问题，读取'''
    cv_img = cv2.imdecode(np.fromfile(imgfile, dtype=np.uint8), -1)
    return cv_img

# def cv_imgwrite(path, file_type, new_img, img_temp_path):
#     '''解决中文路径和名称问题，写入'''
#     cv2.imencode('.' + file_type, new_img)[1].tofile(img_temp_path)

def resize_img(image, h, w, width, height):
    '''调整图像尺寸为width，height，高度不足补黑，高度过大则裁剪'''
    try:
        top, bottom = (0, 0)
        temp_h = int(h * width / w)
        new_img_temp = cv2.resize(image, (width, temp_h))
        dh = height - temp_h
        if dh > 0:
            top = dh // 2
            bottom = dh - top
            border_color = [0, 0, 0]    # RGB颜色，黑色
            new_img = cv2.copyMakeBorder(
                new_img_temp, top, bottom, 0, 0, cv2.BORDER_CONSTANT, value=border_color)
        else:
            dh = - dh
            top = dh // 2
            new_img = new_img_temp[top:(top+height), 0:width]

        return new_img
    except Exception as e:
        print(e)
        return 0

def get_allimg(path_origin):
    '''获取路径下的所有img图像，返回图像路径列表'''
    file_types = ["*.jpg", "*.png"]
    all_imgs = []
    for file_type in file_types:
        all_imgs += glob.glob(os.path.join(path_origin, file_type))
    return all_imgs

class pic2video():
    def __init__(self):
        self.width = 800
        self.height = 800
        self.pic_path = r'D:\MyFiles\Downloads\Pictures\mziTu\2018年09月'
        self.fps = 1

    def set_value(self, width_in, height_in, pic_path_in, fps_in=1):
        self.width = width_in
        self.height = height_in
        self.pic_path = pic_path_in
        self.fps = fps_in

    def trans_video(self):
        parent_path = os.path.dirname(self.pic_path)

        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        all_imgs = get_allimg(self.pic_path)
        count_all = len(all_imgs)
        count = 1
        my_videoWriter = cv2.VideoWriter(parent_path + '_' + os.path.basename(
            self.pic_path) + '.avi', fourcc, self.fps, (self.width, self.height))
            
        for imgfile in all_imgs:
            image = cv_imread(imgfile)
            h, w, _ = image.shape

            if h == self.height and w == self.width:
                new_img = image
            else:
                # file_type = os.path.splitext(imgfile)[-1]
                new_img = resize_img(image, h, w, self.width, self.height)

            my_videoWriter.write(new_img)    # 把new_img写入视频
            print('\r进度: {:.0%}'.format((count)/count_all), end=" ")
            count += 1

        my_videoWriter.release()
        print('\n转换完成，视频文件位于', parent_path)

def __main__():
    '''请事先确认文件夹内图片的尺寸，iPhoneX尺寸 1125*2436'''
    WIDTH = 700
    HEIGHT = 1050
    PIC_PATH = r'D:\MyFiles\Downloads\Pictures\xingganmeinv\2018年06月'

    my_trans = pic2video()
    my_trans.set_value(WIDTH, HEIGHT, PIC_PATH)
    my_trans.trans_video()

if __name__ == "__main__":
    __main__()
