from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship , sessionmaker
from Credentials import get_connection_string
import json
import pyodbc
import datetime
from flask_cors import CORS

Base = declarative_base()

connection_string = get_connection_string() #f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

class Game(Base):
    __tablename__ = 'Games'

    game_id = Column(Integer, primary_key=True)
    game_date = Column(DateTime)

    Players = relationship("Player", back_populates="Games")

class Player(Base):
    __tablename__ = 'Players'

    player_id = Column(Integer, primary_key=True)
    player_name = Column(String(255))
    player_hand = Column(String(255), nullable=True)
    is_winner = Column(Boolean, nullable=True)
    
    game_id = Column(Integer, ForeignKey('Games.game_id'))

    Games = relationship("Game", back_populates="Players")

engine = create_engine(connection_string)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def new_game(players_names):
    new_game = Game(game_date = datetime.datetime.now())
    session.add(new_game)
    session.commit()

    new_players = [
            Player(player_name=players_names['player_one'], game_id=new_game.game_id),
            Player(player_name=players_names['player_two'], game_id=new_game.game_id),
            Player(player_name=players_names['player_three'], game_id=new_game.game_id),
            Player(player_name=players_names['player_four'], game_id=new_game.game_id)
        ]

    session.add_all(new_players)
    x = session.new
    session.commit()

    players_json = [{
            "player_id":player.player_id,
            "game_id": player.game_id,
            "player_name":player.player_name,
            "player_hand": player.player_hand,
            "is_winner":player.is_winner
        }
        for player in x
    ]
    json_result = json.dumps(players_json, indent=4)
    
    session.close()

    return json_result
