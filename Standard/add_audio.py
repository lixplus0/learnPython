import os
import moviepy.editor as mpe
from natsort import natsorted

# 定义一个数组
# video_file = r"D:\MyFiles\Downloads\Video\slimmo\slimmo_2.mkv"
# video = mpe.VideoFileClip(video_file)

audio_file = r"D:\MyFiles\Downloads\Video\slimmo\IPX-143.mp3"
audio_background = mpe.AudioFileClip(audio_file).subclip(150, 150+31*60+36)
# final_audio = mpe.CompositeAudioClip([video.audio, audio_background])
# final_clip = video.set_audio(audio_background)
# 拼接视频
audio_background.write_audiofile(r"D:\MyFiles\Downloads\Video\slimmo\IPX-1433.mp3")
# 生成目标视频文件
# final_clip.to_videofile(r"D:\MyFiles\Downloads\Video\slimmo\slimmo_2.mp4", fps=24, remove_temp=True)
