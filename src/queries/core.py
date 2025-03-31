from src.models import metadata_obj, provider_table
from src.database import engine
from sqlalchemy import insert

# ИМПЕРАТИВНЫЙ СПОСОБ

def create():
    metadata_obj.create_all(engine)

def drop():
    metadata_obj.drop_all(engine)

def insert_data():
    with engine.connect() as conn:
        stmt = insert(provider_table).values(
            [
                {#'id_provide': 1,
                 'name_of_provider': 'Selectel',
                 'representative': 'Иванов Иван',
                 'speak_to': 'Гражданин Иванов',
                 'phone': '+79995554433',
                 'address': 'г. Москва, ул. Гоголя, д. 5'
                 },

                {#'id_provide': 2,
                 'name_of_provider': 'STC',
                 'representative': 'Сидоров Сидор',
                 'speak_to': 'Гражданин Сидоров',
                 'phone': '+79994443322',
                 'address': 'г. Санкт-Петербург, ул. Пушкина, д. 7'
                 },

                {#'id_provide': 3,
                 'name_of_provider': 'Timeweb',
                 'representative': 'Джорджов Джордж',
                 'speak_to': 'Гражданин Джорджов',
                 'phone': '+79996443312',
                 'address': 'г. Санкт-Петербург, ул. Самойлова, д. 88'
                 },

                {#'id_provide': 4,
                 'name_of_provider': 'Stormwall',
                 'representative': 'Камилев Камиль',
                 'speak_to': 'Гражданин Камилев',
                 'phone': '+79996443302',
                 'address': 'г. Лондон, ул. Мишуткина, д. 79'
                 },

                {#'id_provide': 5,
                 'name_of_provider': 'IT-Mentor',
                 'representative': 'Аваров Арсен',
                 'speak_to': 'Гражданин Аваров',
                 'phone': '+79987641313',
                 'address': 'г. Анапа, ул. Бабушкина, д. 84'
                 },
            ]
        )
        conn.execute(stmt)
        conn.commit()
