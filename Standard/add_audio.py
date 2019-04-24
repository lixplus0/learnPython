import os
import moviepy.editor as mpe
from natsort import natsorted

# 定义一个数组
video_file = r"D:\MyFiles\Downloads\Video\slimmo\slimmo_2.mkv"
# video = mpe.VideoFileClip(video_file)
mkvmerge = r'"D:\Program Files (x86)\MarukoToolbox\tools\mkvmerge.exe"'
audio_aac = r"D:\MyFiles\Downloads\Video\slimmo\RBD-725.aac"
audio_file = r"D:\MyFiles\Downloads\Video\slimmo\RBD-725.mp3"

# ffmpeg = r'"D:\Program Files (x86)\MarukoToolbox\tools\ffmpeg.exe"'
# cmd1 = ffmpeg + " -i " + audio_aac + " -b 1500 -ar 8000 -ac 2 -ab 32 -f mp3 " + audio_file
# os.system(cmd1)

audio_background = mpe.AudioFileClip(audio_file).subclip(11*60+53, 11*60+53+31*60+36)
audio_clip = r"D:\MyFiles\Downloads\Video\slimmo\RBD-725_clip.mp3"
audio_background.write_audiofile(audio_clip)

merged_video = r"D:\MyFiles\Downloads\Video\slimmo\slimmo_2_封装.mkv"
cmd2 = mkvmerge+ " -o " + merged_video + " " + video_file +  " " + audio_clip
os.system(cmd2)