import requests
import wget
from bs4 import BeautifulSoup as BS

# how to parse from br ?
URL = "https://m-zona.net/autor/Billie+Eilish/"
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


def get_html(url, params=''):
    req = requests.get(url=URL, params=params, headers=HEADERS)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='track d-flex ai-center grid-item js-item')
    lyrics = []
    for item in items:
        song = item.find('div', class_='track__desc flex-grow-1').find('a')
        lyric = {
            'name': song.string
        }
        song_download_link = item.get("data-track")
        if song_download_link:
            wget.download(song_download_link, out=f'{lyric["name"]}.mp3')
            print(f'{lyric["name"]} downloaded successfully')
        else:
            continue
        lyrics.append(lyric)
    return lyrics


def parser_music():
    html = get_html(URL)
    if html.status_code == 200:
        musics = get_data(html.text)
        return musics
    else:
        raise Exception("Error in parser!")


