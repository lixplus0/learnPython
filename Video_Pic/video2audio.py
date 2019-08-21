# -*- coding: utf-8 -*-
import os
from natsort import natsorted

ffmpeg = r'"D:\Program Files (x86)\MarukoToolbox\tools\ffmpeg.exe"'
video_path = r"D:\MyFiles\Downloads\Video\相声小品全集\陈佩斯"
out_path = r"D:\MyFiles\Downloads\Video\相声小品全集\音乐文件"

for root, dirs, files in os.walk(video_path):
    # 按文件名排序
    files = natsorted(files)
    # 遍历所有文件
    for file in files:
        file_name = os.path.splitext(file)
        if file_name[1] == '.mp4':    # 如果后缀名为 .mp4
            # audio = mpe.AudioFileClip(os.path.join(root, file))
            print('当前转换文件 %s ' % file)
            # audio.write_audiofile(os.path.join(video_path, file_name[0] + '.mp3'))
            cmd = ffmpeg + " -i " + os.path.join(root, file) +  " -vn -sn -c:a copy -y -map 0:a:0 " + os.path.join(out_path, file_name[0] + '.aac')
            os.system(cmd)
