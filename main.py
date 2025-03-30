import moviepy.editor

# Load the video file
cvt_video = moviepy.editor.VideoFileClip("video.mp4")

# Extract audio from the video
ext_audio = cvt_video.audio

# Save the extracted audio as an MP3 file
ext_audio.write_audiofile("audio_extracted.mp3")

# Close the video clip to free resources
cvt_video.close()
