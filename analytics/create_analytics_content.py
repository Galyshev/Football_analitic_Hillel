import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from BD.alchemy import db_session
from BD.Model_db import England, Germany, France, Spain, Italy, Club_Statistics
from sqlalchemy.sql import text as sa_text


def query_DB(query):
    query = db_session.execute(sa_text(query))
    rez = query.fetchone()
    return rez


def create_graph(dic, colnames, name_file):
    frame = pd.DataFrame.from_dict(dic, orient='index', columns=colnames)
    print(frame)

    file = "./static/" + name_file + ".png"
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

    # Клубы точность ударов
    shots_on_target_f = db_session.query(Club_Statistics.shots_on_target_pct).filter(
        Club_Statistics.country == 'France').one()
    shots_on_target_e = db_session.query(Club_Statistics.shots_on_target_pct).filter(
        Club_Statistics.country == 'England').one()
    shots_on_target_s = db_session.query(Club_Statistics.shots_on_target_pct).filter(
        Club_Statistics.country == 'Spain').one()
    shots_on_target_i = db_session.query(Club_Statistics.shots_on_target_pct).filter(
        Club_Statistics.country == 'Italy').one()
    shots_on_target_g = db_session.query(Club_Statistics.shots_on_target_pct).filter(
        Club_Statistics.country == 'Germany').one()

    print(shots_on_target_g)

    shots_on_target_dic = {'1': [goal_club_f[0][0], shots_on_target_f[0]],
                           '2': [goal_club_e[0][0], shots_on_target_e[0]],
                           '3': [goal_club_s[0][0], shots_on_target_s[0]],
                           '4': [goal_club_i[0][0], shots_on_target_i[0]],
                           '5': [goal_club_g[0][0], shots_on_target_g[0]]}

    create_graph(shots_on_target_dic, ['клуб', 'точность ударов, %'], 'shots_on_target_club')

    # Клубы - дистанция удров
    average_shot_distance_f = db_session.query(Club_Statistics.average_shot_distance).filter(
        Club_Statistics.country == 'France').one()
    average_shot_distance_e = db_session.query(Club_Statistics.average_shot_distance).filter(
        Club_Statistics.country == 'England').one()
    average_shot_distance_s = db_session.query(Club_Statistics.average_shot_distance).filter(
        Club_Statistics.country == 'Spain').one()
    average_shot_distance_i = db_session.query(Club_Statistics.average_shot_distance).filter(
        Club_Statistics.country == 'Italy').one()
    average_shot_distance_g = db_session.query(Club_Statistics.average_shot_distance).filter(
        Club_Statistics.country == 'Germany').one()

    print(shots_on_target_g)

    shots_on_target_dic = {'1': [goal_club_f[0][0], average_shot_distance_f[0]],
                           '2': [goal_club_e[0][0], average_shot_distance_e[0]],
                           '3': [goal_club_s[0][0], average_shot_distance_s[0]],
                           '4': [goal_club_i[0][0], average_shot_distance_i[0]],
                           '5': [goal_club_g[0][0], average_shot_distance_g[0]]}

    create_graph(shots_on_target_dic, ['клуб', 'дистанция ударов'], 'average_shot_distance_club')

    # Клубы - пас
    passes_pct_f = db_session.query(Club_Statistics.passes_pct).filter(
        Club_Statistics.country == 'France').one()
    passes_pct_e = db_session.query(Club_Statistics.passes_pct).filter(
        Club_Statistics.country == 'England').one()
    passes_pct_s = db_session.query(Club_Statistics.passes_pct).filter(
        Club_Statistics.country == 'Spain').one()
    passes_pct_i = db_session.query(Club_Statistics.passes_pct).filter(
        Club_Statistics.country == 'Italy').one()
    passes_pct_g = db_session.query(Club_Statistics.passes_pct).filter(
        Club_Statistics.country == 'Germany').one()

    passes_pct_dic = {'1': [goal_club_f[0][0], passes_pct_f[0]],
                      '2': [goal_club_e[0][0], passes_pct_e[0]],
                      '3': [goal_club_s[0][0], passes_pct_s[0]],
                      '4': [goal_club_i[0][0], passes_pct_i[0]],
                      '5': [goal_club_g[0][0], passes_pct_g[0]]}

    create_graph(passes_pct_dic, ['клуб', 'точность паса, %'], 'passes_pct')

    # Клубы - короткий пас
    passes_pct_short_f = db_session.query(Club_Statistics.passes_pct_short).filter(
        Club_Statistics.country == 'France').one()
    passes_pct_short_e = db_session.query(Club_Statistics.passes_pct_short).filter(
        Club_Statistics.country == 'England').one()
    passes_pct_short_s = db_session.query(Club_Statistics.passes_pct_short).filter(
        Club_Statistics.country == 'Spain').one()
    passes_pct_short_i = db_session.query(Club_Statistics.passes_pct_short).filter(
        Club_Statistics.country == 'Italy').one()
    passes_pct_short_g = db_session.query(Club_Statistics.passes_pct_short).filter(
        Club_Statistics.country == 'Germany').one()

    passes_pct_short_dic = {'1': [goal_club_f[0][0], passes_pct_short_f[0]],
                            '2': [goal_club_e[0][0], passes_pct_short_e[0]],
                            '3': [goal_club_s[0][0], passes_pct_short_s[0]],
                            '4': [goal_club_i[0][0], passes_pct_short_i[0]],
                            '5': [goal_club_g[0][0], passes_pct_short_g[0]]}

    create_graph(passes_pct_short_dic, ['клуб', 'точность короткого паса, %'], 'passes_pct_short_pct')

    # Клубы - средний пас
    passes_pct_medium_f = db_session.query(Club_Statistics.passes_pct_medium).filter(
        Club_Statistics.country == 'France').one()
    passes_pct_medium_e = db_session.query(Club_Statistics.passes_pct_medium).filter(
        Club_Statistics.country == 'England').one()
    passes_pct_medium_s = db_session.query(Club_Statistics.passes_pct_medium).filter(
        Club_Statistics.country == 'Spain').one()
    passes_pct_medium_i = db_session.query(Club_Statistics.passes_pct_medium).filter(
        Club_Statistics.country == 'Italy').one()
    passes_pct_medium_g = db_session.query(Club_Statistics.passes_pct_medium).filter(
        Club_Statistics.country == 'Germany').one()

    passes_pct_medium_dic = {'1': [goal_club_f[0][0], passes_pct_medium_f[0]],
                             '2': [goal_club_e[0][0], passes_pct_medium_e[0]],
                             '3': [goal_club_s[0][0], passes_pct_medium_s[0]],
                             '4': [goal_club_i[0][0], passes_pct_medium_i[0]],
                             '5': [goal_club_g[0][0], passes_pct_medium_g[0]]}

    create_graph(passes_pct_medium_dic, ['клуб', 'точность среднего паса, %'], 'passes_pct_medium')

    # Клубы - длинный пас
    passes_pct_long_f = db_session.query(Club_Statistics.passes_pct_long).filter(
        Club_Statistics.country == 'France').one()
    passes_pct_long_e = db_session.query(Club_Statistics.passes_pct_long).filter(
        Club_Statistics.country == 'England').one()
    passes_pct_long_s = db_session.query(Club_Statistics.passes_pct_long).filter(
        Club_Statistics.country == 'Spain').one()
    passes_pct_long_i = db_session.query(Club_Statistics.passes_pct_long).filter(
        Club_Statistics.country == 'Italy').one()
    passes_pct_long_g = db_session.query(Club_Statistics.passes_pct_long).filter(
        Club_Statistics.country == 'Germany').one()

    passes_pct_long_dic = {'1': [goal_club_f[0][0], passes_pct_long_f[0]],
                           '2': [goal_club_e[0][0], passes_pct_long_e[0]],
                           '3': [goal_club_s[0][0], passes_pct_long_s[0]],
                           '4': [goal_club_i[0][0], passes_pct_long_i[0]],
                           '5': [goal_club_g[0][0], passes_pct_long_g[0]]}

    create_graph(passes_pct_long_dic, ['клуб', 'точность длинного паса, %'], 'passes_pct_long')

    # Клубы - голов за удар в створ
    goals_per_shot_on_target_f = db_session.query(Club_Statistics.goals_per_shot_on_target).filter(
        Club_Statistics.country == 'France').one()
    goals_per_shot_on_target_e = db_session.query(Club_Statistics.goals_per_shot_on_target).filter(
        Club_Statistics.country == 'England').one()
    goals_per_shot_on_target_s = db_session.query(Club_Statistics.goals_per_shot_on_target).filter(
        Club_Statistics.country == 'Spain').one()
    goals_per_shot_on_target_i = db_session.query(Club_Statistics.goals_per_shot_on_target).filter(
        Club_Statistics.country == 'Italy').one()
    goals_per_shot_on_target_g = db_session.query(Club_Statistics.goals_per_shot_on_target).filter(
        Club_Statistics.country == 'Germany').one()

    goals_per_shot_on_target_dic = {'1': [goal_club_f[0][0], goals_per_shot_on_target_f[0]],
                                    '2': [goal_club_e[0][0], goals_per_shot_on_target_e[0]],
                                    '3': [goal_club_s[0][0], goals_per_shot_on_target_s[0]],
                                    '4': [goal_club_i[0][0], goals_per_shot_on_target_i[0]],
                                    '5': [goal_club_g[0][0], goals_per_shot_on_target_g[0]]}

    create_graph(goals_per_shot_on_target_dic, ['клуб', 'гол за удар в створ'], 'goals_per_shot_on_target')

    # Клубы - полезные атакующие действия
    sca_per90_f = db_session.query(Club_Statistics.sca_per90).filter(
        Club_Statistics.country == 'France').one()
    sca_per90_e = db_session.query(Club_Statistics.sca_per90).filter(
        Club_Statistics.country == 'England').one()
    sca_per90_s = db_session.query(Club_Statistics.sca_per90).filter(
        Club_Statistics.country == 'Spain').one()
    sca_per90_i = db_session.query(Club_Statistics.sca_per90).filter(
        Club_Statistics.country == 'Italy').one()
    sca_per90_g = db_session.query(Club_Statistics.sca_per90).filter(
        Club_Statistics.country == 'Germany').one()

    sca_per90_dic = {'1': [goal_club_f[0][0], sca_per90_f[0]],
                     '2': [goal_club_e[0][0], sca_per90_e[0]],
                     '3': [goal_club_s[0][0], sca_per90_s[0]],
                     '4': [goal_club_i[0][0], sca_per90_i[0]],
                     '5': [goal_club_g[0][0], sca_per90_g[0]]}

    create_graph(sca_per90_dic, ['клуб', 'атакующие действия'], 'sca_per90')


if __name__ == '__main__':
    # analytics_content_country()
    # analytics_content_club()
    ranking_club()
