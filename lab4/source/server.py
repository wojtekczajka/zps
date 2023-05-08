from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse


app = FastAPI()

def generate_video_player(video_file: str):
    if video_file is None:
        return ""
    return f"""
        <h2>Video player</h2>
        <video id="videoPlayer" src="{video_file}" controls></video>
        <br>
        <button id="videoCancel" onclick="document.getElementById('videoPlayer').src='cancel.mp4'">Cancel Video</button>
        <button id="videoAdd" onclick="addToPlaylist('video', '{video_file}')">Add video</button>
    """

def generate_audio_player(audio_file: str):
    if audio_file is None:
        return ""
    return f"""
        <h2>Audio player</h2>
        <audio id="audioPlayer" src="{audio_file}" controls></audio>
        <br>
        <button id="audioCancel" onclick="document.getElementById('audioPlayer').src='cancel.mp3'">Cancel Audio</button>
        <button id="audioAdd" onclick="addToPlaylist('audio', '{audio_file}')">Add audio</button>
    """

def generate_image_poster(img_file: str):
    if img_file is None:
        return ""
    return f"""
            <h2>Image Poster</h2>
            <img id="posterImage" src="{img_file}" controls>
            <br>
            <button id="imgCancel" onclick="document.getElementById('posterImage').src='cancel.jpg'">Cancel Image</button>
            <button id="imgAdd" onclick="addToPlaylist('img', '{img_file}')">Add img</button>
    """

def generate_playlist_table():
    return f"""
        <h2>Playlist Table</h2>
        <table id="playlist_table">
            <tr>
                <th>No.</th>
                <th>URL</th>
                <th>Type</th>
            </tr>
        </table>
    """

def generate_html_response(video_file: str, audio_file: str, img_file: str):
    return f"""
        <html>
            <head>
                <title>Hello World Player</title>
            </head>
            <body>
                <h1>Hello World Player</h1>
                {generate_video_player(video_file)}
                {generate_audio_player(audio_file)}
                {generate_image_poster(img_file)}
                {generate_playlist_table()}
                <script>
                    let rowCount = 0;
                    function addToPlaylist(type, url) {{
                        rowCount++;
                        let table = document.getElementById("playlist_table");
                        let row = table.insertRow();
                        let noCell = row.insertCell(0);
                        let urlCell = row.insertCell(1);
                        let typeCell = row.insertCell(2);
                        noCell.innerHTML = rowCount;
                        urlCell.innerHTML = url;
                        typeCell.innerHTML = type.charAt(0).toUpperCase() + type.slice(1);
                    }}
                </script>
            </body>
        </html>
    """

@app.get("/")
async def get_players(videoFile: Union[str, None] = None, audioFile: Union[str, None] = None, imgFile: Union[str, None] = None):
    return HTMLResponse(content=generate_html_response(videoFile, audioFile, imgFile))

# sample video https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4
# sample audio https://www2.cs.uic.edu/~i101/SoundFiles/StarWars3.wav
# sample img   https://picsum.photos/200/300

# request url http://127.0.0.1:4080/?videoFile=https%3A%2F%2Fsample-videos.com%2Fvideo123%2Fmp4%2F720%2Fbig_buck_bunny_720p_1mb.mp4&audioFile=https%3A%2F%2Fwww2.cs.uic.edu%2F~i101%2FSoundFiles%2FStarWars3.wav&imgFile=https%3A%2F%2Fpicsum.photos%2F200%2F300
