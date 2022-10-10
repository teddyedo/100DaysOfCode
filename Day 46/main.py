import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

SPOTIFY_CLIENT_ID = "********************"
SPOTIFY_CLIENT_SECRET = "****************************"


def date_is_valid(date: str):
    try:
        if date != datetime.datetime.strptime(date, "%Y-%m-%d").strftime(
            "%Y-%m-%d"):
            raise ValueError
        return True
    except ValueError:
        return False


input_date = input("Tell me the day you want to relive: (YYYY-MM-DD): ")

while not date_is_valid(input_date):
    input_date = input("Invalid date format. Tell me the day you want to "
                       "relive: (YYYY-MM-DD): ")

response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{input_date}/")

soup = BeautifulSoup(response.text, "html.parser")

songs_titles = [song_tag.getText().strip("\n\t") for song_tag in
                soup.select(selector="li h3")]

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                            client_secret=SPOTIFY_CLIENT_SECRET,
                                            redirect_uri="https://www.example.com/",
                                            scope="playlist-modify-private",
                                            show_dialog=True,
                                            cache_path="token.txt"))

user_id = spotify.current_user()["id"]

songs_links = []

for song in songs_titles:
    try:
        link = spotify.search(q=f"track:{song}", limit=1,
                              type="track")["tracks"]["items"][0]["uri"]
        songs_links.append(link)
    except IndexError:
        print(f"{song} doesn't exist on spotify. Ignored.")

playlist = spotify.user_playlist_create(user=user_id,
                                        name=f"{input_date} Billboard 100",
                                        public=False, collaborative=False,
                                        description=f"{input_date} Billboard 100")


spotify.playlist_add_items(playlist["id"], songs_links[:100])
