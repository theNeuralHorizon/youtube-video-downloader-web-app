# YouTube Video Downloader Web App

This is a simple web application that allows you to download YouTube videos. It uses FastAPI for the backend and `yt-dlp` to handle the downloading of the videos.

## Features

- Enter a YouTube video URL to fetch video information (Title, Views).
- Download the video to your device.
- The app supports downloading videos in the best available quality.

## Technologies Used

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **yt-dlp**: A command-line program to download videos from YouTube and other sites.
- **HTML/CSS**: For the frontend (using basic templates).

## Setup Instructions

### 1. Clone the repository

Clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/youtube-video-downloader.git
```

### 2.Create a virtual environment

It is recommended to use a virtual environment to manage dependencies.

```bash
cd youtube-video-downloader
python3 -m venv myenv
source myenv/bin/activate  # For Linux/Mac
# or
myenv\Scripts\activate  # For Windows
```
### 3.Install the dependencies
Install all necessary packages using pip:

```bash
pip install -r requirements.txt
```
This will install FastAPI, yt-dlp, and other necessary packages.

### 3.Install python-multipart
FastAPI uses the python-multipart library for form data handling. Install it using:

```bash
pip install python-multipart
```

### 4.Run the application locally
To start the development server, run the following command:

```bash
uvicorn app:app --reload
```

Your application will be available at http://127.0.0.1:8000.
