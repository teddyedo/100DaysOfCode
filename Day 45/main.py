from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

titles = [film_tag.getText() for film_tag in soup.select(selector="h3")][::-1]

with open("film_to_watch.txt", "w", encoding="utf8") as film_file:
    [film_file.write("%s\n" % title) for title in titles]