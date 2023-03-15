from sqlalchemy.sql import text as sa_text
from BD.alchemy import db_session
import requests
from bs4 import BeautifulSoup
from BD import Model_db
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def england_parser():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.premierleague.com/tables'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    club_content = soup.findAll("tr", {"data-compseason": "489"})

    # так как данные тянутся с таблицы всегда актуальные, нет смысла обновлять базу, проще удалить данные и записать по новой
    # так точно не будет дублирований
    db_session.execute(sa_text('TRUNCATE TABLE england_table').execution_options(autocommit=True))

    # вытягивание данных и запись в базу
    for i in club_content:
        position = i.find("span", {"class": "value"}).text
        club_name = i.find("span", {"class": "long"}).text
        part_club_site = i.find("a")['href']
        club_url = 'https://www.premierleague.com' + part_club_site
        game = i.findAll("td")[3].text
        won = i.findAll("td")[4].text
        drawn = i.findAll("td")[5].text
        lost = i.findAll("td")[6].text
        goals_for = i.findAll("td", {"class": "hideSmall"})[0].text
        goals_against = i.findAll("td", {"class": "hideSmall"})[1].text
        points = i.find("td", {"class": "points"}).text

        insert_query = Model_db.England(position=position, club_name=club_name, club_stat_url=club_url,
                                         game=game, won=won, drawn=drawn, lost=lost, goals_for=goals_for,
                                        goals_against=goals_against, points=points)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()

def german_parser():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.bundesliga.com/en/bundesliga/table'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    club_content = soup.findAll("tr", {"class": "ng-star-inserted"})

    # так как данные тянутся с таблицы всегда актуальные, нет смысла обновлять базу, проще удалить данные и записать по новой
    # так точно не будет дублирований
    db_session.execute(sa_text('TRUNCATE TABLE germany_table').execution_options(autocommit=True))

    # вытягивание данных и запись в базу
    for i in club_content:
        position = i.find("td", {"class": "rank"}).text
        club_name = i.find("span", {"class": "d-none d-sm-inline-block"}).text
        game = i.find("td", {"class": "matches"}).text
        won = i.find("td", {"class": "wins"}).text
        drawn = i.find("td", {"class": "draws"}).text
        lost = i.find("td", {"class": "losses"}).text
        goals = i.find("td", {"class": "goals"}).text
        goals_for = str(goals).split(':')[0]
        goals_against = str(goals).split(':')[-1]
        points = i.find("td", {"class": "pts"}).text
        tmp_site = i.find("a", {"class": "logolink"})['href']
        club_site = 'https://www.bundesliga.com' + tmp_site

        insert_query = Model_db.Germany(position=position, club_name=club_name, club_stat_url=club_site,
                                        game=game, won=won, drawn=drawn, lost=lost, goals_for=goals_for,
                                        goals_against=goals_against, points=points)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()

def spain_club_site_parser():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.laliga.com/en-GB/laliga-santander/clubs'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    club_site_content = soup.findAll("div", {"class": "styled__ItemContainer-fyva03-1"})
    dic = {}
    for i in club_site_content:
        link = i.find("a", {"class": "link"})['href']
        site_stat = 'https://www.laliga.com' + link
        name_club = i.find("h2").text
        dic[name_club] = site_stat
    return dic

def spain_parser():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.laliga.com/en-GB/laliga-santander/standing'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    club_content = soup.findAll("div", {"class": "styled__ContainerAccordion-e89col-11 HquGF"})[0:20]

    # так как данные тянутся с таблицы всегда актуальные, нет смысла обновлять базу, проще удалить данные и записать по новой
    # так точно не будет дублирований
    db_session.execute(sa_text('TRUNCATE TABLE spain_table').execution_options(autocommit=True))

    # вытягивание данных и запись в базу
    for i in club_content:
        position = i.find("p", {"class": "fciXFy"}).text
        club_name = i.findAll("p", {"class": "styled__TextRegularStyled-sc-1raci4c-0 glrfl"})[1].text
        game = i.findAll("div", {"class": "styled__Td-e89col-10 gETuZs"})[1].text
        won = i.findAll("div", {"class": "styled__Td-e89col-10 gETuZs"})[2].text
        drawn = i.findAll("div", {"class": "styled__Td-e89col-10 gETuZs"})[3].text
        lost = i.findAll("div", {"class": "styled__Td-e89col-10 gETuZs"})[4].text
        goals_for = i.findAll("div", {"class": "styled__Td-e89col-10 gETuZs"})[5].text
        goals_against = i.findAll("div", {"class": "styled__Td-e89col-10 gETuZs"})[6].text
        points = i.findAll("div", {"class": "styled__Td-e89col-10 gETuZs"})[0].text
        dic_site = spain_club_site_parser()
        club_site = dic_site[club_name]

        insert_query = Model_db.Spain(position=position, club_name=club_name, club_stat_url=club_site,
                                        game=game, won=won, drawn=drawn, lost=lost, goals_for=goals_for,
                                        goals_against=goals_against, points=points)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()
        print(club_site)
        print('///////////////////////////////////////')

def france_parser():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.ligue1.com/ranking'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    club_content = soup.findAll("li", {"class": "GeneralStats-row"})

    # так как данные тянутся с таблицы всегда актуальные, нет смысла обновлять базу, проще удалить данные и записать по новой
    # так точно не будет дублирований
    db_session.execute(sa_text('TRUNCATE TABLE france_table').execution_options(autocommit=True))

    # вытягивание данных и запись в базу
    for i in club_content:
        position = i.find("div", {"class": "GeneralStats-item"}).text
        club_name = i.find("span", {"class": "GeneralStats-clubName desktop-item"}).text
        game = i.findAll("div", {"class": "GeneralStats-item"})[3].text
        won = i.findAll("div", {"class": "GeneralStats-item"})[4].text
        drawn = i.findAll("div", {"class": "GeneralStats-item"})[5].text
        lost = i.findAll("div", {"class": "GeneralStats-item"})[6].text
        goals_for = i.findAll("div", {"class": "GeneralStats-item"})[7].text
        goals_against = i.findAll("div", {"class": "GeneralStats-item"})[8].text
        points = i.find("div", {"class": "GeneralStats-item GeneralStats-item--points"}).text
        part_club_site = i.find("a", {"class": "GeneralStats-link"})['href']
        club_site = 'https://www.ligue1.com' + part_club_site

        insert_query = Model_db.France(position=position, club_name=club_name, club_stat_url=club_site,
                                        game=game, won=won, drawn=drawn, lost=lost, goals_for=goals_for,
                                        goals_against=goals_against, points=points)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()
        # print(won,drawn,lost,  goals_for, goals_against)
        # print('///////////////////////////////////////')

def italy_parser():
    site = 'https://www.legaseriea.it/en/serie-a/classifica'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    executable_path = '.\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
    driver.get(site)

    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource, 'html.parser')
    club_content = soup.findAll("tr", {"class": ""})[1:]

    # так как данные тянутся с таблицы всегда актуальные, нет смысла обновлять базу, проще удалить данные и записать по новой
    # так точно не будет дублирований
    db_session.execute(sa_text('TRUNCATE TABLE italy_table').execution_options(autocommit=True))

    # вытягивание данных и запись в базу
    for i in club_content:
        content = i.findAll("h3")
        position = content[0].text
        club_name = content[1].text
        points = content[3].text
        game = content[4].text
        won = content[5].text
        drawn = content[6].text
        lost = content[7].text
        goals_for = content[8].text
        goals_against = content[9].text
        content_site = i.findAll("a")
        for y in content_site:
            try:
                part_club_site = y['href']
                club_site = 'https://www.legaseriea.it' + part_club_site
            except KeyError:
                pass

        insert_query = Model_db.Italy(position=position, club_name=club_name, club_stat_url=club_site,
                                        game=game, won=won, drawn=drawn, lost=lost, goals_for=goals_for,
                                        goals_against=goals_against, points=points)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()



# england_parser()
# german_parser()
# spain_parser()
# spain_club_site_parser()
# france_parser()
# italy_parser()