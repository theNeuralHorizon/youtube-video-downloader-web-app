import os
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import yt_dlp
from typing import Optional

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Pydantic model for video info response
class VideoInfo(BaseModel):
    title: str
    views: int

def get_video_info(url: str) -> Optional[VideoInfo]:
    try:
        ydl_opts_info = {'quiet': True, 'skip_download': True}
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown title')
            views = info.get('view_count', 'Unknown views')
            return VideoInfo(title=title, views=views)
    except Exception as e:
        return None

def download_video(url: str) -> bool:
    try:
        save_path = os.path.expanduser("~/Downloads")
        ydl_opts_download = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts_download) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        return False

@app.get("/", response_class=HTMLResponse)
async def index(request: str):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/fetch_video_info", response_class=HTMLResponse)
async def fetch_video_info(request: str, url: str = Form(...)):
    video_info = get_video_info(url)
    if video_info:
        return templates.TemplateResponse("download.html", {"request": request, "video_info": video_info, "url": url})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Failed to retrieve video info. Please check the URL."})

@app.post("/download", response_class=HTMLResponse)
async def download(request: str, url: str = Form(...)):
    success = download_video(url)
    if success:
        return templates.TemplateResponse("success.html", {"request": request})
    else:
        return templates.TemplateResponse("error.html", {"request": request, "error": "Failed to download the video. Try again later."})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)