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
        <button id="videoPlay" onclick="playVideo()">Play Video</button>
        <button id="videoPause" onclick="pauseVideo()">Pause Video</button>
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
        <button id="audioPlay">Play Audio</button>
        <button id="audioPause">Pause Audio</button>
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
                <th>Action</th> 
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
                        let actionCell = row.insertCell(3);
                        noCell.innerHTML = rowCount;
                        urlCell.innerHTML = url;
                        typeCell.innerHTML = type.charAt(0).toUpperCase() + type.slice(1);
                        actionCell.innerHTML = '<button class="removeRowButton" onclick="removeRow(this)">Delete</button>' +
                                                '<button class="moveRowUpButton" onclick="moveRowUp(this)">Up</button>' +
                                                '<button class="moveRowDownButton" onclick="moveRowDown(this)">Down</button>';
                        updateRowNumbers(table);
                    }}

                    function removeRow(button) {{
                        let row = button.parentNode.parentNode;
                        row.parentNode.removeChild(row);
                        let table = document.getElementById("playlist_table");
                        updateRowNumbers(table);
                    }}

                    function moveRowUp(button) {{
                        let row = button.parentNode.parentNode;
                        let table = row.parentNode;
                        if (row.rowIndex === 1) {{
                            // Move the first row to the end
                            table.appendChild(row);
                        }} else {{
                            // Swap the row with the previous row
                            table.insertBefore(row, row.previousSibling);
                        }}
                        updateRowNumbers(table);
                    }}

                    function moveRowDown(button) {{
                        let row = button.parentNode.parentNode;
                        let table = row.parentNode;
                        if (row.rowIndex === table.rows.length - 1) {{
                            // Move the last row to the beginning
                            table.insertBefore(row, table.firstChild.nextSibling);
                        }} else {{
                            // Swap the row with the next row
                            table.insertBefore(row.nextSibling, row);
                        }}
                        updateRowNumbers(table);
                    }}

                    function updateRowNumbers(table) {{
                        let rows = table.getElementsByTagName("tr");
                        for (let i = 1; i < rows.length; i++) {{
                            let numberCell = rows[i].getElementsByTagName("td")[0];
                            numberCell.innerHTML = i;
                        }}
                    }}

                    function playVideo() {{
                        let videoPlayer = document.getElementById("videoPlayer");
                        videoPlayer.play();
                    }}

                    function pauseVideo() {{
                        let videoPlayer = document.getElementById("videoPlayer");
                        videoPlayer.pause();
                    }}
                </script>
            </body>
        </html>
    """


@app.get("/")
async def get_players(videoFile: Union[str, None] = None, audioFile: Union[str, None] = None,
                      imgFile: Union[str, None] = None):
    return HTMLResponse(content=generate_html_response(videoFile, audioFile, imgFile))
