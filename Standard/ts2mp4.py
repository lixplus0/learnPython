# 主要是需要moviepy这个库
import os
import moviepy.editor as mpe
from natsort import natsorted

ffmpeg = r'"D:\Program Files (x86)\MarukoToolbox\tools\ffmpeg.exe"'
n = 0
for root, dirs, files in os.walk(r"D:\MyFiles\Downloads\Pictures\slimmo\video\960x720"):
    files = natsorted(files)
    for file in files:
        file_split = os.path.splitext(file)
        if file_split[1] == '.ts':
            filePath = os.path.join(root, file)
            out_filePath = os.path.join(r'D:\mp4', file_split[0]+'.mp4')
            print(out_filePath)
            cmd = ffmpeg + " -i " + filePath + " -c copy " + out_filePath
            os.system(cmd)
            n += 1
print(n)
