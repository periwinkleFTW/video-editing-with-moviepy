from moviepy.editor import VideoFileClip, concatenate_videoclips, \
    vfx, AudioFileClip, afx, CompositeAudioClip

# Take parts from 10s to 20s
clip1 = VideoFileClip('Seoul - 21985.mp4').subclip(1, 11).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip2 = VideoFileClip('Shoes - 3627.mp4').subclip(2, 12).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)

# Video effects
clip3 = VideoFileClip('Seoul - 21985.mp4').subclip(1, 11)\
    .fx(vfx.colorx, 1.5).fx(vfx.lum_contrast, 0, 50, 128).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)

# Adding audio
audio = AudioFileClip('order-99518.mp3').subclip(1, 20).fx(afx.audio_fadein, 1)


combined = concatenate_videoclips([clip1, clip2, clip3])
combined.audio = CompositeAudioClip([audio])
combined.write_videofile('combined.mp4')


