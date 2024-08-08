import yt_dlp

def download_video(url, output_path='video-data'):
    try:
        # Create a YT-DLP object
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output template
            'format': 'bestvideo+bestaudio/best',  # Download the best available video and audio
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Attempting to download video from URL: {url}")
            info_dict = ydl.extract_info(url, download=True)
            print(f"Video downloaded successfully: {info_dict['title']}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'URL' with the YouTube video URL you want to download
video_url = 'https://www.youtube.com/watch?v=059irIziaOo'
output_path = 'video-data'  # You can specify the output path if needed

download_video(video_url, output_path)
