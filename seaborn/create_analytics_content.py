import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from BD.alchemy import db_session
from BD import Model_db
from sqlalchemy.sql import text as sa_text


def query_DB(query):
    query = db_session.execute(sa_text(query))
    rez = query.fetchone()
    return rez


def create_graph(dic, colnames, name_file):
    frame = pd.DataFrame.from_dict(dic, orient='index', columns=colnames)
    print(frame)

    swarm_plot = sns.barplot(data=frame, x=colnames[0], y=colnames[1])  # ,estimator=np.sum
    swarm_plot.bar_label(swarm_plot.containers[0])
    fig = swarm_plot.get_figure()
    plt.show()
    file = "./pic/" + name_file + ".png"
    fig.savefig(file, dpi=600)


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

    #  Самые миролюбивые (больше всех ничьих)
    drawn_e = round(query_DB('select avg(drawn)from england_table;')[0], 2)
    drawn_s = round(query_DB('select avg(drawn) from spain_table;')[0], 2)
    drawn_i = round(query_DB('select avg(drawn) from italy_table;')[0], 2)
    drawn_g = round(query_DB('select avg(drawn) from germany_table;')[0], 2)
    drawn_f = round(query_DB('select avg(drawn) from france_table;')[0], 2)

    drawn_dic = {'1': ['France', drawn_f],
                 '2': ['England', drawn_e],
                 '3': ['Spain', drawn_s],
                 '4': ['Italy', drawn_i],
                 '5': ['Germany', drawn_g]}

    create_graph(drawn_dic, ['страна', 'игры в ничью'], 'drawn')

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


if __name__ == '__main__':
    analytics_content_country()
