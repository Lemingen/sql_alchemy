from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import settings


engine = create_engine(
    url = settings.DATABASE_URL_psycopg,
    echo = False,
    pool_size = 5
)

with engine.connect() as conn:
    #res = conn.execute(text("SELECT VERSION()"))
    #print(f'Версия БД - {res.first()[0]}')
    pass

session_factory = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
