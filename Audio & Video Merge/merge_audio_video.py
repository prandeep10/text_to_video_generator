from moviepy.editor import VideoFileClip, AudioFileClip

def merge_video_audio(input_video_path, input_audio_path, output_video_path):
    # Load video clip
    video_clip = VideoFileClip(input_video_path)

    # Load audio clip
    audio_clip = AudioFileClip(input_audio_path)

    # Trim the video to match the audio duration
    video_clip = video_clip.subclip(0, audio_clip.duration)

    # Set the audio of the video to the loaded audio clip
    video_clip = video_clip.set_audio(audio_clip)

    # Write the merged video with audio to the output file
    video_clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac", temp_audiofile="temp_audio.m4a", remove_temp=True)

if __name__ == "__main__":
    input_video_path = "input_video.mp4"
    input_audio_path = "input_audio.mp3"
    output_video_path = "output_video.mp4"

    merge_video_audio(input_video_path, input_audio_path, output_video_path)
