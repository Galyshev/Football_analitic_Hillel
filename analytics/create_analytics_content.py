import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from BD.alchemy import db_session
from BD.Model_db import England, Germany, France, Spain, Italy
from sqlalchemy.sql import text as sa_text


def query_DB(query):
    query = db_session.execute(sa_text(query))
    rez = query.fetchone()
    return rez

def create_graph(dic, colnames, name_file):
    frame = pd.DataFrame.from_dict(dic, orient='index', columns=colnames)
    print(frame)

    file = "../static/" + name_file + ".png"
    plt.figure()
    swarm_plot = sns.barplot(data=frame, x=colnames[0], y=colnames[1])
    swarm_plot.bar_label(swarm_plot.containers[0])
    # plt.show()
    plt.savefig(file, dpi=600)

def ranking_club():
    best_club_e = db_session.query(England.club_name).filter(
        England.position == 1).all()[0][0]
    best_club_s = db_session.query(Spain.club_name).filter(
        Spain.position == 1).all()[0][0]
    best_club_i = db_session.query(Italy.club_name).filter(
        Italy.position == 1).all()[0][0]
    best_club_g = db_session.query(Germany.club_name).filter(
        Germany.position == 1).all()[0][0]
    best_club_f = db_session.query(France.club_name).filter(
        France.position == 1).all()[0][0]
    rezult_dic = {'best_club_e': best_club_e, 'best_club_s': best_club_s, 'best_club_i': best_club_i,
                  'best_club_g': best_club_g, 'best_club_f': best_club_f}
    return rezult_dic

def analytics_content_country():
    # Забиваемые голы, в среднем за игру (атака чемпионата)
    goal_for_e = round(query_DB('select (sum(goals_for) / sum(game)::float) as goal from england_table;')[0], 3)
    goal_for_s = round(query_DB('select (sum(goals_for) / sum(game)::float) as goal from spain_table;')[0], 3)
    goal_for_i = round(query_DB('select (sum(goals_for) / sum(game)::float) as goal from italy_table;')[0], 3)
    goal_for_g = round(query_DB('select (sum(goals_for) / sum(game)::float) as goal from germany_table;')[0], 3)
    goal_for_f = round(query_DB('select (sum(goals_for) / sum(game)::float) as goal from france_table;')[0], 3)

    goal_for_dic = {'1': ['France', goal_for_f],
                    '2': ['England', goal_for_e],
                    '3': ['Spain', goal_for_s],
                    '4': ['Italy', goal_for_i],
                    '5': ['Germany', goal_for_g]}

    create_graph(goal_for_dic, ['страна', 'голы за игру'], 'goal')


    #  Самые точные в передачах
    passes_e = round(
        query_DB("select (passing_completed / passing::float) as col from statistics where country = 'England';")[0],
        2) * 100
    passes_s = round(
        query_DB("select (passing_completed / passing::float) as col from statistics where country = 'Spain';")[0],
        2) * 100
    passes_i = round(
        query_DB("select (passing_completed / passing::float) as col from statistics where country = 'Italy';")[0],
        2) * 100
    passes_g = round(
        query_DB("select (passing_completed / passing::float) as col from statistics where country = 'Germany';")[0],
        2) * 100
    passes_f = round(
        query_DB("select (passing_completed / passing::float) as col from statistics where country = 'France';")[0],
        2) * 100

    passes_dic = {'1': ['France', passes_f],
                  '2': ['England', passes_e],
                  '3': ['Spain', passes_s],
                  '4': ['Italy', passes_i],
                  '5': ['Germany', passes_g]}

    create_graph(passes_dic, ['страна', 'точность в передачах'], 'passes')

    #  Самые недисциплинированные
    fouls_e = round(
        query_DB("select (fouls / game::float) from statistics  where country = 'England';")[0], 2)
    fouls_s = round(
        query_DB("select (fouls / game::float) from statistics  where country = 'Spain';")[0], 2)
    fouls_i = round(
        query_DB("select (fouls / game::float) from statistics  where country = 'Italy';")[0], 2)
    fouls_g = round(
        query_DB("select (fouls / game::float) from statistics  where country = 'Germany';")[0], 2)
    fouls_f = round(
        query_DB("select (fouls / game::float) from statistics  where country = 'France';")[0], 2)

    fouls_dic = {'1': ['France', fouls_f],
                 '2': ['England', fouls_e],
                 '3': ['Spain', fouls_s],
                 '4': ['Italy', fouls_i],
                 '5': ['Germany', fouls_g]}

    create_graph(fouls_dic, ['страна', 'фолы за игру'], 'fouls')

    #  Самые грубые
    yellow_card_e = round(
        query_DB("select (yellow_card / game::float) from statistics  where country = 'England';")[0], 2)
    yellow_card_s = round(
        query_DB("select (yellow_card / game::float) from statistics  where country = 'Spain';")[0], 2)
    yellow_card_i = round(
        query_DB("select (yellow_card / game::float) from statistics  where country = 'Italy';")[0], 2)
    yellow_card_g = round(
        query_DB("select (yellow_card / game::float) from statistics  where country = 'Germany';")[0], 2)
    yellow_card_f = round(
        query_DB("select (yellow_card / game::float) from statistics  where country = 'France';")[0], 2)

    yellow_card_dic = {'1': ['France', yellow_card_f],
                       '2': ['England', yellow_card_e],
                       '3': ['Spain', yellow_card_s],
                       '4': ['Italy', yellow_card_i],
                       '5': ['Germany', yellow_card_g]}

    create_graph(yellow_card_dic, ['страна', 'желтые карточки за игру'], 'yellow_card')

    #  Самые точные в ударах
    shot_e = round(
        query_DB("select (shot_on_target / shot::float) from statistics  where country = 'England';")[0], 2) * 100
    shot_s = round(
        query_DB("select (shot_on_target / shot::float) from statistics  where country = 'Spain';")[0], 2) * 100
    shot_i = round(
        query_DB("select (shot_on_target / shot::float) from statistics  where country = 'Italy';")[0], 2) * 100
    shot_g = round(
        query_DB("select (shot_on_target / shot::float) from statistics  where country = 'Germany';")[0], 2) * 100
    shot_f = round(
        query_DB("select (shot_on_target / shot::float) from statistics  where country = 'France';")[0], 2) * 100

    shot_dic = {'1': ['France', shot_f],
                '2': ['England', shot_e],
                '3': ['Spain', shot_s],
                '4': ['Italy', shot_i],
                '5': ['Germany', shot_g]}

    create_graph(shot_dic, ['страна', 'точность ударов'], 'shot')

    #  ударов на гол
    goal_all_e = query_DB('select sum(goals_for) from england_table;')[0]
    goal_all_s = query_DB('select sum(goals_for) from spain_table;')[0]
    goal_all_i = query_DB('select sum(goals_for) from italy_table;')[0]
    goal_all_g = query_DB('select sum(goals_for) from germany_table;')[0]
    goal_all_f = query_DB('select sum(goals_for) from france_table;')[0]

    shot_all_e = query_DB("select shot from statistics where country = 'England';")[0]
    shot_all_s = query_DB("select shot from statistics where country = 'Spain';")[0]
    shot_all_i = query_DB("select shot from statistics where country = 'Italy';")[0]
    shot_all_g = query_DB("select shot from statistics where country ='Germany';")[0]
    shot_all_f = query_DB("select shot from statistics where country ='France';")[0]

    shot_per_goal_e = round(shot_all_e / goal_all_e, 2)
    shot_per_goal_s = round(shot_all_s / goal_all_s, 2)
    shot_per_goal_i = round(shot_all_i / goal_all_i, 2)
    shot_per_goal_g = round(shot_all_g / goal_all_g, 2)
    shot_per_goal_f = round(shot_all_f / goal_all_f, 2)

    shot_per_goal_dic = {'1': ['France', shot_per_goal_f],
                         '2': ['England', shot_per_goal_e],
                         '3': ['Spain', shot_per_goal_s],
                         '4': ['Italy', shot_per_goal_i],
                         '5': ['Germany', shot_per_goal_g]}

    create_graph(shot_per_goal_dic, ['страна', 'ударов до гола'], 'shot_per_goal')


def analytics_content_club():
    # Клубы на 1 месте забивают за игру
    goal_club_e = db_session.query(England.club_name, England.goals_for, England.game).filter(
        England.position == 1).all()
    goal_club_s = db_session.query(Spain.club_name, Spain.goals_for, Spain.game).filter(Spain.position == 1).all()
    goal_club_i = db_session.query(Italy.club_name, Italy.goals_for, Italy.game).filter(Italy.position == 1).all()
    goal_club_g = db_session.query(Germany.club_name, Germany.goals_for, Germany.game).filter(
        Germany.position == 1).all()
    goal_club_f = db_session.query(France.club_name, France.goals_for, France.game).filter(France.position == 1).all()

    goal_club_e_dic = {'1': [goal_club_f[0][0], round(goal_club_f[0][1] / goal_club_f[0][2], 2)],
                       '2': [goal_club_e[0][0], round(goal_club_e[0][1] / goal_club_e[0][2], 2)],
                       '3': [goal_club_s[0][0], round(goal_club_s[0][1] / goal_club_s[0][2], 2)],
                       '4': [goal_club_i[0][0], round(goal_club_i[0][1] / goal_club_i[0][2], 2)],
                       '5': [goal_club_g[0][0], round(goal_club_g[0][1] / goal_club_g[0][2], 2)]}

    create_graph(goal_club_e_dic, ['клуб', 'гол за игру'], 'club_goal_for')

    # Клубы на 1 месте пропускают за игру
    goals_against_club_e = db_session.query(England.club_name, England.goals_against, England.game).filter(
        England.position == 1).all()
    goals_against_club_s = db_session.query(Spain.club_name, Spain.goals_against, Spain.game).filter(
        Spain.position == 1).all()
    goals_against_club_i = db_session.query(Italy.club_name, Italy.goals_against, Italy.game).filter(
        Italy.position == 1).all()
    goals_against_club_g = db_session.query(Germany.club_name, Germany.goals_against, Germany.game).filter(
        Germany.position == 1).all()
    goals_against_club_f = db_session.query(France.club_name, France.goals_against, France.game).filter(
        France.position == 1).all()

    goals_against_club_e_dic = {
        '1': [goals_against_club_f[0][0], round(goals_against_club_f[0][1] / goals_against_club_f[0][2], 2)],
        '2': [goals_against_club_e[0][0], round(goals_against_club_e[0][1] / goals_against_club_e[0][2], 2)],
        '3': [goals_against_club_s[0][0], round(goals_against_club_s[0][1] / goals_against_club_s[0][2], 2)],
        '4': [goals_against_club_i[0][0], round(goals_against_club_i[0][1] / goals_against_club_i[0][2], 2)],
        '5': [goals_against_club_g[0][0], round(goals_against_club_g[0][1] / goals_against_club_g[0][2], 2)]}

    create_graph(goals_against_club_e_dic, ['клуб', 'гол за игру'], 'club_against_for')

def ranking_club():
    best_club_e = db_session.query(England.club_name).filter(
        England.position == 1).all()[0][0]
    best_club_s = db_session.query(Spain.club_name).filter(
        Spain.position == 1).all()[0][0]
    best_club_i = db_session.query(Italy.club_name).filter(
        Italy.position == 1).all()[0][0]
    best_club_g = db_session.query(Germany.club_name).filter(
        Germany.position == 1).all()[0][0]
    best_club_f = db_session.query(France.club_name).filter(
        France.position == 1).all()[0][0]
    rezult_dic = {'best_club_e': best_club_e, 'best_club_s': best_club_s, 'best_club_i': best_club_i,
                  'best_club_g': best_club_g, 'best_club_f': best_club_f}
    return rezult_dic
if __name__ == '__main__':
    analytics_content_country()
    # analytics_content_club()
    # ranking_club()
