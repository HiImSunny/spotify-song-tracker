import time

from flask import Flask, request, redirect, session, render_template
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
import requests
import os

app = Flask(__name__)
app.secret_key = os.environ['SESSION_SECRET']

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
REDIRECT_URI = 'http://localhost:3000/callback'
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
SCOPE = [
    "user-read-currently-playing"
]

@app.route("/login")
def login():
    spotify = OAuth2Session(CLIENT_ID, scope=SCOPE, redirect_uri=REDIRECT_URI)
    authorization_url, state = spotify.authorization_url(AUTH_URL)
    return redirect(authorization_url)


@app.route("/callback", methods=['GET'])
def callback():
    code = request.args.get('code')
    res = requests.post(TOKEN_URL,
                        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                        data={
                            'grant_type': 'authorization_code',
                            'code': code,
                            'redirect_uri': REDIRECT_URI
                        })
    # Store the access token in a session
    session['access_token'] = res.json().get('access_token')
    return redirect("/")


@app.route("/")
def current_playing():
    access_token = session.get('access_token')
    while True:
        if access_token:
            url = "https://api.spotify.com/v1/me/player/currently-playing"
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                song_name = data["item"]["name"]
                artist_name = data["item"]["artists"][0]["name"]
                cover_image_url = data["item"]["album"]["images"][0]["url"]

                # Write the song_name to a text file
                with app.app_context():
                    with open("song.txt", "w", encoding="utf-8") as file:
                        file.write(song_name + " by " + artist_name)

                # Download and save the image file
                response = requests.get(cover_image_url)
                if response.status_code == 200:
                    with open("cover_image.jpg", "wb") as file:
                        file.write(response.content)

                return render_template("index.html", song_name=song_name, artist_name=artist_name,
                                       cover_image_url=cover_image_url)
        time.sleep(5)  # Pause the execution for 5 seconds before checking again


if __name__ == '__main__':
    app.run(port=3000, debug=True)
