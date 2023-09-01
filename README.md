# spotify-song-tracker
Get song name, artist name and album cover for the currently playing song

## Setup
* Step 1: Create [Spotify Dev App](https://developer.spotify.com/dashboard) ([Instruction](https://developer.spotify.com/documentation/web-api))
* Step 2: Clone the project (git clone https://github.com/HiImSunny/spotify-song-tracker)
* Step 3: Edit **app.secret_key**, **CLIENT_ID** and **CLIENT_SECRET** in **main.py**
* Step 4: Run main.py
* Step 5: Open your browser then go to http://localhost:3000/login and authenticate with spotify

After complete all the step, the website should be showing what you're currently playing on spotify
Also, the **song.txt** and **cover_image.jpg** files should be created in the same folder with main.py

> **CLIENT_ID** and **CLIENT_SECRET** is from Spotify Dashboard
>> Step 1: Go to the [Dashboard](https://developer.spotify.com/dashboard) <br>
Step 2: Click on the name of the app you have just created (My App) <br>
Step 3: Click on the Settings button

> You can type any character into **app.secret_key**