from bs4 import BeautifulSoup

import requests
from collections import namedtuple



player_list_html = requests.get(tests_url).content

soup = BeautifulSoup(player_list_html)
player_class_dict = {'class': 'ciPlayername'}

player_list_raw = soup.find_all('li',attrs=player_class_dict)

#dict create the player -> link dict
Player_tup = namedtuple('Player',['name','link'])

class Player(object):
    def __init__(self, name, link, country):
        self.name = name
        self.link = link
        self.country = country
        self.formats_played = []

#a = Player_tup(p.text,p.find('a').attrs['href'])
player_list_tupled = []


for p in player_list_raw:
    name = p.text
    link = p.find('a', attrs['href']
    t = Player_tup(p.text,p.find('a').attrs['href'])
    o = Player(
    player_list_tupled.append(t)

match_type_dict = dict(test=1, odi = 2, t20 = 3,)
country_dict = dict(india = 6, england = 1, australia = 2, south_africa = 3, west_indies = 4, new_zealand = 5, pakistan = 7, sri_lanka = 8, zimbabwe = 9,)

#build player list
resulting_player_list = []
for k,v in country_dict.items()[:1]:
    country_code = v
    country_name = k
    for m_k,m_v in match_type_dict.items():
        match_type_str = m_k
        play_format = m_v
        url_format = 'http://www.espncricinfo.com/ci/content/player/caps.html?country={country_code};class={play_format}'
        url = url_format.format(country_code=country_code, play_format = play_format)
        print "getting data from "  + url

        player_list_html = requests.get(url).content

        soup = BeautifulSoup(player_list_html)
        player_class_dict = {'class': 'ciPlayername'}

        player_list_raw = soup.find_all('li',attrs=player_class_dict)
        for p in player_list_html:
            

        
    #tests_url = 'http://www.espncricinfo.com/ci/content/player/caps.html?country=6;class=1'
    












