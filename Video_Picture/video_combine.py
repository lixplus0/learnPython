# 主要是需要moviepy这个库
import os
import moviepy.editor as mpe
from natsort import natsorted

# 定义一个数组
L = []

# 访问 video 文件夹 (假设视频都放在这里面)
for root, dirs, files in os.walk(r"D:\MyFiles\Downloads\Pictures\slimmo\video"):
    # 按文件名排序
    files = natsorted(files)
    # 遍历所有文件
    for file in files:
        # 如果后缀名为 .mp4
        if os.path.splitext(file)[1] == '.mp4':
            # 拼接成完整路径
            filePath = os.path.join(root, file)
            # 载入视频
            video = mpe.VideoFileClip(filePath)
            # 添加到数组
            L.append(video)

# 拼接视频
final_clip = mpe.concatenate_videoclips(L)

# 生成目标视频文件
final_clip.to_videofile(r"D:\MyFiles\Downloads\Pictures\slimmo\video\target2.mp4", fps=24, remove_temp=True)