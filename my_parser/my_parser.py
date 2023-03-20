import chromedriver_autoinstaller
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
        game = i.findAll("td")[3].text
        won = i.findAll("td")[4].text
        drawn = i.findAll("td")[5].text
        lost = i.findAll("td")[6].text
        goals_for = i.findAll("td", {"class": "hideSmall"})[0].text
        goals_against = i.findAll("td", {"class": "hideSmall"})[1].text
        points = i.find("td", {"class": "points"}).text

        insert_query = Model_db.England(position=position, club_name=club_name,
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

        insert_query = Model_db.Germany(position=position, club_name=club_name,
                                        game=game, won=won, drawn=drawn, lost=lost, goals_for=goals_for,
                                        goals_against=goals_against, points=points)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()


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

        insert_query = Model_db.Spain(position=position, club_name=club_name,
                                      game=game, won=won, drawn=drawn, lost=lost, goals_for=goals_for,
                                      goals_against=goals_against, points=points)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()


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

        insert_query = Model_db.France(position=position, club_name=club_name,
                                       game=game, won=won, drawn=drawn, lost=lost, goals_for=goals_for,
                                       goals_against=goals_against, points=points)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()


def italy_parser():
    site = 'https://www.legaseriea.it/en/serie-a/classifica'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # executable_path = 'chromedriver.exe'
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome(executable_path = executable_path, options=chrome_options)
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

        insert_query = Model_db.Italy(position=position, club_name=club_name,
                                      game=game, won=won, drawn=drawn, lost=lost, goals_for=goals_for,
                                      goals_against=goals_against, points=points)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()


def statistics_parser():
    site_list = ['https://fbref.com/en/comps/13/Ligue-1-Stats', 'https://fbref.com/en/comps/9/Premier-League-Stats',
                 'https://fbref.com/en/comps/12/La-Liga-Stats', 'https://fbref.com/en/comps/11/Serie-A-Stats',
                 'https://fbref.com/en/comps/20/Bundesliga-Stats']
    country_dic = {1: 'France', 2: 'England', 3: 'Spain', 4: 'Italy', 5: 'Germany'}
    flag = 1

    # так как данные тянутся с таблицы всегда актуальные, нет смысла обновлять базу, проще удалить данные и записать по новой
    # так точно не будет дублирований
    db_session.execute(sa_text('TRUNCATE TABLE statistics').execution_options(autocommit=True))

    for site in site_list:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = site
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        # удары
        content = soup.findAll("table", {"id": "stats_squads_shooting_for"})
        shots = []
        for i in content:
            cont = i.findAll("td", {"data-stat": "shots"})
            for y in cont:
                shots.append(int(y.text))
        shots_on_target = []
        for i in content:
            cont = i.findAll("td", {"data-stat": "shots_on_target"})
            for y in cont:
                shots_on_target.append(int(y.text))

        # пасы
        content = soup.findAll("table", {"id": "stats_squads_passing_for"})
        passing = []
        for i in content:
            cont = i.findAll("td", {"data-stat": "passes"})
            for y in cont:
                passing.append(int(y.text))
        passing_completed = []
        for i in content:
            cont = i.findAll("td", {"data-stat": "passes_completed"})
            for y in cont:
                passing_completed.append(int(y.text))

        # фолы
        content = soup.findAll("table", {"id": "stats_squads_misc_for"})
        fouls = []
        for i in content:
            cont = i.findAll("td", {"data-stat": "fouls"})
            for y in cont:
                fouls.append(int(y.text))
        yellow_card = []
        for i in content:
            cont = i.findAll("td", {"data-stat": "cards_yellow"})
            for y in cont:
                yellow_card.append(int(y.text))
        red_card = []
        for i in content:
            cont = i.findAll("td", {"data-stat": "cards_red"})
            for y in cont:
                red_card.append(int(y.text))

        # игры
        content = soup.findAll("table", {"id": "stats_squads_standard_for"})
        games = []
        for i in content:
            cont = i.findAll("td", {"data-stat": "games"})
            for y in cont:
                games.append(int(y.text))

        country = country_dic[flag]

        insert_query = Model_db.Statistics(yellow_card=sum(yellow_card), red_card=sum(red_card), shot=sum(shots),
                                           shot_on_target=sum(shots_on_target), passing=sum(passing), country=country,
                                           passing_completed=sum(passing_completed), fouls=sum(fouls), game=sum(games))
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()
        flag += 1


def club_statistics_parser():
    site_list = ['https://fbref.com/en/comps/13/Ligue-1-Stats', 'https://fbref.com/en/comps/9/Premier-League-Stats',
                 'https://fbref.com/en/comps/12/La-Liga-Stats', 'https://fbref.com/en/comps/11/Serie-A-Stats',
                 'https://fbref.com/en/comps/20/Bundesliga-Stats']
    id_tablelist = ["results2022-2023131_overall", "results2022-202391_overall",
                    "results2022-2023121_overall", "results2022-2023111_overall",
                    "results2022-2023201_overall"]
    country = ['France', 'England', 'Spain', 'Italy', 'Germany']
    flag = 0

    db_session.execute(sa_text('TRUNCATE TABLE statistics_club').execution_options(autocommit=True))

    for site in site_list:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = site
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        clubs = []
        id_table = id_tablelist[flag]
        content = soup.findAll("table", {"id": id_table})
        for i in content:
            club = i.findAll("td", {"data-stat": "team"})
            for y in club:
                clubs.append(y.text)
        FIRST_CLUB_NAME = str(clubs[0]).strip()
        rez = {}

        # удары
        value1 = []
        value2 = []
        name_club = []
        content = soup.findAll("table", {"id": "stats_squads_shooting_for"})
        for i in content:
            club = i.findAll("th", {"data-stat": "team"})[1:]
            for y in club:
                name_club.append(y.text)
            cont = i.findAll("td", {"data-stat": "shots_on_target_pct"})
            for y in cont:
                value1.append(y.text)
            cont = i.findAll("td", {"data-stat": "average_shot_distance"})
            for y in cont:
                value2.append(y.text)

        for i in range(len(name_club)):
            name = name_club[i]
            if FIRST_CLUB_NAME == name:
                rez['shots_on_target_pct'] = float(value1[i])
                rez['average_shot_distance'] = round((float(value2[i]) * 0.9144), 2)

        # пасы
        tmp1 = []
        tmp2 = []
        value1 = []
        value2 = []
        name_club = []
        content = soup.findAll("table", {"id": "stats_squads_passing_for"})
        for i in content:
            club = i.findAll("th", {"data-stat": "team"})[1:]
            for y in club:
                name_club.append(y.text)
            cont = i.findAll("td", {"data-stat": "passes_pct"})
            for y in cont:
                value1.append(y.text)
            cont = i.findAll("td", {"data-stat": "passes_pct_short"})
            for y in cont:
                value2.append(y.text)
            cont = i.findAll("td", {"data-stat": "passes_pct_medium"})
            for y in cont:
                tmp1.append(y.text)
            cont = i.findAll("td", {"data-stat": "passes_pct_long"})
            for y in cont:
                tmp2.append(y.text)
        for i in range(len(name_club)):
            name = name_club[i]
            if FIRST_CLUB_NAME == name:
                rez['passes_pct'] = float(value1[i])
                rez['passes_pct_short'] = float(value2[i])
                rez['passes_pct_medium'] = float(tmp1[i])
                rez['passes_pct_long'] = float(tmp2[i])

        # фолы
        value1 = []
        value2 = []
        name_club = []
        content = soup.findAll("table", {"id": "stats_squads_misc_for"})
        for i in content:
            club = i.findAll("th", {"data-stat": "team"})[1:]
            for y in club:
                name_club.append(y.text)
            cont = i.findAll("td", {"data-stat": "fouls"})
            for y in cont:
                value1.append(y.text)
            cont = i.findAll("td", {"data-stat": "cards_yellow"})
            for y in cont:
                value2.append(y.text)

        for i in range(len(name_club)):
            name = name_club[i]
            if FIRST_CLUB_NAME == name:
                rez['fouls'] = int(value1[i])
                rez['cards_yellow'] = int(value2[i])

        # гол на удары в створ
        value1 = []
        name_club = []
        content = soup.findAll("table", {"id": "stats_squads_shooting_for"})
        for i in content:
            club = i.findAll("th", {"data-stat": "team"})[1:]
            for y in club:
                name_club.append(y.text)
            cont = i.findAll("td", {"data-stat": "goals_per_shot_on_target"})
            for y in cont:
                value1.append(y.text)

        for i in range(len(name_club)):
            name = name_club[i]
            if FIRST_CLUB_NAME == name:
                rez['goals_per_shot_on_target'] = float(value1[i])

        # атакующие действия
        value1 = []
        name_club = []
        content = soup.findAll("table", {"id": "stats_squads_gca_for"})
        for i in content:
            club = i.findAll("th", {"data-stat": "team"})[1:]
            for y in club:
                name_club.append(y.text)
            cont = i.findAll("td", {"data-stat": "sca_per90"})
            for y in cont:
                value1.append(y.text)

        for i in range(len(name_club)):
            name = name_club[i]
            if FIRST_CLUB_NAME == name:
                rez['sca_per90'] = float(value1[i])

        countr = country[flag]

        insert_query = Model_db.Club_Statistics(shots_on_target_pct=rez['shots_on_target_pct'],
                                                average_shot_distance=rez['average_shot_distance'],
                                                passes_pct=rez['passes_pct'],
                                                passes_pct_short=rez['passes_pct_short'],
                                                passes_pct_medium=rez['passes_pct_medium'],
                                                passes_pct_long=rez['passes_pct_long'], fouls=rez['fouls'],
                                                cards_yellow=rez['cards_yellow'],
                                                country=countr,
                                                goals_per_shot_on_target=rez['goals_per_shot_on_target'],
                                                sca_per90=rez['sca_per90'])
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()

        flag += 1

# england_parser()
# german_parser()
# spain_parser()
# france_parser()
# italy_parser()
# statistics_parser()
# first_club_name()
# club_statistics_parser()
