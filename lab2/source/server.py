from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

def generate_html_response(video_file: str, audio_file: str):
    return f"""
            <html>
                <head>
                    <title>Hello World Player</title>
                </head>
                <body>
                <h1>Hello World Player</h1>
                </body>
            </html>
    """

@app.get("/")
async def get_players(videoFile: Union[str, None] = None, audioFile: Union[str, None] = None):
    return HTMLResponse(content=generate_html_response(videoFile, audioFile))