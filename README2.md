## Create a virtual environment

It is recommended to use a virtual environment to manage dependencies.

```bash
cd youtube-video-downloader
python3 -m venv myenv
source myenv/bin/activate  # For Linux/Mac
# or
myenv\Scripts\activate  # For Windows
```
## Install the dependencies
Install all necessary packages using pip:

```bash
pip install -r requirements.txt
```
This will install FastAPI, yt-dlp, and other necessary packages.

# Install python-multipart
FastAPI uses the python-multipart library for form data handling. Install it using:

```bash
pip install python-multipart
```

## Run the application locally
To start the development server, run the following command:

```bash
uvicorn app:app --reload
```

Your application will be available at http://127.0.0.1:8000.
