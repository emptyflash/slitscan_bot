import imageio
import os
import moviepy.editor as mpy
from pytube import YouTube
import numpy as np

imageio.plugins.ffmpeg.download()

def get_slit_scans(video_id):
    yt = YouTube("https://www.youtube.com/watch?v=" + video_id)
    youtube_video = sorted(yt.filter('mp4'), key = lambda x : int(x.resolution[:-1]))[-1]
    video_filename = youtube_video.filename + ".mp4"
    youtube_video.download(".")

    def get_row(gf, frame):
        row = frame % clip.h
        return gf(frame / clip.fps)[row]

    def slitscan(gf, t):
        frame = int(clip.fps * t)
        min_frame = int(frame - frame % clip.h)
        max_frame = int(frame + (clip.h - frame % clip.h))
        return np.array([get_row(gf, x) for x in range(min_frame, max_frame)])

    clip = mpy.VideoFileClip(video_filename)
    clip = clip.fl(slitscan, apply_to="mask")
    scans = [clip.get_frame(t / clip.fps) for t in range(0, int(clip.duration * clip.fps), clip.h)]
    os.remove(video_filename)
    return scans
