import datetime

from user_agent import generate_user_agent
import requests
from bs4 import BeautifulSoup

def England_parser():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.premierleague.com/tables'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    club_content = soup.findAll("tr", {"data-compseason": "489"})
    dic = {}
    for i in club_content:
        position = i.find("span", {"class": "value"}).text
        club_name = i.find("span", {"class": "long"}).text
        club_site = i.find("a")['href']
        tmp = club_site.replace('overview', 'stats')
        club_stat_url = 'https://www.premierleague.com' + tmp
        game = i.findAll("td")[3].text
        won = i.findAll("td")[4].text
        drawn = i.findAll("td")[5].text
        lost = i.findAll("td")[6].text
        goals_for = i.findAll("td", {"class": "hideSmall"})[0].text
        goals_against = i.findAll("td", {"class": "hideSmall"})[1].text
        points = i.find("td", {"class": "points"}).text
        data = datetime.datetime.strftime(datetime.datetime.now(), "%Y.%m.%d")
        dic = {'position': position, 'club_name': club_name, 'club_stat_url': club_stat_url, 'game': game,
               'won': won, 'drawn': drawn, 'lost': lost, 'goals_for': goals_for, 'goals_against': goals_against,
               'points': points, 'data': data}

        print(dic)
England_parser()