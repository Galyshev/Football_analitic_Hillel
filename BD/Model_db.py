from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from BD.alchemy import Base


class England(Base):
    __tablename__ = "england_table"

    id = Column(Integer, primary_key=True)
    position = Column(Integer)
    club_name = Column(String)
    game = Column(Integer)
    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    points = Column(Integer)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, position, club_name, game, won, drawn, lost, goals_for, goals_against, points):
        self.position = position
        self.club_name = club_name
        self.game = game
        self.won = won
        self.drawn = drawn
        self.lost = lost
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.points = points


class Germany(Base):
    __tablename__ = "germany_table"

    id = Column(Integer, primary_key=True)
    position = Column(Integer)
    club_name = Column(String)
    game = Column(Integer)
    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    points = Column(Integer)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, position, club_name, game, won, drawn, lost, goals_for, goals_against, points):
        self.position = position
        self.club_name = club_name
        self.game = game
        self.won = won
        self.drawn = drawn
        self.lost = lost
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.points = points

class France(Base):
    __tablename__ = "france_table"

    id = Column(Integer, primary_key=True)
    position = Column(Integer)
    club_name = Column(String)
    game = Column(Integer)
    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    points = Column(Integer)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, position, club_name, game, won, drawn, lost, goals_for, goals_against, points):
        self.position = position
        self.club_name = club_name
        self.game = game
        self.won = won
        self.drawn = drawn
        self.lost = lost
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.points = points


class Spain(Base):
    __tablename__ = "spain_table"

    id = Column(Integer, primary_key=True)
    position = Column(Integer)
    club_name = Column(String)
    game = Column(Integer)
    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    points = Column(Integer)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, position, club_name, game, won, drawn, lost, goals_for, goals_against, points):
        self.position = position
        self.club_name = club_name
        self.game = game
        self.won = won
        self.drawn = drawn
        self.lost = lost
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.points = points


class Italy(Base):
    __tablename__ = "italy_table"

    id = Column(Integer, primary_key=True)
    position = Column(Integer)
    club_name = Column(String)
    game = Column(Integer)
    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    points = Column(Integer)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, position, club_name, game, won, drawn, lost, goals_for, goals_against, points):
        self.position = position
        self.club_name = club_name
        self.game = game
        self.won = won
        self.drawn = drawn
        self.lost = lost
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.points = points


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    password = Column(String)
    email = Column(String)

    def __init__(self, user, password, email):
        self.user = user
        self.password = password
        self.email = email

class Statistics(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True)
    yellow_card = Column(Integer)
    red_card = Column(Integer)
    shot = Column(Integer)
    shot_on_target = Column(Integer)
    passing = Column(Integer)
    passing_completed = Column(Integer)
    fouls = Column(Integer)
    game = Column(Integer)
    country = Column(String)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, yellow_card, red_card, shot, shot_on_target, passing, passing_completed, fouls, game, country):
        self.yellow_card = yellow_card
        self.red_card = red_card
        self.shot = shot
        self.shot_on_target = shot_on_target
        self.passing = passing
        self.passing_completed = passing_completed
        self.fouls = fouls
        self.game = game
        self.country = country

class Club_Statistics(Base):
    __tablename__ = "statistics_club"

    id = Column(Integer, primary_key=True)
    shots_on_target_pct = Column(Float)
    average_shot_distance = Column(Float)
    passes_pct = Column(Float)
    passes_pct_short = Column(Float)
    passes_pct_medium = Column(Float)
    passes_pct_long = Column(Float)
    fouls = Column(Integer)
    cards_yellow = Column(Integer)
    goals_per_shot_on_target = Column(Float)
    sca_per90 = Column(Float)
    country = Column(String)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, shots_on_target_pct, average_shot_distance, passes_pct, passes_pct_short, passes_pct_medium,
                 passes_pct_long, fouls, cards_yellow, country, goals_per_shot_on_target, sca_per90):
        self.shots_on_target_pct = shots_on_target_pct
        self.average_shot_distance = average_shot_distance
        self.passes_pct = passes_pct
        self.passes_pct_short = passes_pct_short
        self.passes_pct_medium = passes_pct_medium
        self.passes_pct_long = passes_pct_long
        self.fouls = fouls
        self.cards_yellow = cards_yellow
        self.country = country
        self.goals_per_shot_on_target = goals_per_shot_on_target
        self.sca_per90 = sca_per90