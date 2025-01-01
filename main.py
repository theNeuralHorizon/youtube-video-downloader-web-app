import os
import yt_dlp

def download_video():
    try:
        # Ask for the YouTube link
        url = input("Enter the YouTube video URL: ")
        
        # Options to fetch video information without downloading
        ydl_opts_info = {'quiet': True, 'skip_download': True}
        
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            # Extract video information
            info = ydl.extract_info(url, download=False)
            
            # Print video title and views
            title = info.get('title', 'Unknown title')
            views = info.get('view_count', 'Unknown views')
            print(f"Title: {title}")
            print(f"Views: {views}")
        
        # Confirm download
        confirm = input("Do you want to download this video? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Download canceled.")
            return

        # Set download directory dynamically
        save_path = os.path.expanduser("~/Downloads")
        ydl_opts_download = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts_download) as ydl:
            ydl.download([url])
        print(f"Download completed successfully! Saved to {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
download_video()
