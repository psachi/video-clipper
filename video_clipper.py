import subprocess

def download_video(youtube_url, output_path="output.mp4"):
    subprocess.run(["yt-dlp", youtube_url, "-o", "video.mp4"], check=True)
    return "video.mp4"

def clip_video(input_file, start_time, end_time, output_file="clip.mp4"):
    subprocess.run(["ffmpeg", "-i", input_file, "-ss", start_time, "-to", end_time, "-c", "copy", output_file], check=True)
    return output_file

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube URL: ")
    start_time = input("Enter the start time (HH:MM:SS): ")
    end_time = input("Enter the end time (HH:MM:SS): ")

    video_file = download_video(youtube_url)
    clipped_file = clip_video(video_file, start_time, end_time)

    print(f"Clipped video saved as {clipped_file}")
