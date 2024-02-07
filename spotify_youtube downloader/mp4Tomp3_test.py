from moviepy.editor import VideoFileClip

# Load the mp4 file
video_path = "test.mp4"
output_audio_path = "example.mp3"

video = VideoFileClip(video_path)

# Extract audio from video
video.audio.write_audiofile(output_audio_path, codec="mp3")
