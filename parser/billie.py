from pprint import pprint

import requests
from bs4 import BeautifulSoup as BS
import wget

URL = 'https://hitster.fm/billie-eilish'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


def get_html(url, params=''):
    req = requests.get(url=URL, params=params, headers=HEADERS)
    return req


def get_music(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('li', class_='track')
    musics = []
    for item in items:
        song_link = 'https://hitster.fm' + item.find('em', class_='playlist-name-title __adv_artist').find('a').get(
            'href')
        music = {
            'song': item.find('em', class_='playlist-name-title __adv_artist').find('a').string,
            'music':2
        }
        # song = wget.download(song_link, out=f'{music["song"]}.mp3')
        # music['music'] = song
        # print('downloaded succesfully')
        musics.append(music)
        pprint(musics)


html = get_html(URL)
get_music(html.text)
