from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

# sample video https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4
# sample audio https://www2.cs.uic.edu/~i101/SoundFiles/StarWars3.wav

app = FastAPI()

def generate_html_response(video_file: str, audio_file: str):
    return f"""
            <html>
                <head>
                    <title>Hello World Player</title>
                </head>
                <body>
                <h1>Hello World Player</h1>
                {'<h2>Video player</h2><video id="videoPlayer" src="' + video_file + '" controls></video>' if video_file is not None else ''}
                {'<h2>Audio player</h2><audio id="audioPlayer" src="' + audio_file + '" controls></audio>' if audio_file is not None else ''}
                </body>
            </html>
    """

@app.get("/")
async def get_players(videoFile: Union[str, None] = None, audioFile: Union[str, None] = None):
    return HTMLResponse(content=generate_html_response(videoFile, audioFile))