import yt_dlp

def download_youtube_video(url, output_path='.'):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'cookiefile': 'cookies.txt',  # Path to your cookie file
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL or ID: ")
    download_path = input("Enter the download path (leave empty for current directory): ")
    download_path = download_path.strip() or './yt_dlp/videos'
    download_youtube_video(video_url, download_path)