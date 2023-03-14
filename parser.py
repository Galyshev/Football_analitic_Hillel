from user_agent import generate_user_agent
import requests
from bs4 import BeautifulSoup

def England_parser():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.premierleague.com/tables'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    first_club_content = soup.find("tr", {"class": "tableDark"})
    other_club_content = soup.findAll("tr", {"class": "tableMid"})
    print(first_club_content)
    position = first_club_content.find("span", {"class": "value"}).text
    club_name = first_club_content.find("span", {"class": "long"}).text
    club_site = first_club_content.find("a")['href']
    tmp = club_site.replace('overview', 'stats')
    club_stat_url = 'https://www.premierleague.com' + tmp
    print(club_stat_url)


England_parser()