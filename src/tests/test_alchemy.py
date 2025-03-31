from time import time

import pytest
from src.database import session_factory
from sqlalchemy import text
from src.queries.orm import select_data, select_data_join, update_data, insert_line_provider, select_where, select_order_by, select_group_by, select_distinct_dates, joined_load_passports_and_client_id, get_passports_and_client_id
from unittest.mock import MagicMock
from src.models import ProviderOrm

"Тест движка"
def test_connection():
    with session_factory() as sess:
        result = sess.execute(text("SELECT 1"))
        assert result.scalar() == 1


"Тест поставщиков"
@pytest.mark.parametrize("expected", [
    ["Selectel", "STC", "Timeweb", "Stormwall", "IT-Mentor"]
])
def test_select_data(expected):
    """Тест проверяет выборку данных"""
    result = select_data()  # Вызываем функцию
    assert result == expected


"Тест join"
@pytest.mark.parametrize("expected", [
    [[1, 'Selectel', '25.03.1999'], [2, 'Timeweb', '13.06.2005'], [3, 'Stormwall', '09.05.2020'], [4, 'Timeweb', '11.11.1945'], [5, 'STC', '29.04.2025']]
])
def test_select_data_join(expected):
    result = select_data_join()
    assert result == expected

"Тест снифинга where"
def test_select_where_output(capsys):
    select_where()
    captured = capsys.readouterr()
    expected_output = "ID: 2, Name: STC, Representative: Сидоров Сидор, Speak To: Гражданин Сидоров, Phone: +79994443322, Address: г. Санкт-Петербург, ул. Пушкина, д. 7\n"
    assert captured.out == expected_output

"Тест снифинга order_by"
def test_select_order_by_output(capsys):
    select_order_by()
    captured = capsys.readouterr()
    expected_output = (
        "ID: 7, Name: ООО Крольчанск, Representative: Кирстн Данст, Speak To: мисс Данст, Phone: +78457654738, Address: село Капустино\n"
        "ID: 6, Name: ООО Крольчанск, Representative: Кирстн Данст, Speak To: мисс Данст, Phone: +78457654738, Address: село Капустино\n"
        "ID: 5, Name: IT-Mentor, Representative: Аваров Арсен, Speak To: Гражданин Аваров, Phone: +79987641313, Address: г. Анапа, ул. Бабушкина, д. 84\n"
        "ID: 4, Name: Stormwall, Representative: Камилев Камиль, Speak To: Гражданин Камилев, Phone: +79996443302, Address: г. Лондон, ул. Мишуткина, д. 79\n"
        "ID: 3, Name: Timeweb, Representative: Джорджов Джордж, Speak To: Гражданин Джорджов, Phone: +79996443312, Address: г. Санкт-Петербург, ул. Самойлова, д. 88\n"
        "ID: 2, Name: STC, Representative: Сидоров Сидор, Speak To: Гражданин Сидоров, Phone: +79994443322, Address: г. Санкт-Петербург, ул. Пушкина, д. 7\n"
        "ID: 1, Name: Selectel, Representative: Станислалво Вактор, Speak To: Гражданин Иванов, Phone: +79995554433, Address: г. Москва, ул. Гоголя, д. 5\n"
    )

    assert captured.out == expected_output

"Тест count фикстурой"
@pytest.fixture
def expected_return_value():
    return {3: 2, 4: 1, 2: 1, 1: 1}

def test_select_group_by_return(expected_return_value):
    returned_value = select_group_by()
    assert returned_value == expected_return_value

"Test distinct"
@pytest.mark.parametrize("expected", [
    ["11.11.1945", "29.04.2025", "09.05.2020", "25.03.1999", "13.06.2005"]
                                      ])
def test_select_distinct_dates(expected):
    assert select_distinct_dates() == expected

def test_time_functions():
    first_time = time()
    get_passports_and_client_id()
    time_without = time() - first_time

    first_time = time()
    joined_load_passports_and_client_id()
    time_relationsheep = time() - first_time

    assert time_relationsheep < time_without