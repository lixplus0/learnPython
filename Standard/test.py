# 主要是需要moviepy这个库
import os
import moviepy.editor as mpe
from natsort import natsorted


n = 0
for root, dirs, files in os.walk(r"D:\MyFiles\Downloads\Pictures\slimmo\video\960x720"):
    files = natsorted(files)
    for i in range(0, len(files)-1):
        if os.path.splitext(files[i])[0] == os.path.splitext(files[i+1])[0]:
            print(files[i+1])
            os.remove(os.path.join(root, files[i+1]))
            n += 1
print(n)
