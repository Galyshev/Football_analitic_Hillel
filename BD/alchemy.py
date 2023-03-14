import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

# try:
#     engine = create_engine(f'postgresql+psycopg2://{os.environ.get("DB_USER", "postgres")}:'
#                            f'{os.environ.get("DB_PASSWORD", "postgres")}'
#                            f'@{os.environ.get("DB_HOST", "127.0.0.1")}:5432/')
#     connection = engine.connect()
#
# except sqlalchemy.exc.OperationalError:
#     print("Database doesn't exists or username/password incorrect")
#     input("Press any key to continue...")
# else:
#     print("OK")
#     input("Press any key to continue...")

engine = create_engine(f'postgresql+psycopg2://{os.environ.get("DB_USER", "postgres")}:'
                       f'{os.environ.get("DB_PASSWORD", "postgres")}'
                       f'@{os.environ.get("DB_HOST", "127.0.0.1")}:5432/football_analitics')

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from BD import Model_db
    Base.metadata.create_all(bind=engine)