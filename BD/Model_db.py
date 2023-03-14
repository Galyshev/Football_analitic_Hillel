from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from BD.alchemy import Base


class England(Base):
    __tablename__ = "england_table"

    id = Column(Integer, primary_key=True)
    position = Column(Integer)
    club_name = Column(String)
    club_stat_url = Column(String)
    game = Column(Integer)
    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    points = Column(Integer)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, position, club_name, club_stat_url, game, won, drawn, lost, goals_for, goals_against, points):
        self.position = position
        self.club_name = club_name
        self.club_stat_url = club_stat_url
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
    club_stat_url = Column(String)
    game = Column(Integer)
    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    points = Column(Integer)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, position, club_name, club_stat_url, game, won, drawn, lost, goals_for, goals_against, points):
        self.position = position
        self.club_name = club_name
        self.club_stat_url = club_stat_url
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
    club_stat_url = Column(String)
    game = Column(Integer)
    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    points = Column(Integer)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, position, club_name, club_stat_url, game, won, drawn, lost, goals_for, goals_against, points):
        self.position = position
        self.club_name = club_name
        self.club_stat_url = club_stat_url
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
    club_stat_url = Column(String)
    game = Column(Integer)
    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    points = Column(Integer)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, position, club_name, club_stat_url, game, won, drawn, lost, goals_for, goals_against, points):
        self.position = position
        self.club_name = club_name
        self.club_stat_url = club_stat_url
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
    club_stat_url = Column(String)
    game = Column(Integer)
    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    points = Column(Integer)
    date_add = Column(DateTime, default=datetime.utcnow)

    def __init__(self, position, club_name, club_stat_url, game, won, drawn, lost, goals_for, goals_against, points):
        self.position = position
        self.club_name = club_name
        self.club_stat_url = club_stat_url
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


