from src.models import ProviderOrm, SupplyOrm, ProductsOrm, EmployeesOrm, ClientOrm, OrdersOrm, PassportsOrm
from src.database import session_factory, Base, engine
from sqlalchemy import select, func

def delete_orm():
    Base.metadata.drop_all(engine)

def create_orm():
    Base.metadata.create_all(engine)

def insert_provider_orm():
    provider1 = ProviderOrm(
        name_of_provider = 'Selectel',
        representative = 'Иванов Иван',
        speak_to = 'Гражданин Иванов',
        phone = '+79995554433',
        address = 'г. Москва, ул. Гоголя, д. 5'
    )

    provider2 = ProviderOrm(
        name_of_provider = 'STC',
        representative = 'Сидоров Сидор',
        speak_to = 'Гражданин Сидоров',
        phone = '+79994443322',
        address = 'г. Санкт-Петербург, ул. Пушкина, д. 7'
    )

    provider3 = ProviderOrm(
        name_of_provider = 'Timeweb',
        representative = 'Джорджов Джордж',
        speak_to = 'Гражданин Джорджов',
        phone = '+79996443312',
        address = 'г. Санкт-Петербург, ул. Самойлова, д. 88'
    )

    provider4 = ProviderOrm(
        name_of_provider = 'Stormwall',
        representative = 'Камилев Камиль',
        speak_to = 'Гражданин Камилев',
        phone = '+79996443302',
        address = 'г. Лондон, ул. Мишуткина, д. 79'
    )

    provider5 = ProviderOrm(
        name_of_provider = 'IT-Mentor',
        representative = 'Аваров Арсен',
        speak_to = 'Гражданин Аваров',
        phone = '+79987641313',
        address = 'г. Анапа, ул. Бабушкина, д. 84'
    )

    with session_factory() as session:
        session.add_all([provider1, provider2, provider3, provider4, provider5])
        session.commit()

def insert_supply_orm():
    supply_1 = SupplyOrm(
        id_provider = 1,
        date_of_supply = '25.03.1999',
        test = ''
    )

    supply_2 = SupplyOrm(
        id_provider = 3,
        date_of_supply = '13.06.2005',
        test = ''
    )

    supply_3 = SupplyOrm(
        id_provider = 4,
        date_of_supply = '09.05.2020',
        test = ''
    )

    supply_4 = SupplyOrm(
        id_provider = 3,
        date_of_supply = '11.11.1945',
        test = ''
    )

    supply_5 = SupplyOrm(
        id_provider = 2,
        date_of_supply = '29.04.2025',
        test = ''
    )

    with session_factory() as session:
        session.add_all([supply_1, supply_2, supply_3, supply_4, supply_5])
        session.commit()

def insert_product_orm():
    product_1 = ProductsOrm(
        id_supply = 1,
        name_of_product = "Ноутбук Lenovo ThinkPad",
        specifications = "Intel i7, 16GB RAM, 512GB SSD",
        description = "Надежный бизнес-ноутбук с высоким уровнем производительности.",
        image = "lenovo_thinkpad.jpg",
        purchase_cost = 70000,
        availability = True,
        quantity = 10,
        selling_cost = 85000
    )

    product_2 = ProductsOrm(
        id_supply=2,
        name_of_product="Смартфон Samsung Galaxy S23",
        specifications="Snapdragon 8 Gen 2, 8GB RAM, 128GB",
        description="Флагманский смартфон с передовой камерой.",
        image="samsung_s23.jpg",
        purchase_cost=60000,
        availability=True,
        quantity=15,
        selling_cost=75000
    )

    product_3 = ProductsOrm(
        id_supply=3,
        name_of_product="Игровая мышь Logitech G502",
        specifications="16000 DPI, 11 программируемых кнопок",
        description="Эргономичная мышь для профессиональных геймеров.",
        image="logitech_g502.jpg",
        purchase_cost=5000,
        availability=False,
        quantity=0,
        selling_cost=6500
    )

    product_4 = ProductsOrm(
        id_supply=4,
        name_of_product="Монитор LG UltraGear 27GL850",
        specifications="27'', 2560x1440, 144Hz, 1ms",
        description="Игровой монитор с высоким разрешением и частотой обновления.",
        image="lg_ultragear.jpg",
        purchase_cost=25000,
        availability=True,
        quantity=7,
        selling_cost=32000
    )

    product_5 = ProductsOrm(
        id_supply=5,
        name_of_product="Клавиатура Razer BlackWidow V3",
        specifications="Механические переключатели, RGB подсветка",
        description="Игровая клавиатура с индивидуальной RGB-подсветкой.",
        image="razer_blackwidow.jpg",
        purchase_cost=8000,
        availability=True,
        quantity=20,
        selling_cost=10500
    )

    with session_factory() as session:
        session.add_all([product_1, product_2, product_3, product_4, product_5])
        session.commit()

def insert_employee_orm():
    employee_1 = EmployeesOrm(
        family = "Иванов",
        name = "Иван",
        surname = "Иванович",
        job_title = "Системный администратор",
        address = "г. Москва, ул. Ленина, д. 12",
        home_phone = "+74951234567",
        birthday = "1990-05-15"
    )

    employee_2 = EmployeesOrm(
        family = "Петров",
        name = "Петр",
        surname = "Петрович",
        job_title = "Программист",
        address = "г. Санкт-Петербург, ул. Мира, д. 45",
        home_phone = "+78121234567",
        birthday = "1985-08-20"
    )

    employee_3 = EmployeesOrm(
        family = "Сидорова",
        name = "Мария",
        surname = "Александровна",
        job_title = "Менеджер по продажам",
        address = "г. Казань, ул. Победы, д. 3",
        home_phone = "+78431234567",
        birthday = "1992-11-10"
    )

    employee_4 = EmployeesOrm(
        family = "Кузнецов",
        name = "Алексей",
        surname = "Владимирович",
        job_title = "Аналитик данных",
        address = "г. Новосибирск, ул. Красная, д. 7",
        home_phone = "+73831234567",
        birthday = "1988-03-05"
    )

    employee_5 = EmployeesOrm(
        family = "Смирнова",
        name = "Екатерина",
        surname = "Игоревна",
        job_title = "Бухгалтер",
        address = "г. Екатеринбург, ул. Московская, д. 22",
        home_phone = "+73431234567",
        birthday = "1995-12-30"
    )

    with session_factory() as session:
        session.add_all([employee_1, employee_2, employee_3, employee_4, employee_5])
        session.commit()

def insert_client_orm():
    client_1 = ClientOrm(
        full_name = "Иванов Иван Иванович",
        address = "г. Москва, ул. Ленина, д. 12",
        phone = "+74951234567"
    )

    client_2 = ClientOrm(
        full_name = "Петрова Марина Сергеевна",
        address = "г. Санкт-Петербург, ул. Мира, д. 45",
        phone = "+78121234567"
    )

    client_3 = ClientOrm(
        full_name = "Сидоров Алексей Владимирович",
        address = "г. Казань, ул. Победы, д. 3",
        phone = "+78431234567"
    )

    client_4 = ClientOrm(
        full_name = "Кузнецова Ольга Александровна",
        address = "г. Новосибирск, ул. Красная, д. 7",
        phone = "+73831234567"
    )

    client_5 = ClientOrm(
        full_name = "Смирнов Дмитрий Олегович",
        address = "г. Екатеринбург, ул. Московская, д. 22",
        phone = "+73431234567"
    )

    client_6 = ClientOrm(
        full_name="Федоров Николай Евгеньевич",
        address="г. Омск, ул. Гоголя, д. 5",
        phone="+73831234568"
    )

    client_7 = ClientOrm(
        full_name="Васильева Анна Сергеевна",
        address="г. Челябинск, ул. Кирова, д. 9",
        phone="+73512234569"
    )

    client_8 = ClientOrm(
        full_name="Морозов Дмитрий Павлович",
        address="г. Тюмень, ул. Лесная, д. 17",
        phone="+73442234570"
    )

    client_9 = ClientOrm(
        full_name="Громова Елена Викторовна",
        address="г. Краснодар, ул. Советская, д. 21",
        phone="+78612234571"
    )

    client_10 = ClientOrm(
        full_name="Захаров Алексей Олегович",
        address="г. Ростов-на-Дону, ул. Ленина, д. 11",
        phone="+78632234572"
    )

    client_11 = ClientOrm(
        full_name="Борисов Сергей Николаевич",
        address="г. Самара, ул. Победы, д. 3",
        phone="+78462234573"
    )

    client_12 = ClientOrm(
        full_name="Тимофеева Ольга Петровна",
        address="г. Казань, ул. Московская, д. 15",
        phone="+78431234574"
    )

    client_13 = ClientOrm(
        full_name="Поляков Артем Дмитриевич",
        address="г. Уфа, ул. Гагарина, д. 7",
        phone="+73472234575"
    )

    client_14 = ClientOrm(
        full_name="Макарова Светлана Викторовна",
        address="г. Волгоград, ул. Советская, д. 9",
        phone="+78442234576"
    )

    client_15 = ClientOrm(
        full_name="Гаврилов Евгений Александрович",
        address="г. Пермь, ул. Центральная, д. 22",
        phone="+73422234577"
    )

    client_16 = ClientOrm(
        full_name="Фролова Надежда Сергеевна",
        address="г. Красноярск, ул. Лермонтова, д. 5",
        phone="+73912234578"
    )

    client_17 = ClientOrm(
        full_name="Денисов Виктор Павлович",
        address="г. Воронеж, ул. Чехова, д. 13",
        phone="+74732234579"
    )

    client_18 = ClientOrm(
        full_name="Зуева Марина Олеговна",
        address="г. Иркутск, ул. Байкальская, д. 20",
        phone="+73952234580"
    )

    client_19 = ClientOrm(
        full_name="Семенов Михаил Иванович",
        address="г. Барнаул, ул. Пролетарская, д. 18",
        phone="+73852234581"
    )

    client_20 = ClientOrm(
        full_name="Романова Елена Владимировна",
        address="г. Тула, ул. Октябрьская, д. 6",
        phone="+74872234582"
    )

    client_21 = ClientOrm(
        full_name="Королев Александр Сергеевич",
        address="г. Ярославль, ул. Лесная, д. 8",
        phone="+74852234583"
    )

    client_22 = ClientOrm(
        full_name="Мельникова Ирина Алексеевна",
        address="г. Иваново, ул. Советская, д. 5",
        phone="+74922234584"
    )

    client_23 = ClientOrm(
        full_name="Григорьев Павел Олегович",
        address="г. Тверь, ул. Кирова, д. 12",
        phone="+74822234585"
    )

    client_24 = ClientOrm(
        full_name="Сафонова Оксана Николаевна",
        address="г. Смоленск, ул. Ленина, д. 3",
        phone="+74812234586"
    )

    client_25 = ClientOrm(
        full_name="Беляев Дмитрий Викторович",
        address="г. Кострома, ул. Победы, д. 9",
        phone="+74942234587"
    )

    client_26 = ClientOrm(
        full_name="Никитина Екатерина Владимировна",
        address="г. Рязань, ул. Гагарина, д. 11",
        phone="+74912234588"
    )

    client_27 = ClientOrm(
        full_name="Орлов Максим Андреевич",
        address="г. Тамбов, ул. Московская, д. 7",
        phone="+74752234589"
    )

    client_28 = ClientOrm(
        full_name="Козлова Анна Дмитриевна",
        address="г. Брянск, ул. Октябрьская, д. 4",
        phone="+74832234590"
    )

    client_29 = ClientOrm(
        full_name="Егоров Василий Павлович",
        address="г. Курск, ул. Центральная, д. 14",
        phone="+74712234591"
    )

    client_30 = ClientOrm(
        full_name="Павлова Наталья Сергеевна",
        address="г. Белгород, ул. Чехова, д. 19",
        phone="+74722234592"
    )

    client_31 = ClientOrm(
        full_name="Степанов Артем Сергеевич",
        address="г. Орел, ул. Гоголя, д. 6",
        phone="+74732234593"
    )

    client_32 = ClientOrm(
        full_name="Федорова Татьяна Николаевна",
        address="г. Владимир, ул. Пушкина, д. 15",
        phone="+74922234594"
    )

    client_33 = ClientOrm(
        full_name="Морозов Иван Павлович",
        address="г. Калуга, ул. Советская, д. 8",
        phone="+74842234595"
    )

    client_34 = ClientOrm(
        full_name="Васильева Ольга Дмитриевна",
        address="г. Тула, ул. Лермонтова, д. 5",
        phone="+74872234596"
    )

    client_35 = ClientOrm(
        full_name="Жуков Алексей Викторович",
        address="г. Липецк, ул. Гагарина, д. 13",
        phone="+74742234597"
    )

    client_36 = ClientOrm(
        full_name="Андреева Мария Владимировна",
        address="г. Тамбов, ул. Победы, д. 9",
        phone="+74752234598"
    )

    client_37 = ClientOrm(
        full_name="Захаров Дмитрий Николаевич",
        address="г. Смоленск, ул. Московская, д. 7",
        phone="+74812234599"
    )

    client_38 = ClientOrm(
        full_name="Сергеев Николай Александрович",
        address="г. Брянск, ул. Красная, д. 4",
        phone="+74832234600"
    )

    client_39 = ClientOrm(
        full_name="Киселева Елена Олеговна",
        address="г. Курск, ул. Центральная, д. 14",
        phone="+74712234601"
    )

    client_40 = ClientOrm(
        full_name="Михайлов Павел Аркадьевич",
        address="г. Белгород, ул. Чехова, д. 19",
        phone="+74722234602"
    )

    client_41 = ClientOrm(
        full_name="Романов Виктор Алексеевич",
        address="г. Воронеж, ул. Свободы, д. 21",
        phone="+74732234603"
    )

    client_42 = ClientOrm(
        full_name="Гаврилова Наталья Петровна",
        address="г. Тамбов, ул. Лесная, д. 10",
        phone="+74752234604"
    )

    client_43 = ClientOrm(
        full_name="Денисов Алексей Владимирович",
        address="г. Иваново, ул. Октябрьская, д. 6",
        phone="+74922234605"
    )

    client_44 = ClientOrm(
        full_name="Семенова Ольга Сергеевна",
        address="г. Липецк, ул. Кирова, д. 18",
        phone="+74742234606"
    )

    client_45 = ClientOrm(
        full_name="Титов Артем Викторович",
        address="г. Смоленск, ул. Гагарина, д. 11",
        phone="+74812234607"
    )

    client_46 = ClientOrm(
        full_name="Елисеева Татьяна Андреевна",
        address="г. Брянск, ул. Чехова, д. 9",
        phone="+74832234608"
    )

    client_47 = ClientOrm(
        full_name="Прокофьев Николай Дмитриевич",
        address="г. Калуга, ул. Советская, д. 13",
        phone="+74842234609"
    )

    client_48 = ClientOrm(
        full_name="Куликова Марина Олеговна",
        address="г. Орел, ул. Московская, д. 4",
        phone="+74732234610"
    )

    client_49 = ClientOrm(
        full_name="Филиппов Михаил Павлович",
        address="г. Белгород, ул. Центральная, д. 16",
        phone="+74722234611"
    )

    client_50 = ClientOrm(
        full_name="Борисова Анна Николаевна",
        address="г. Курск, ул. Ленина, д. 8",
        phone="+74712234612"
    )

    client_51 = ClientOrm(
        full_name="Воронов Павел Сергеевич",
        address="г. Тверь, ул. Грибоедова, д. 5",
        phone="+74822234613"
    )

    client_52 = ClientOrm(
        full_name="Лазарева Анна Викторовна",
        address="г. Ярославль, ул. Солнечная, д. 12",
        phone="+74852234614"
    )

    client_53 = ClientOrm(
        full_name="Егоров Иван Алексеевич",
        address="г. Иваново, ул. Победы, д. 19",
        phone="+74922234615"
    )

    client_54 = ClientOrm(
        full_name="Полякова Оксана Дмитриевна",
        address="г. Владимир, ул. Парковая, д. 6",
        phone="+74932234616"
    )

    client_55 = ClientOrm(
        full_name="Тихонов Алексей Игоревич",
        address="г. Рязань, ул. Советская, д. 14",
        phone="+74912234617"
    )

    client_56 = ClientOrm(
        full_name="Громова Наталья Андреевна",
        address="г. Вологда, ул. Молодежная, д. 22",
        phone="+74962234618"
    )

    client_57 = ClientOrm(
        full_name="Федотов Сергей Павлович",
        address="г. Челябинск, ул. Лесная, д. 8",
        phone="+73512234619"
    )

    client_58 = ClientOrm(
        full_name="Савельева Марина Олеговна",
        address="г. Тула, ул. Гагарина, д. 3",
        phone="+74872234620"
    )

    client_59 = ClientOrm(
        full_name="Никифоров Артем Дмитриевич",
        address="г. Саратов, ул. Московская, д. 7",
        phone="+78452234621"
    )

    client_60 = ClientOrm(
        full_name="Шестакова Ирина Сергеевна",
        address="г. Псков, ул. Ленина, д. 5",
        phone="+78112234622"
    )

    client_61 = ClientOrm(
        full_name="Родионов Виктор Александрович",
        address="г. Смоленск, ул. Чехова, д. 11",
        phone="+74812234623"
    )

    client_62 = ClientOrm(
        full_name="Фомина Татьяна Николаевна",
        address="г. Тверь, ул. Свободы, д. 4",
        phone="+74822234624"
    )

    client_63 = ClientOrm(
        full_name="Гришин Алексей Сергеевич",
        address="г. Липецк, ул. Октябрьская, д. 9",
        phone="+74742234625"
    )

    client_64 = ClientOrm(
        full_name="Кондратьева Ольга Андреевна",
        address="г. Курск, ул. Центральная, д. 18",
        phone="+74712234626"
    )

    client_65 = ClientOrm(
        full_name="Трофимов Михаил Павлович",
        address="г. Белгород, ул. Парковая, д. 7",
        phone="+74722234627"
    )

    client_66 = ClientOrm(
        full_name="Суханова Елена Викторовна",
        address="г. Брянск, ул. Молодежная, д. 10",
        phone="+74832234628"
    )

    client_67 = ClientOrm(
        full_name="Чернов Дмитрий Олегович",
        address="г. Орел, ул. Гоголя, д. 13",
        phone="+74732234629"
    )

    client_68 = ClientOrm(
        full_name="Зайцева Наталья Александровна",
        address="г. Воронеж, ул. Солнечная, д. 16",
        phone="+74732234630"
    )

    client_69 = ClientOrm(
        full_name="Колесников Артем Игоревич",
        address="г. Пермь, ул. Лесная, д. 6",
        phone="+73422234631"
    )

    client_70 = ClientOrm(
        full_name="Панфилова Оксана Алексеевна",
        address="г. Киров, ул. Кирова, д. 8",
        phone="+78332234632"
    )

    client_71 = ClientOrm(
        full_name="Михайлова Виктория Павловна",
        address="г. Калуга, ул. Гагарина, д. 10",
        phone="+74842234633"
    )

    client_72 = ClientOrm(
        full_name="Беляев Алексей Николаевич",
        address="г. Тольятти, ул. Советская, д. 8",
        phone="+78482234634"
    )

    client_73 = ClientOrm(
        full_name="Соловьева Анастасия Дмитриевна",
        address="г. Уфа, ул. Победы, д. 5",
        phone="+73472234635"
    )

    client_74 = ClientOrm(
        full_name="Ковалев Михаил Сергеевич",
        address="г. Оренбург, ул. Центральная, д. 3",
        phone="+73532234636"
    )

    client_75 = ClientOrm(
        full_name="Гаврилова Ольга Андреевна",
        address="г. Чебоксары, ул. Лесная, д. 9",
        phone="+78322234637"
    )

    client_76 = ClientOrm(
        full_name="Филиппов Дмитрий Олегович",
        address="г. Брянск, ул. Кирова, д. 7",
        phone="+74832234638"
    )

    client_77 = ClientOrm(
        full_name="Тихонова Марина Викторовна",
        address="г. Архангельск, ул. Ломоносова, д. 11",
        phone="+78182234639"
    )

    client_78 = ClientOrm(
        full_name="Яковлев Сергей Петрович",
        address="г. Петрозаводск, ул. Октябрьская, д. 15",
        phone="+78142234640"
    )

    client_79 = ClientOrm(
        full_name="Денисова Оксана Алексеевна",
        address="г. Мурманск, ул. Московская, д. 13",
        phone="+78152234641"
    )

    client_80 = ClientOrm(
        full_name="Захаров Николай Иванович",
        address="г. Владикавказ, ул. Победы, д. 6",
        phone="+78652234642"
    )

    client_81 = ClientOrm(
        full_name="Нестерова Ирина Владимировна",
        address="г. Кострома, ул. Грибоедова, д. 2",
        phone="+74942234643"
    )

    client_82 = ClientOrm(
        full_name="Макаров Артем Сергеевич",
        address="г. Кемерово, ул. Сибирская, д. 9",
        phone="+73842234644"
    )

    client_83 = ClientOrm(
        full_name="Гордеева Татьяна Дмитриевна",
        address="г. Новокузнецк, ул. Мира, д. 14",
        phone="+73822234645"
    )

    client_84 = ClientOrm(
        full_name="Фролов Иван Олегович",
        address="г. Астрахань, ул. Центральная, д. 10",
        phone="+78552234646"
    )

    client_85 = ClientOrm(
        full_name="Сафонова Екатерина Павловна",
        address="г. Тюмень, ул. Молодежная, д. 5",
        phone="+73492234647"
    )

    client_86 = ClientOrm(
        full_name="Рябов Алексей Викторович",
        address="г. Магнитогорск, ул. Красная, д. 8",
        phone="+73592234648"
    )

    client_87 = ClientOrm(
        full_name="Козлова Светлана Алексеевна",
        address="г. Курган, ул. Лесная, д. 16",
        phone="+73522234649"
    )

    client_88 = ClientOrm(
        full_name="Дорофеев Дмитрий Олегович",
        address="г. Иваново, ул. Гагарина, д. 3",
        phone="+74922234650"
    )

    client_89 = ClientOrm(
        full_name="Антонова Елена Андреевна",
        address="г. Орёл, ул. Чехова, д. 7",
        phone="+74862234651"
    )

    client_90 = ClientOrm(
        full_name="Капустин Михаил Сергеевич",
        address="г. Тамбов, ул. Кирова, д. 12",
        phone="+74752234652"
    )

    client_91 = ClientOrm(
        full_name="Горшкова Ольга Павловна",
        address="г. Великий Новгород, ул. Ленина, д. 5",
        phone="+78162234653"
    )

    client_92 = ClientOrm(
        full_name="Потапов Андрей Викторович",
        address="г. Чита, ул. Советская, д. 8",
        phone="+73022234654"
    )

    client_93 = ClientOrm(
        full_name="Кириллова Виктория Дмитриевна",
        address="г. Ульяновск, ул. Молодежная, д. 14",
        phone="+78422234655"
    )

    client_94 = ClientOrm(
        full_name="Гусев Павел Николаевич",
        address="г. Волжский, ул. Октябрьская, д. 9",
        phone="+78442234656"
    )

    client_95 = ClientOrm(
        full_name="Борисова Наталья Ивановна",
        address="г. Якутск, ул. Победы, д. 6",
        phone="+74112234657"
    )

    client_96 = ClientOrm(
        full_name="Федоров Алексей Олегович",
        address="г. Сочи, ул. Солнечная, д. 3",
        phone="+78622234658"
    )

    client_97 = ClientOrm(
        full_name="Щербакова Мария Алексеевна",
        address="г. Красноярск, ул. Гагарина, д. 11",
        phone="+73912234659"
    )

    client_98 = ClientOrm(
        full_name="Артемьев Сергей Викторович",
        address="г. Омск, ул. Центральная, д. 5",
        phone="+73812234660"
    )

    client_99 = ClientOrm(
        full_name="Терентьева Анастасия Павловна",
        address="г. Барнаул, ул. Кирова, д. 13",
        phone="+73852234661"
    )

    client_100 = ClientOrm(
        full_name="Мельников Виктор Олегович",
        address="г. Владивосток, ул. Ломоносова, д. 7",
        phone="+74232234662"
    )

    with session_factory() as session:
        session.add_all([
    client_6, client_7, client_8, client_9, client_10,
    client_11, client_12, client_13, client_14, client_15,
    client_16, client_17, client_18, client_19, client_20,
    client_21, client_22, client_23, client_24, client_25,
    client_26, client_27, client_28, client_29, client_30,
    client_31, client_32, client_33, client_34, client_35,
    client_36, client_37, client_38, client_39, client_40,
    client_41, client_42, client_43, client_44, client_45,
    client_46, client_47, client_48, client_49, client_50,
    client_51, client_52, client_53, client_54, client_55,
    client_56, client_57, client_58, client_59, client_60,
    client_61, client_62, client_63, client_64, client_65,
    client_66, client_67, client_68, client_69, client_70,
    client_71, client_72, client_73, client_74, client_75,
    client_76, client_77, client_78, client_79, client_80,
    client_81, client_82, client_83, client_84, client_85,
    client_86, client_87, client_88, client_89, client_90,
    client_91, client_92, client_93, client_94, client_95,
    client_96, client_97, client_98, client_99, client_100
])
        session.commit()

def insert_orders_orm():
    order_1 = OrdersOrm(
        id_employee=1,
        id_product=2,
        id_client=3,
        posting_date="2025-03-15",
        execution_date="2025-03-20"
    )

    order_2 = OrdersOrm(
        id_employee=2,
        id_product=4,
        id_client=1,
        posting_date="2025-02-10",
        execution_date="2025-02-18"
    )

    order_3 = OrdersOrm(
        id_employee=3,
        id_product=1,
        id_client=5,
        posting_date="2025-01-05",
        execution_date="2025-01-10"
    )

    order_4 = OrdersOrm(
        id_employee=4,
        id_product=3,
        id_client=2,
        posting_date="2024-12-20",
        execution_date="2024-12-25"
    )

    order_5 = OrdersOrm(
        id_employee=5,
        id_product=5,
        id_client=4,
        posting_date="2025-03-01",
        execution_date="2025-03-05"
    )

    with session_factory() as session:
        session.add_all([order_1, order_2, order_3, order_4, order_5])
        session.commit()

def insert_passports_orm():
    ...
    passport_1 = PassportsOrm(id_client=1, country='United States')
    passport_2 = PassportsOrm(id_client=1, country='Canada')
    passport_3 = PassportsOrm(id_client=1, country='Germany')
    passport_4 = PassportsOrm(id_client=1, country='France')
    passport_5 = PassportsOrm(id_client=1, country='Italy')
    passport_6 = PassportsOrm(id_client=1, country='United Kingdom')
    passport_7 = PassportsOrm(id_client=1, country='Australia')
    passport_8 = PassportsOrm(id_client=1, country='Spain')
    passport_9 = PassportsOrm(id_client=1, country='Japan')
    passport_10 = PassportsOrm(id_client=1, country='South Korea')
    passport_11 = PassportsOrm(id_client=2, country='Russia')
    passport_12 = PassportsOrm(id_client=2, country='China')
    passport_13 = PassportsOrm(id_client=2, country='India')
    passport_14 = PassportsOrm(id_client=2, country='Brazil')
    passport_15 = PassportsOrm(id_client=2, country='Mexico')
    passport_16 = PassportsOrm(id_client=2, country='South Africa')
    passport_17 = PassportsOrm(id_client=2, country='Egypt')
    passport_18 = PassportsOrm(id_client=2, country='Argentina')
    passport_19 = PassportsOrm(id_client=2, country='Turkey')
    passport_20 = PassportsOrm(id_client=2, country='Saudi Arabia')
    passport_21 = PassportsOrm(id_client=3, country='Brazil')
    passport_22 = PassportsOrm(id_client=3, country='Argentina')
    passport_23 = PassportsOrm(id_client=3, country='Chile')
    passport_24 = PassportsOrm(id_client=3, country='Peru')
    passport_25 = PassportsOrm(id_client=3, country='Colombia')
    passport_26 = PassportsOrm(id_client=3, country='Venezuela')
    passport_27 = PassportsOrm(id_client=3, country='Ecuador')
    passport_28 = PassportsOrm(id_client=3, country='Paraguay')
    passport_29 = PassportsOrm(id_client=3, country='Uruguay')
    passport_30 = PassportsOrm(id_client=3, country='Bolivia')
    passport_31 = PassportsOrm(id_client=4, country='Germany')
    passport_32 = PassportsOrm(id_client=4, country='France')
    passport_33 = PassportsOrm(id_client=4, country='Spain')
    passport_34 = PassportsOrm(id_client=4, country='Italy')
    passport_35 = PassportsOrm(id_client=4, country='Sweden')
    passport_36 = PassportsOrm(id_client=4, country='Norway')
    passport_37 = PassportsOrm(id_client=4, country='Denmark')
    passport_38 = PassportsOrm(id_client=4, country='Netherlands')
    passport_39 = PassportsOrm(id_client=4, country='Belgium')
    passport_40 = PassportsOrm(id_client=4, country='Austria')
    passport_41 = PassportsOrm(id_client=5, country='Japan')
    passport_42 = PassportsOrm(id_client=5, country='South Korea')
    passport_43 = PassportsOrm(id_client=5, country='China')
    passport_44 = PassportsOrm(id_client=5, country='India')
    passport_45 = PassportsOrm(id_client=5, country='Nepal')
    passport_46 = PassportsOrm(id_client=5, country='Bangladesh')
    passport_47 = PassportsOrm(id_client=5, country='Pakistan')
    passport_48 = PassportsOrm(id_client=5, country='Sri Lanka')
    passport_49 = PassportsOrm(id_client=5, country='Myanmar')
    passport_50 = PassportsOrm(id_client=5, country='Thailand')
    passport_51 = PassportsOrm(id_client=6, country='Mexico')
    passport_52 = PassportsOrm(id_client=6, country='Cuba')
    passport_53 = PassportsOrm(id_client=6, country='Guatemala')
    passport_54 = PassportsOrm(id_client=6, country='Honduras')
    passport_55 = PassportsOrm(id_client=6, country='Costa Rica')
    passport_56 = PassportsOrm(id_client=6, country='Panama')
    passport_57 = PassportsOrm(id_client=6, country='El Salvador')
    passport_58 = PassportsOrm(id_client=6, country='Nicaragua')
    passport_59 = PassportsOrm(id_client=6, country='Dominican Republic')
    passport_60 = PassportsOrm(id_client=6, country='Belize')
    passport_61 = PassportsOrm(id_client=7, country='Colombia')
    passport_62 = PassportsOrm(id_client=7, country='Peru')
    passport_63 = PassportsOrm(id_client=7, country='Venezuela')
    passport_64 = PassportsOrm(id_client=7, country='Ecuador')
    passport_65 = PassportsOrm(id_client=7, country='Paraguay')
    passport_66 = PassportsOrm(id_client=7, country='Chile')
    passport_67 = PassportsOrm(id_client=7, country='Bolivia')
    passport_68 = PassportsOrm(id_client=7, country='Uruguay')
    passport_69 = PassportsOrm(id_client=7, country='Suriname')
    passport_70 = PassportsOrm(id_client=7, country='Guyana')
    passport_71 = PassportsOrm(id_client=8, country='Sweden')
    passport_72 = PassportsOrm(id_client=8, country='Norway')
    passport_73 = PassportsOrm(id_client=8, country='Denmark')
    passport_74 = PassportsOrm(id_client=8, country='Finland')
    passport_75 = PassportsOrm(id_client=8, country='Iceland')
    passport_76 = PassportsOrm(id_client=8, country='Estonia')
    passport_77 = PassportsOrm(id_client=8, country='Latvia')
    passport_78 = PassportsOrm(id_client=8, country='Lithuania')
    passport_79 = PassportsOrm(id_client=8, country='Poland')
    passport_80 = PassportsOrm(id_client=8, country='Czech Republic')
    passport_81 = PassportsOrm(id_client=9, country='Finland')
    passport_82 = PassportsOrm(id_client=9, country='Sweden')
    passport_83 = PassportsOrm(id_client=9, country='Norway')
    passport_84 = PassportsOrm(id_client=9, country='Denmark')
    passport_85 = PassportsOrm(id_client=9, country='Estonia')
    passport_86 = PassportsOrm(id_client=9, country='Latvia')
    passport_87 = PassportsOrm(id_client=9, country='Lithuania')
    passport_88 = PassportsOrm(id_client=9, country='Poland')
    passport_89 = PassportsOrm(id_client=9, country='Slovakia')
    passport_90 = PassportsOrm(id_client=9, country='Hungary')
    passport_91 = PassportsOrm(id_client=10, country='Japan')
    passport_92 = PassportsOrm(id_client=10, country='South Korea')
    passport_93 = PassportsOrm(id_client=10, country='China')
    passport_94 = PassportsOrm(id_client=10, country='India')
    passport_95 = PassportsOrm(id_client=10, country='Nepal')
    passport_96 = PassportsOrm(id_client=10, country='Bangladesh')
    passport_97 = PassportsOrm(id_client=10, country='Pakistan')
    passport_98 = PassportsOrm(id_client=10, country='Sri Lanka')
    passport_99 = PassportsOrm(id_client=10, country='Myanmar')
    passport_100 = PassportsOrm(id_client=10, country='Thailand')

    passports = [
        PassportsOrm(id_client=11, country='USA'),
        PassportsOrm(id_client=11, country='Canada'),
        PassportsOrm(id_client=11, country='Mexico'),
        PassportsOrm(id_client=11, country='UK'),
        PassportsOrm(id_client=11, country='France'),
        PassportsOrm(id_client=11, country='Germany'),
        PassportsOrm(id_client=11, country='Italy'),
        PassportsOrm(id_client=11, country='Spain'),
        PassportsOrm(id_client=11, country='Netherlands'),
        PassportsOrm(id_client=11, country='Belgium'),

        PassportsOrm(id_client=12, country='Switzerland'),
        PassportsOrm(id_client=12, country='Austria'),
        PassportsOrm(id_client=12, country='Sweden'),
        PassportsOrm(id_client=12, country='Norway'),
        PassportsOrm(id_client=12, country='Denmark'),
        PassportsOrm(id_client=12, country='Finland'),
        PassportsOrm(id_client=12, country='Iceland'),
        PassportsOrm(id_client=12, country='Portugal'),
        PassportsOrm(id_client=12, country='Greece'),
        PassportsOrm(id_client=12, country='Ireland'),

        PassportsOrm(id_client=13, country='Poland'),
        PassportsOrm(id_client=13, country='Czech Republic'),
        PassportsOrm(id_client=13, country='Slovakia'),
        PassportsOrm(id_client=13, country='Hungary'),
        PassportsOrm(id_client=13, country='Romania'),
        PassportsOrm(id_client=13, country='Bulgaria'),
        PassportsOrm(id_client=13, country='Serbia'),
        PassportsOrm(id_client=13, country='Croatia'),
        PassportsOrm(id_client=13, country='Slovenia'),
        PassportsOrm(id_client=13, country='Bosnia and Herzegovina'),

        PassportsOrm(id_client=14, country='Montenegro'),
        PassportsOrm(id_client=14, country='Albania'),
        PassportsOrm(id_client=14, country='North Macedonia'),
        PassportsOrm(id_client=14, country='Ukraine'),
        PassportsOrm(id_client=14, country='Belarus'),
        PassportsOrm(id_client=14, country='Russia'),
        PassportsOrm(id_client=14, country='Turkey'),
        PassportsOrm(id_client=14, country='Georgia'),
        PassportsOrm(id_client=14, country='Armenia'),
        PassportsOrm(id_client=14, country='Azerbaijan'),

        PassportsOrm(id_client=15, country='Kazakhstan'),
        PassportsOrm(id_client=15, country='Uzbekistan'),
        PassportsOrm(id_client=15, country='Turkmenistan'),
        PassportsOrm(id_client=15, country='Tajikistan'),
        PassportsOrm(id_client=15, country='Kyrgyzstan'),
        PassportsOrm(id_client=15, country='Mongolia'),
        PassportsOrm(id_client=15, country='China'),
        PassportsOrm(id_client=15, country='India'),
        PassportsOrm(id_client=15, country='Pakistan'),
        PassportsOrm(id_client=15, country='Bangladesh'),

        PassportsOrm(id_client=16, country='Nepal'),
        PassportsOrm(id_client=16, country='Bhutan'),
        PassportsOrm(id_client=16, country='Sri Lanka'),
        PassportsOrm(id_client=16, country='Maldives'),
        PassportsOrm(id_client=16, country='Thailand'),
        PassportsOrm(id_client=16, country='Vietnam'),
        PassportsOrm(id_client=16, country='Cambodia'),
        PassportsOrm(id_client=16, country='Laos'),
        PassportsOrm(id_client=16, country='Myanmar'),
        PassportsOrm(id_client=16, country='Malaysia'),

        PassportsOrm(id_client=17, country='Singapore'),
        PassportsOrm(id_client=17, country='Indonesia'),
        PassportsOrm(id_client=17, country='Philippines'),
        PassportsOrm(id_client=17, country='Brunei'),
        PassportsOrm(id_client=17, country='Japan'),
        PassportsOrm(id_client=17, country='South Korea'),
        PassportsOrm(id_client=17, country='North Korea'),
        PassportsOrm(id_client=17, country='Taiwan'),
        PassportsOrm(id_client=17, country='Hong Kong'),
        PassportsOrm(id_client=17, country='Macau'),

        PassportsOrm(id_client=18, country='Australia'),
        PassportsOrm(id_client=18, country='New Zealand'),
        PassportsOrm(id_client=18, country='Fiji'),
        PassportsOrm(id_client=18, country='Papua New Guinea'),
        PassportsOrm(id_client=18, country='Samoa'),
        PassportsOrm(id_client=18, country='Tonga'),
        PassportsOrm(id_client=18, country='Vanuatu'),
        PassportsOrm(id_client=18, country='Solomon Islands'),
        PassportsOrm(id_client=18, country='Tuvalu'),
        PassportsOrm(id_client=18, country='Kiribati'),

        PassportsOrm(id_client=19, country='Argentina'),
        PassportsOrm(id_client=19, country='Brazil'),
        PassportsOrm(id_client=19, country='Chile'),
        PassportsOrm(id_client=19, country='Colombia'),
        PassportsOrm(id_client=19, country='Ecuador'),
        PassportsOrm(id_client=19, country='Paraguay'),
        PassportsOrm(id_client=19, country='Peru'),
        PassportsOrm(id_client=19, country='Uruguay'),
        PassportsOrm(id_client=19, country='Venezuela'),
        PassportsOrm(id_client=19, country='Bolivia'),

        PassportsOrm(id_client=20, country='South Africa'),
        PassportsOrm(id_client=20, country='Egypt'),
        PassportsOrm(id_client=20, country='Nigeria'),
        PassportsOrm(id_client=20, country='Kenya'),
        PassportsOrm(id_client=20, country='Ghana'),
        PassportsOrm(id_client=20, country='Ethiopia'),
        PassportsOrm(id_client=20, country='Morocco'),
        PassportsOrm(id_client=20, country='Algeria'),
        PassportsOrm(id_client=20, country='Tunisia'),
        PassportsOrm(id_client=20, country='Sudan')
    ]
    passports_3 = [
    PassportsOrm(id_client=21, country='USA'),
    PassportsOrm(id_client=21, country='Canada'),
    PassportsOrm(id_client=21, country='Mexico'),
    PassportsOrm(id_client=21, country='Brazil'),
    PassportsOrm(id_client=21, country='Argentina'),
    PassportsOrm(id_client=21, country='Chile'),
    PassportsOrm(id_client=21, country='Peru'),
    PassportsOrm(id_client=21, country='Colombia'),
    PassportsOrm(id_client=21, country='Venezuela'),
    PassportsOrm(id_client=21, country='Ecuador'),

    PassportsOrm(id_client=22, country='France'),
    PassportsOrm(id_client=22, country='Germany'),
    PassportsOrm(id_client=22, country='Italy'),
    PassportsOrm(id_client=22, country='Spain'),
    PassportsOrm(id_client=22, country='Portugal'),
    PassportsOrm(id_client=22, country='Netherlands'),
    PassportsOrm(id_client=22, country='Belgium'),
    PassportsOrm(id_client=22, country='Switzerland'),
    PassportsOrm(id_client=22, country='Austria'),
    PassportsOrm(id_client=22, country='Sweden'),

    PassportsOrm(id_client=23, country='Norway'),
    PassportsOrm(id_client=23, country='Denmark'),
    PassportsOrm(id_client=23, country='Finland'),
    PassportsOrm(id_client=23, country='Iceland'),
    PassportsOrm(id_client=23, country='Poland'),
    PassportsOrm(id_client=23, country='Czech Republic'),
    PassportsOrm(id_client=23, country='Slovakia'),
    PassportsOrm(id_client=23, country='Hungary'),
    PassportsOrm(id_client=23, country='Romania'),
    PassportsOrm(id_client=23, country='Bulgaria'),

    PassportsOrm(id_client=24, country='Greece'),
    PassportsOrm(id_client=24, country='Turkey'),
    PassportsOrm(id_client=24, country='Cyprus'),
    PassportsOrm(id_client=24, country='Russia'),
    PassportsOrm(id_client=24, country='Ukraine'),
    PassportsOrm(id_client=24, country='Belarus'),
    PassportsOrm(id_client=24, country='Moldova'),
    PassportsOrm(id_client=24, country='Georgia'),
    PassportsOrm(id_client=24, country='Armenia'),
    PassportsOrm(id_client=24, country='Azerbaijan'),

    PassportsOrm(id_client=25, country='Kazakhstan'),
    PassportsOrm(id_client=25, country='Uzbekistan'),
    PassportsOrm(id_client=25, country='Turkmenistan'),
    PassportsOrm(id_client=25, country='Tajikistan'),
    PassportsOrm(id_client=25, country='Kyrgyzstan'),
    PassportsOrm(id_client=25, country='China'),
    PassportsOrm(id_client=25, country='Japan'),
    PassportsOrm(id_client=25, country='South Korea'),
    PassportsOrm(id_client=25, country='North Korea'),
    PassportsOrm(id_client=25, country='Mongolia'),

    PassportsOrm(id_client=26, country='India'),
    PassportsOrm(id_client=26, country='Pakistan'),
    PassportsOrm(id_client=26, country='Bangladesh'),
    PassportsOrm(id_client=26, country='Nepal'),
    PassportsOrm(id_client=26, country='Bhutan'),
    PassportsOrm(id_client=26, country='Sri Lanka'),
    PassportsOrm(id_client=26, country='Maldives'),
    PassportsOrm(id_client=26, country='Myanmar'),
    PassportsOrm(id_client=26, country='Thailand'),
    PassportsOrm(id_client=26, country='Vietnam'),

    PassportsOrm(id_client=27, country='Laos'),
    PassportsOrm(id_client=27, country='Cambodia'),
    PassportsOrm(id_client=27, country='Malaysia'),
    PassportsOrm(id_client=27, country='Singapore'),
    PassportsOrm(id_client=27, country='Indonesia'),
    PassportsOrm(id_client=27, country='Philippines'),
    PassportsOrm(id_client=27, country='Australia'),
    PassportsOrm(id_client=27, country='New Zealand'),
    PassportsOrm(id_client=27, country='Fiji'),
    PassportsOrm(id_client=27, country='Papua New Guinea'),

    PassportsOrm(id_client=28, country='South Africa'),
    PassportsOrm(id_client=28, country='Nigeria'),
    PassportsOrm(id_client=28, country='Egypt'),
    PassportsOrm(id_client=28, country='Kenya'),
    PassportsOrm(id_client=28, country='Ethiopia'),
    PassportsOrm(id_client=28, country='Ghana'),
    PassportsOrm(id_client=28, country='Algeria'),
    PassportsOrm(id_client=28, country='Morocco'),
    PassportsOrm(id_client=28, country='Tunisia'),
    PassportsOrm(id_client=28, country='Sudan'),

    PassportsOrm(id_client=29, country='Saudi Arabia'),
    PassportsOrm(id_client=29, country='United Arab Emirates'),
    PassportsOrm(id_client=29, country='Qatar'),
    PassportsOrm(id_client=29, country='Kuwait'),
    PassportsOrm(id_client=29, country='Bahrain'),
    PassportsOrm(id_client=29, country='Oman'),
    PassportsOrm(id_client=29, country='Jordan'),
    PassportsOrm(id_client=29, country='Lebanon'),
    PassportsOrm(id_client=29, country='Syria'),
    PassportsOrm(id_client=29, country='Iraq'),

    PassportsOrm(id_client=30, country='Iran'),
    PassportsOrm(id_client=30, country='Afghanistan'),
    PassportsOrm(id_client=30, country='Yemen'),
    PassportsOrm(id_client=30, country='Somalia'),
    PassportsOrm(id_client=30, country='South Sudan'),
    PassportsOrm(id_client=30, country='Libya'),
    PassportsOrm(id_client=30, country='Chad'),
    PassportsOrm(id_client=30, country='Niger'),
    PassportsOrm(id_client=30, country='Burkina Faso'),
    PassportsOrm(id_client=30, country='Mali')
    ]
    passports_4 = [
        PassportsOrm(id_client=31, country='USA'),
        PassportsOrm(id_client=31, country='Canada'),
        PassportsOrm(id_client=31, country='Mexico'),
        PassportsOrm(id_client=31, country='Brazil'),
        PassportsOrm(id_client=31, country='Argentina'),
        PassportsOrm(id_client=31, country='UK'),
        PassportsOrm(id_client=31, country='Germany'),
        PassportsOrm(id_client=31, country='France'),
        PassportsOrm(id_client=31, country='Italy'),
        PassportsOrm(id_client=31, country='Spain'),

        PassportsOrm(id_client=32, country='USA'),
        PassportsOrm(id_client=32, country='Canada'),
        PassportsOrm(id_client=32, country='Mexico'),
        PassportsOrm(id_client=32, country='Brazil'),
        PassportsOrm(id_client=32, country='Argentina'),
        PassportsOrm(id_client=32, country='UK'),
        PassportsOrm(id_client=32, country='Germany'),
        PassportsOrm(id_client=32, country='France'),
        PassportsOrm(id_client=32, country='Italy'),
        PassportsOrm(id_client=32, country='Spain'),

        PassportsOrm(id_client=33, country='USA'),
        PassportsOrm(id_client=33, country='Canada'),
        PassportsOrm(id_client=33, country='Mexico'),
        PassportsOrm(id_client=33, country='Brazil'),
        PassportsOrm(id_client=33, country='Argentina'),
        PassportsOrm(id_client=33, country='UK'),
        PassportsOrm(id_client=33, country='Germany'),
        PassportsOrm(id_client=33, country='France'),
        PassportsOrm(id_client=33, country='Italy'),
        PassportsOrm(id_client=33, country='Spain'),

        PassportsOrm(id_client=34, country='USA'),
        PassportsOrm(id_client=34, country='Canada'),
        PassportsOrm(id_client=34, country='Mexico'),
        PassportsOrm(id_client=34, country='Brazil'),
        PassportsOrm(id_client=34, country='Argentina'),
        PassportsOrm(id_client=34, country='UK'),
        PassportsOrm(id_client=34, country='Germany'),
        PassportsOrm(id_client=34, country='France'),
        PassportsOrm(id_client=34, country='Italy'),
        PassportsOrm(id_client=34, country='Spain'),

        PassportsOrm(id_client=35, country='USA'),
        PassportsOrm(id_client=35, country='Canada'),
        PassportsOrm(id_client=35, country='Mexico'),
        PassportsOrm(id_client=35, country='Brazil'),
        PassportsOrm(id_client=35, country='Argentina'),
        PassportsOrm(id_client=35, country='UK'),
        PassportsOrm(id_client=35, country='Germany'),
        PassportsOrm(id_client=35, country='France'),
        PassportsOrm(id_client=35, country='Italy'),
        PassportsOrm(id_client=35, country='Spain'),

        PassportsOrm(id_client=36, country='USA'),
        PassportsOrm(id_client=36, country='Canada'),
        PassportsOrm(id_client=36, country='Mexico'),
        PassportsOrm(id_client=36, country='Brazil'),
        PassportsOrm(id_client=36, country='Argentina'),
        PassportsOrm(id_client=36, country='UK'),
        PassportsOrm(id_client=36, country='Germany'),
        PassportsOrm(id_client=36, country='France'),
        PassportsOrm(id_client=36, country='Italy'),
        PassportsOrm(id_client=36, country='Spain'),

        PassportsOrm(id_client=37, country='USA'),
        PassportsOrm(id_client=37, country='Canada'),
        PassportsOrm(id_client=37, country='Mexico'),
        PassportsOrm(id_client=37, country='Brazil'),
        PassportsOrm(id_client=37, country='Argentina'),
        PassportsOrm(id_client=37, country='UK'),
        PassportsOrm(id_client=37, country='Germany'),
        PassportsOrm(id_client=37, country='France'),
        PassportsOrm(id_client=37, country='Italy'),
        PassportsOrm(id_client=37, country='Spain'),

        PassportsOrm(id_client=38, country='USA'),
        PassportsOrm(id_client=38, country='Canada'),
        PassportsOrm(id_client=38, country='Mexico'),
        PassportsOrm(id_client=38, country='Brazil'),
        PassportsOrm(id_client=38, country='Argentina'),
        PassportsOrm(id_client=38, country='UK'),
        PassportsOrm(id_client=38, country='Germany'),
        PassportsOrm(id_client=38, country='France'),
        PassportsOrm(id_client=38, country='Italy'),
        PassportsOrm(id_client=38, country='Spain'),

        PassportsOrm(id_client=39, country='USA'),
        PassportsOrm(id_client=39, country='Canada'),
        PassportsOrm(id_client=39, country='Mexico'),
        PassportsOrm(id_client=39, country='Brazil'),
        PassportsOrm(id_client=39, country='Argentina'),
        PassportsOrm(id_client=39, country='UK'),
        PassportsOrm(id_client=39, country='Germany'),
        PassportsOrm(id_client=39, country='France'),
        PassportsOrm(id_client=39, country='Italy'),
        PassportsOrm(id_client=39, country='Spain'),

        PassportsOrm(id_client=40, country='USA'),
        PassportsOrm(id_client=40, country='Canada'),
        PassportsOrm(id_client=40, country='Mexico'),
        PassportsOrm(id_client=40, country='Brazil'),
        PassportsOrm(id_client=40, country='Argentina'),
        PassportsOrm(id_client=40, country='UK'),
        PassportsOrm(id_client=40, country='Germany'),
        PassportsOrm(id_client=40, country='France'),
        PassportsOrm(id_client=40, country='Italy'),
        PassportsOrm(id_client=40, country='Spain')
    ]

    passports_5 = [
        PassportsOrm(id_client=41, country='USA'),
        PassportsOrm(id_client=41, country='Canada'),
        PassportsOrm(id_client=41, country='Germany'),
        PassportsOrm(id_client=41, country='France'),
        PassportsOrm(id_client=41, country='Italy'),
        PassportsOrm(id_client=41, country='Spain'),
        PassportsOrm(id_client=41, country='Japan'),
        PassportsOrm(id_client=41, country='China'),
        PassportsOrm(id_client=41, country='Brazil'),
        PassportsOrm(id_client=41, country='India'),

        PassportsOrm(id_client=42, country='USA'),
        PassportsOrm(id_client=42, country='Canada'),
        PassportsOrm(id_client=42, country='Germany'),
        PassportsOrm(id_client=42, country='France'),
        PassportsOrm(id_client=42, country='Italy'),
        PassportsOrm(id_client=42, country='Spain'),
        PassportsOrm(id_client=42, country='Japan'),
        PassportsOrm(id_client=42, country='China'),
        PassportsOrm(id_client=42, country='Brazil'),
        PassportsOrm(id_client=42, country='India'),

        PassportsOrm(id_client=43, country='USA'),
        PassportsOrm(id_client=43, country='Canada'),
        PassportsOrm(id_client=43, country='Germany'),
        PassportsOrm(id_client=43, country='France'),
        PassportsOrm(id_client=43, country='Italy'),
        PassportsOrm(id_client=43, country='Spain'),
        PassportsOrm(id_client=43, country='Japan'),
        PassportsOrm(id_client=43, country='China'),
        PassportsOrm(id_client=43, country='Brazil'),
        PassportsOrm(id_client=43, country='India'),

        PassportsOrm(id_client=44, country='USA'),
        PassportsOrm(id_client=44, country='Canada'),
        PassportsOrm(id_client=44, country='Germany'),
        PassportsOrm(id_client=44, country='France'),
        PassportsOrm(id_client=44, country='Italy'),
        PassportsOrm(id_client=44, country='Spain'),
        PassportsOrm(id_client=44, country='Japan'),
        PassportsOrm(id_client=44, country='China'),
        PassportsOrm(id_client=44, country='Brazil'),
        PassportsOrm(id_client=44, country='India'),

        PassportsOrm(id_client=45, country='USA'),
        PassportsOrm(id_client=45, country='Canada'),
        PassportsOrm(id_client=45, country='Germany'),
        PassportsOrm(id_client=45, country='France'),
        PassportsOrm(id_client=45, country='Italy'),
        PassportsOrm(id_client=45, country='Spain'),
        PassportsOrm(id_client=45, country='Japan'),
        PassportsOrm(id_client=45, country='China'),
        PassportsOrm(id_client=45, country='Brazil'),
        PassportsOrm(id_client=45, country='India'),

        PassportsOrm(id_client=46, country='USA'),
        PassportsOrm(id_client=46, country='Canada'),
        PassportsOrm(id_client=46, country='Germany'),
        PassportsOrm(id_client=46, country='France'),
        PassportsOrm(id_client=46, country='Italy'),
        PassportsOrm(id_client=46, country='Spain'),
        PassportsOrm(id_client=46, country='Japan'),
        PassportsOrm(id_client=46, country='China'),
        PassportsOrm(id_client=46, country='Brazil'),
        PassportsOrm(id_client=46, country='India'),

        PassportsOrm(id_client=47, country='USA'),
        PassportsOrm(id_client=47, country='Canada'),
        PassportsOrm(id_client=47, country='Germany'),
        PassportsOrm(id_client=47, country='France'),
        PassportsOrm(id_client=47, country='Italy'),
        PassportsOrm(id_client=47, country='Spain'),
        PassportsOrm(id_client=47, country='Japan'),
        PassportsOrm(id_client=47, country='China'),
        PassportsOrm(id_client=47, country='Brazil'),
        PassportsOrm(id_client=47, country='India'),

        PassportsOrm(id_client=48, country='USA'),
        PassportsOrm(id_client=48, country='Canada'),
        PassportsOrm(id_client=48, country='Germany'),
        PassportsOrm(id_client=48, country='France'),
        PassportsOrm(id_client=48, country='Italy'),
        PassportsOrm(id_client=48, country='Spain'),
        PassportsOrm(id_client=48, country='Japan'),
        PassportsOrm(id_client=48, country='China'),
        PassportsOrm(id_client=48, country='Brazil'),
        PassportsOrm(id_client=48, country='India'),

        PassportsOrm(id_client=49, country='USA'),
        PassportsOrm(id_client=49, country='Canada'),
        PassportsOrm(id_client=49, country='Germany'),
        PassportsOrm(id_client=49, country='France'),
        PassportsOrm(id_client=49, country='Italy'),
        PassportsOrm(id_client=49, country='Spain'),
        PassportsOrm(id_client=49, country='Japan'),
        PassportsOrm(id_client=49, country='China'),
        PassportsOrm(id_client=49, country='Brazil'),
        PassportsOrm(id_client=49, country='India'),

        PassportsOrm(id_client=50, country='USA'),
        PassportsOrm(id_client=50, country='Canada'),
        PassportsOrm(id_client=50, country='Germany'),
        PassportsOrm(id_client=50, country='France'),
        PassportsOrm(id_client=50, country='Italy'),
        PassportsOrm(id_client=50, country='Spain'),
        PassportsOrm(id_client=50, country='Japan'),
        PassportsOrm(id_client=50, country='China'),
        PassportsOrm(id_client=50, country='Brazil'),
        PassportsOrm(id_client=50, country='India')
    ]

    passports_6 = [
    PassportsOrm(id_client=51, country='Japan'),
    PassportsOrm(id_client=51, country='Germany'),
    PassportsOrm(id_client=51, country='France'),
    PassportsOrm(id_client=51, country='Italy'),
     PassportsOrm(id_client=51, country='Brazil'),
     PassportsOrm(id_client=51, country='Argentina'),
      PassportsOrm(id_client=51, country='Australia'),
      PassportsOrm(id_client=51, country='Canada'),
     PassportsOrm(id_client=51, country='USA'),
      PassportsOrm(id_client=51, country='Mexico'),

      PassportsOrm(id_client=52, country='China'),
      PassportsOrm(id_client=52, country='South Korea'),
      PassportsOrm(id_client=52, country='India'),
      PassportsOrm(id_client=52, country='Russia'),
      PassportsOrm(id_client=52, country='Turkey'),
      PassportsOrm(id_client=52, country='South Africa'),
      PassportsOrm(id_client=52, country='Egypt'),
      PassportsOrm(id_client=52, country='Singapore'),
      PassportsOrm(id_client=52, country='Indonesia'),
      PassportsOrm(id_client=52, country='Malaysia'),

      PassportsOrm(id_client=53, country='Thailand'),
      PassportsOrm(id_client=53, country='Vietnam'),
      PassportsOrm(id_client=53, country='Philippines'),
      PassportsOrm(id_client=53, country='Bangladesh'),
      PassportsOrm(id_client=53, country='Nepal'),
      PassportsOrm(id_client=53, country='Pakistan'),
      PassportsOrm(id_client=53, country='Sri Lanka'),
      PassportsOrm(id_client=53, country='Myanmar'),
      PassportsOrm(id_client=53, country='Cambodia'),
      PassportsOrm(id_client=53, country='Laos'),

      PassportsOrm(id_client=54, country='Belgium'),
      PassportsOrm(id_client=54, country='Netherlands'),
      PassportsOrm(id_client=54, country='Luxembourg'),
      PassportsOrm(id_client=54, country='Switzerland'),
      PassportsOrm(id_client=54, country='Austria'),
      PassportsOrm(id_client=54, country='Denmark'),
      PassportsOrm(id_client=54, country='Norway'),
      PassportsOrm(id_client=54, country='Sweden'),
      PassportsOrm(id_client=54, country='Finland'),
      PassportsOrm(id_client=54, country='Iceland'),

      PassportsOrm(id_client=55, country='Poland'),
      PassportsOrm(id_client=55, country='Czech Republic'),
      PassportsOrm(id_client=55, country='Slovakia'),
      PassportsOrm(id_client=55, country='Hungary'),
      PassportsOrm(id_client=55, country='Romania'),
      PassportsOrm(id_client=55, country='Bulgaria'),
      PassportsOrm(id_client=55, country='Croatia'),
      PassportsOrm(id_client=55, country='Serbia'),
      PassportsOrm(id_client=55, country='Bosnia and Herzegovina'),
      PassportsOrm(id_client=55, country='Montenegro'),

      PassportsOrm(id_client=56, country='Greece'),
      PassportsOrm(id_client=56, country='Cyprus'),
      PassportsOrm(id_client=56, country='Macedonia'),
      PassportsOrm(id_client=56, country='Albania'),
      PassportsOrm(id_client=56, country='Kosovo'),
      PassportsOrm(id_client=56, country='Bulgaria'),
      PassportsOrm(id_client=56, country='Georgia'),
      PassportsOrm(id_client=56, country='Armenia'),
      PassportsOrm(id_client=56, country='Turkey'),
      PassportsOrm(id_client=56, country='Israel'),

      PassportsOrm(id_client=57, country='Jordan'),
      PassportsOrm(id_client=57, country='Palestine'),
      PassportsOrm(id_client=57, country='Lebanon'),
      PassportsOrm(id_client=57, country='Syria'),
      PassportsOrm(id_client=57, country='Egypt'),
      PassportsOrm(id_client=57, country='Kuwait'),
      PassportsOrm(id_client=57, country='Qatar'),
      PassportsOrm(id_client=57, country='United Arab Emirates'),
      PassportsOrm(id_client=57, country='Saudi Arabia'),
      PassportsOrm(id_client=57, country='Oman'),

      PassportsOrm(id_client=58, country='Yemen'),
      PassportsOrm(id_client=58, country='Bahrain'),
      PassportsOrm(id_client=58, country='Iraq'),
      PassportsOrm(id_client=58, country='Afghanistan'),
      PassportsOrm(id_client=58, country='Pakistan'),
      PassportsOrm(id_client=58, country='India'),
      PassportsOrm(id_client=58, country='Bangladesh'),
      PassportsOrm(id_client=58, country='Sri Lanka'),
      PassportsOrm(id_client=58, country='Nepal'),
      PassportsOrm(id_client=58, country='Bhutan'),

      PassportsOrm(id_client=59, country='Somalia'),
      PassportsOrm(id_client=59, country='Djibouti'),
      PassportsOrm(id_client=59, country='Kenya'),
      PassportsOrm(id_client=59, country='Uganda'),
      PassportsOrm(id_client=59, country='Ethiopia'),
      PassportsOrm(id_client=59, country='Tanzania'),
      PassportsOrm(id_client=59, country='Malawi'),
      PassportsOrm(id_client=59, country='Mozambique'),
      PassportsOrm(id_client=59, country='Zambia'),
      PassportsOrm(id_client=59, country='Botswana'),

      PassportsOrm(id_client=60, country='Namibia'),
      PassportsOrm(id_client=60, country='Zimbabwe'),
      PassportsOrm(id_client=60, country='South Africa'),
      PassportsOrm(id_client=60, country='Lesotho'),
      PassportsOrm(id_client=60, country='Swaziland'),
      PassportsOrm(id_client=60, country='Angola'),
      PassportsOrm(id_client=60, country='Gabon'),
      PassportsOrm(id_client=60, country='Republic of Congo'),
      PassportsOrm(id_client=60, country='Chad'),
      PassportsOrm(id_client=60, country='Central African Republic')
    ]

    passports_7=[
        PassportsOrm(id_client=61, country='Argentina'),
        PassportsOrm(id_client=61, country='Brazil'),
        PassportsOrm(id_client=61, country='Chile'),
        PassportsOrm(id_client=61, country='Colombia'),
        PassportsOrm(id_client=61, country='Peru'),
        PassportsOrm(id_client=61, country='Ecuador'),
        PassportsOrm(id_client=61, country='Bolivia'),
        PassportsOrm(id_client=61, country='Paraguay'),
        PassportsOrm(id_client=61, country='Uruguay'),
        PassportsOrm(id_client=61, country='Venezuela'),

        PassportsOrm(id_client=62, country='Poland'),
        PassportsOrm(id_client=62, country='Ukraine'),
        PassportsOrm(id_client=62, country='Czech Republic'),
        PassportsOrm(id_client=62, country='Slovakia'),
        PassportsOrm(id_client=62, country='Hungary'),
        PassportsOrm(id_client=62, country='Romania'),
        PassportsOrm(id_client=62, country='Bulgaria'),
        PassportsOrm(id_client=62, country='Croatia'),
        PassportsOrm(id_client=62, country='Serbia'),
        PassportsOrm(id_client=62, country='Bosnia and Herzegovina'),

        PassportsOrm(id_client=63, country='Nigeria'),
        PassportsOrm(id_client=63, country='South Africa'),
        PassportsOrm(id_client=63, country='Kenya'),
        PassportsOrm(id_client=63, country='Egypt'),
        PassportsOrm(id_client=63, country='Morocco'),
        PassportsOrm(id_client=63, country='Ghana'),
        PassportsOrm(id_client=63, country='Uganda'),
        PassportsOrm(id_client=63, country='Ethiopia'),
        PassportsOrm(id_client=63, country='Tanzania'),
        PassportsOrm(id_client=63, country='Algeria'),

        PassportsOrm(id_client=64, country='Australia'),
        PassportsOrm(id_client=64, country='New Zealand'),
        PassportsOrm(id_client=64, country='Papua New Guinea'),
        PassportsOrm(id_client=64, country='Fiji'),
        PassportsOrm(id_client=64, country='Solomon Islands'),
        PassportsOrm(id_client=64, country='Vanuatu'),
        PassportsOrm(id_client=64, country='Samoa'),
        PassportsOrm(id_client=64, country='Tonga'),
        PassportsOrm(id_client=64, country='Kiribati'),
        PassportsOrm(id_client=64, country='Tuvalu'),

        PassportsOrm(id_client=65, country='Thailand'),
        PassportsOrm(id_client=65, country='Vietnam'),
        PassportsOrm(id_client=65, country='Cambodia'),
        PassportsOrm(id_client=65, country='Laos'),
        PassportsOrm(id_client=65, country='Myanmar'),
        PassportsOrm(id_client=65, country='Philippines'),
        PassportsOrm(id_client=65, country='Indonesia'),
        PassportsOrm(id_client=65, country='Malaysia'),
        PassportsOrm(id_client=65, country='Singapore'),
        PassportsOrm(id_client=65, country='Brunei'),

        PassportsOrm(id_client=66, country='United States'),
        PassportsOrm(id_client=66, country='Canada'),
        PassportsOrm(id_client=66, country='Mexico'),
        PassportsOrm(id_client=66, country='Guatemala'),
        PassportsOrm(id_client=66, country='Honduras'),
        PassportsOrm(id_client=66, country='El Salvador'),
        PassportsOrm(id_client=66, country='Nicaragua'),
        PassportsOrm(id_client=66, country='Costa Rica'),
        PassportsOrm(id_client=66, country='Panama'),
        PassportsOrm(id_client=66, country='Cuba'),

        PassportsOrm(id_client=67, country='Germany'),
        PassportsOrm(id_client=67, country='France'),
        PassportsOrm(id_client=67, country='Italy'),
        PassportsOrm(id_client=67, country='Spain'),
        PassportsOrm(id_client=67, country='Portugal'),
        PassportsOrm(id_client=67, country='Netherlands'),
        PassportsOrm(id_client=67, country='Belgium'),
        PassportsOrm(id_client=67, country='Luxembourg'),
        PassportsOrm(id_client=67, country='Austria'),
        PassportsOrm(id_client=67, country='Switzerland'),

        PassportsOrm(id_client=68, country='Russia'),
        PassportsOrm(id_client=68, country='Ukraine'),
        PassportsOrm(id_client=68, country='Belarus'),
        PassportsOrm(id_client=68, country='Kazakhstan'),
        PassportsOrm(id_client=68, country='Uzbekistan'),
        PassportsOrm(id_client=68, country='Kyrgyzstan'),
        PassportsOrm(id_client=68, country='Turkmenistan'),
        PassportsOrm(id_client=68, country='Armenia'),
        PassportsOrm(id_client=68, country='Georgia'),
        PassportsOrm(id_client=68, country='Azerbaijan'),

        PassportsOrm(id_client=69, country='South Korea'),
        PassportsOrm(id_client=69, country='Japan'),
        PassportsOrm(id_client=69, country='China'),
        PassportsOrm(id_client=69, country='Taiwan'),
        PassportsOrm(id_client=69, country='Hong Kong'),
        PassportsOrm(id_client=69, country='Mongolia'),
        PassportsOrm(id_client=69, country='North Korea'),
        PassportsOrm(id_client=69, country='Macau'),
        PassportsOrm(id_client=69, country='Philippines'),
        PassportsOrm(id_client=69, country='Vietnam'),

        PassportsOrm(id_client=70, country='Brazil'),
        PassportsOrm(id_client=70, country='Argentina'),
        PassportsOrm(id_client=70, country='Chile'),
        PassportsOrm(id_client=70, country='Peru'),
        PassportsOrm(id_client=70, country='Colombia'),
        PassportsOrm(id_client=70, country='Ecuador'),
        PassportsOrm(id_client=70, country='Bolivia'),
        PassportsOrm(id_client=70, country='Paraguay'),
        PassportsOrm(id_client=70, country='Uruguay'),
        PassportsOrm(id_client=70, country='Venezuela')

    ]

    passports_8=[
        PassportsOrm(id_client=71, country='Turkey'),
        PassportsOrm(id_client=71, country='Greece'),
        PassportsOrm(id_client=71, country='Cyprus'),
        PassportsOrm(id_client=71, country='Israel'),
        PassportsOrm(id_client=71, country='Lebanon'),
        PassportsOrm(id_client=71, country='Syria'),
        PassportsOrm(id_client=71, country='Jordan'),
        PassportsOrm(id_client=71, country='Saudi Arabia'),
        PassportsOrm(id_client=71, country='Egypt'),
        PassportsOrm(id_client=71, country='United Arab Emirates'),

        PassportsOrm(id_client=72, country='Ireland'),
        PassportsOrm(id_client=72, country='United Kingdom'),
        PassportsOrm(id_client=72, country='Scotland'),
        PassportsOrm(id_client=72, country='Wales'),
        PassportsOrm(id_client=72, country='Northern Ireland'),
        PassportsOrm(id_client=72, country='Bermuda'),
        PassportsOrm(id_client=72, country='Channel Islands'),
        PassportsOrm(id_client=72, country='Isle of Man'),
        PassportsOrm(id_client=72, country='Jersey'),
        PassportsOrm(id_client=72, country='Guernsey'),

        PassportsOrm(id_client=73, country='Norway'),
        PassportsOrm(id_client=73, country='Sweden'),
        PassportsOrm(id_client=73, country='Finland'),
        PassportsOrm(id_client=73, country='Denmark'),
        PassportsOrm(id_client=73, country='Iceland'),
        PassportsOrm(id_client=73, country='Greenland'),
        PassportsOrm(id_client=73, country='Faroe Islands'),
        PassportsOrm(id_client=73, country='Aland Islands'),
        PassportsOrm(id_client=73, country='Svalbard'),
        PassportsOrm(id_client=73, country='Bouvet Island'),

        PassportsOrm(id_client=74, country='Belgium'),
        PassportsOrm(id_client=74, country='Luxembourg'),
        PassportsOrm(id_client=74, country='Netherlands'),
        PassportsOrm(id_client=74, country='Germany'),
        PassportsOrm(id_client=74, country='France'),
        PassportsOrm(id_client=74, country='Switzerland'),
        PassportsOrm(id_client=74, country='Liechtenstein'),
        PassportsOrm(id_client=74, country='Austria'),
        PassportsOrm(id_client=74, country='Italy'),
        PassportsOrm(id_client=74, country='Monaco'),

        PassportsOrm(id_client=75, country='Chile'),
        PassportsOrm(id_client=75, country='Argentina'),
        PassportsOrm(id_client=75, country='Brazil'),
        PassportsOrm(id_client=75, country='Peru'),
        PassportsOrm(id_client=75, country='Colombia'),
        PassportsOrm(id_client=75, country='Bolivia'),
        PassportsOrm(id_client=75, country='Ecuador'),
        PassportsOrm(id_client=75, country='Uruguay'),
        PassportsOrm(id_client=75, country='Venezuela'),
        PassportsOrm(id_client=75, country='Paraguay'),

        PassportsOrm(id_client=76, country='South Africa'),
        PassportsOrm(id_client=76, country='Kenya'),
        PassportsOrm(id_client=76, country='Nigeria'),
        PassportsOrm(id_client=76, country='Ethiopia'),
        PassportsOrm(id_client=76, country='Egypt'),
        PassportsOrm(id_client=76, country='Morocco'),
        PassportsOrm(id_client=76, country='Algeria'),
        PassportsOrm(id_client=76, country='Ghana'),
        PassportsOrm(id_client=76, country='Uganda'),
        PassportsOrm(id_client=76, country='Tanzania'),

        PassportsOrm(id_client=77, country='China'),
        PassportsOrm(id_client=77, country='India'),
        PassportsOrm(id_client=77, country='Nepal'),
        PassportsOrm(id_client=77, country='Sri Lanka'),
        PassportsOrm(id_client=77, country='Bhutan'),
        PassportsOrm(id_client=77, country='Bangladesh'),
        PassportsOrm(id_client=77, country='Pakistan'),
        PassportsOrm(id_client=77, country='Afghanistan'),
        PassportsOrm(id_client=77, country='Maldives'),
        PassportsOrm(id_client=77, country='Myanmar'),

        PassportsOrm(id_client=78, country='Australia'),
        PassportsOrm(id_client=78, country='New Zealand'),
        PassportsOrm(id_client=78, country='Fiji'),
        PassportsOrm(id_client=78, country='Vanuatu'),
        PassportsOrm(id_client=78, country='Samoa'),
        PassportsOrm(id_client=78, country='Tonga'),
        PassportsOrm(id_client=78, country='Solomon Islands'),
        PassportsOrm(id_client=78, country='Papua New Guinea'),
        PassportsOrm(id_client=78, country='Kiribati'),
        PassportsOrm(id_client=78, country='Tuvalu'),

        PassportsOrm(id_client=79, country='Portugal'),
        PassportsOrm(id_client=79, country='Spain'),
        PassportsOrm(id_client=79, country='France'),
        PassportsOrm(id_client=79, country='Germany'),
        PassportsOrm(id_client=79, country='Italy'),
        PassportsOrm(id_client=79, country='Austria'),
        PassportsOrm(id_client=79, country='Belgium'),
        PassportsOrm(id_client=79, country='Netherlands'),
        PassportsOrm(id_client=79, country='Luxembourg'),
        PassportsOrm(id_client=79, country='Switzerland'),

        PassportsOrm(id_client=80, country='United States'),
        PassportsOrm(id_client=80, country='Canada'),
        PassportsOrm(id_client=80, country='Mexico'),
        PassportsOrm(id_client=80, country='Guatemala'),
        PassportsOrm(id_client=80, country='Honduras'),
        PassportsOrm(id_client=80, country='El Salvador'),
        PassportsOrm(id_client=80, country='Costa Rica'),
        PassportsOrm(id_client=80, country='Panama'),
        PassportsOrm(id_client=80, country='Cuba'),
        PassportsOrm(id_client=80, country='Dominican Republic')

    ]

    passports_9=[
        PassportsOrm(id_client=81, country='Brazil'),
        PassportsOrm(id_client=81, country='Argentina'),
        PassportsOrm(id_client=81, country='Chile'),
        PassportsOrm(id_client=81, country='Peru'),
        PassportsOrm(id_client=81, country='Colombia'),
        PassportsOrm(id_client=81, country='Bolivia'),
        PassportsOrm(id_client=81, country='Ecuador'),
        PassportsOrm(id_client=81, country='Uruguay'),
        PassportsOrm(id_client=81, country='Venezuela'),
        PassportsOrm(id_client=81, country='Paraguay'),

        PassportsOrm(id_client=82, country='Canada'),
        PassportsOrm(id_client=82, country='United States'),
        PassportsOrm(id_client=82, country='Mexico'),
        PassportsOrm(id_client=82, country='Cuba'),
        PassportsOrm(id_client=82, country='Guatemala'),
        PassportsOrm(id_client=82, country='Honduras'),
        PassportsOrm(id_client=82, country='El Salvador'),
        PassportsOrm(id_client=82, country='Costa Rica'),
        PassportsOrm(id_client=82, country='Panama'),
        PassportsOrm(id_client=82, country='Dominican Republic'),

        PassportsOrm(id_client=83, country='France'),
        PassportsOrm(id_client=83, country='Germany'),
        PassportsOrm(id_client=83, country='Italy'),
        PassportsOrm(id_client=83, country='Spain'),
        PassportsOrm(id_client=83, country='Portugal'),
        PassportsOrm(id_client=83, country='Belgium'),
        PassportsOrm(id_client=83, country='Luxembourg'),
        PassportsOrm(id_client=83, country='Netherlands'),
        PassportsOrm(id_client=83, country='Switzerland'),
        PassportsOrm(id_client=83, country='Austria'),

        PassportsOrm(id_client=84, country='Turkey'),
        PassportsOrm(id_client=84, country='Greece'),
        PassportsOrm(id_client=84, country='Cyprus'),
        PassportsOrm(id_client=84, country='Israel'),
        PassportsOrm(id_client=84, country='Lebanon'),
        PassportsOrm(id_client=84, country='Syria'),
        PassportsOrm(id_client=84, country='Jordan'),
        PassportsOrm(id_client=84, country='Saudi Arabia'),
        PassportsOrm(id_client=84, country='Egypt'),
        PassportsOrm(id_client=84, country='United Arab Emirates'),

        PassportsOrm(id_client=85, country='Australia'),
        PassportsOrm(id_client=85, country='New Zealand'),
        PassportsOrm(id_client=85, country='Fiji'),
        PassportsOrm(id_client=85, country='Vanuatu'),
        PassportsOrm(id_client=85, country='Samoa'),
        PassportsOrm(id_client=85, country='Tonga'),
        PassportsOrm(id_client=85, country='Solomon Islands'),
        PassportsOrm(id_client=85, country='Papua New Guinea'),
        PassportsOrm(id_client=85, country='Kiribati'),
        PassportsOrm(id_client=85, country='Tuvalu'),

        PassportsOrm(id_client=86, country='China'),
        PassportsOrm(id_client=86, country='India'),
        PassportsOrm(id_client=86, country='Nepal'),
        PassportsOrm(id_client=86, country='Sri Lanka'),
        PassportsOrm(id_client=86, country='Bhutan'),
        PassportsOrm(id_client=86, country='Bangladesh'),
        PassportsOrm(id_client=86, country='Pakistan'),
        PassportsOrm(id_client=86, country='Afghanistan'),
        PassportsOrm(id_client=86, country='Maldives'),
        PassportsOrm(id_client=86, country='Myanmar'),

        PassportsOrm(id_client=87, country='South Africa'),
        PassportsOrm(id_client=87, country='Kenya'),
        PassportsOrm(id_client=87, country='Nigeria'),
        PassportsOrm(id_client=87, country='Ethiopia'),
        PassportsOrm(id_client=87, country='Egypt'),
        PassportsOrm(id_client=87, country='Morocco'),
        PassportsOrm(id_client=87, country='Algeria'),
        PassportsOrm(id_client=87, country='Ghana'),
        PassportsOrm(id_client=87, country='Uganda'),
        PassportsOrm(id_client=87, country='Tanzania'),

        PassportsOrm(id_client=88, country='Japan'),
        PassportsOrm(id_client=88, country='South Korea'),
        PassportsOrm(id_client=88, country='North Korea'),
        PassportsOrm(id_client=88, country='Mongolia'),
        PassportsOrm(id_client=88, country='Taiwan'),
        PassportsOrm(id_client=88, country='Hong Kong'),
        PassportsOrm(id_client=88, country='Macau'),
        PassportsOrm(id_client=88, country='Philippines'),
        PassportsOrm(id_client=88, country='Indonesia'),
        PassportsOrm(id_client=88, country='Malaysia'),

        PassportsOrm(id_client=89, country='Brazil'),
        PassportsOrm(id_client=89, country='Argentina'),
        PassportsOrm(id_client=89, country='Chile'),
        PassportsOrm(id_client=89, country='Peru'),
        PassportsOrm(id_client=89, country='Colombia'),
        PassportsOrm(id_client=89, country='Bolivia'),
        PassportsOrm(id_client=89, country='Ecuador'),
        PassportsOrm(id_client=89, country='Uruguay'),
        PassportsOrm(id_client=89, country='Venezuela'),
        PassportsOrm(id_client=89, country='Paraguay'),

        PassportsOrm(id_client=90, country='Italy'),
        PassportsOrm(id_client=90, country='France'),
        PassportsOrm(id_client=90, country='Germany'),
        PassportsOrm(id_client=90, country='Spain'),
        PassportsOrm(id_client=90, country='Portugal'),
        PassportsOrm(id_client=90, country='Belgium'),
        PassportsOrm(id_client=90, country='Netherlands'),
        PassportsOrm(id_client=90, country='Luxembourg'),
        PassportsOrm(id_client=90, country='Switzerland'),
        PassportsOrm(id_client=90, country='Austria'),
    ]

    passports_10=[
        PassportsOrm(id_client=91, country='United Kingdom'),
        PassportsOrm(id_client=91, country='Ireland'),
        PassportsOrm(id_client=91, country='France'),
        PassportsOrm(id_client=91, country='Germany'),
        PassportsOrm(id_client=91, country='Italy'),
        PassportsOrm(id_client=91, country='Spain'),
        PassportsOrm(id_client=91, country='Netherlands'),
        PassportsOrm(id_client=91, country='Belgium'),
        PassportsOrm(id_client=91, country='Luxembourg'),
        PassportsOrm(id_client=91, country='Portugal'),

        PassportsOrm(id_client=92, country='Russia'),
        PassportsOrm(id_client=92, country='Ukraine'),
        PassportsOrm(id_client=92, country='Belarus'),
        PassportsOrm(id_client=92, country='Kazakhstan'),
        PassportsOrm(id_client=92, country='Georgia'),
        PassportsOrm(id_client=92, country='Armenia'),
        PassportsOrm(id_client=92, country='Azerbaijan'),
        PassportsOrm(id_client=92, country='Uzbekistan'),
        PassportsOrm(id_client=92, country='Turkmenistan'),
        PassportsOrm(id_client=92, country='Kyrgyzstan'),

        PassportsOrm(id_client=93, country='United States'),
        PassportsOrm(id_client=93, country='Canada'),
        PassportsOrm(id_client=93, country='Mexico'),
        PassportsOrm(id_client=93, country='Cuba'),
        PassportsOrm(id_client=93, country='Panama'),
        PassportsOrm(id_client=93, country='Dominican Republic'),
        PassportsOrm(id_client=93, country='Guatemala'),
        PassportsOrm(id_client=93, country='Honduras'),
        PassportsOrm(id_client=93, country='El Salvador'),
        PassportsOrm(id_client=93, country='Costa Rica'),

        PassportsOrm(id_client=94, country='Japan'),
        PassportsOrm(id_client=94, country='South Korea'),
        PassportsOrm(id_client=94, country='Taiwan'),
        PassportsOrm(id_client=94, country='Hong Kong'),
        PassportsOrm(id_client=94, country='Mongolia'),
        PassportsOrm(id_client=94, country='North Korea'),
        PassportsOrm(id_client=94, country='Philippines'),
        PassportsOrm(id_client=94, country='Indonesia'),
        PassportsOrm(id_client=94, country='Malaysia'),
        PassportsOrm(id_client=94, country='Singapore'),

        PassportsOrm(id_client=95, country='Brazil'),
        PassportsOrm(id_client=95, country='Argentina'),
        PassportsOrm(id_client=95, country='Chile'),
        PassportsOrm(id_client=95, country='Peru'),
        PassportsOrm(id_client=95, country='Colombia'),
        PassportsOrm(id_client=95, country='Bolivia'),
        PassportsOrm(id_client=95, country='Ecuador'),
        PassportsOrm(id_client=95, country='Venezuela'),
        PassportsOrm(id_client=95, country='Paraguay'),
        PassportsOrm(id_client=95, country='Uruguay'),

        PassportsOrm(id_client=96, country='South Africa'),
        PassportsOrm(id_client=96, country='Nigeria'),
        PassportsOrm(id_client=96, country='Kenya'),
        PassportsOrm(id_client=96, country='Egypt'),
        PassportsOrm(id_client=96, country='Morocco'),
        PassportsOrm(id_client=96, country='Algeria'),
        PassportsOrm(id_client=96, country='Ghana'),
        PassportsOrm(id_client=96, country='Uganda'),
        PassportsOrm(id_client=96, country='Ethiopia'),
        PassportsOrm(id_client=96, country='Tanzania'),

        PassportsOrm(id_client=97, country='Australia'),
        PassportsOrm(id_client=97, country='New Zealand'),
        PassportsOrm(id_client=97, country='Fiji'),
        PassportsOrm(id_client=97, country='Samoa'),
        PassportsOrm(id_client=97, country='Vanuatu'),
        PassportsOrm(id_client=97, country='Tonga'),
        PassportsOrm(id_client=97, country='Solomon Islands'),
        PassportsOrm(id_client=97, country='Papua New Guinea'),
        PassportsOrm(id_client=97, country='Kiribati'),
        PassportsOrm(id_client=97, country='Tuvalu'),

        PassportsOrm(id_client=98, country='China'),
        PassportsOrm(id_client=98, country='India'),
        PassportsOrm(id_client=98, country='Nepal'),
        PassportsOrm(id_client=98, country='Sri Lanka'),
        PassportsOrm(id_client=98, country='Bangladesh'),
        PassportsOrm(id_client=98, country='Pakistan'),
        PassportsOrm(id_client=98, country='Afghanistan'),
        PassportsOrm(id_client=98, country='Myanmar'),
        PassportsOrm(id_client=98, country='Maldives'),
        PassportsOrm(id_client=98, country='Bhutan'),

        PassportsOrm(id_client=99, country='France'),
        PassportsOrm(id_client=99, country='Germany'),
        PassportsOrm(id_client=99, country='Italy'),
        PassportsOrm(id_client=99, country='Spain'),
        PassportsOrm(id_client=99, country='Portugal'),
        PassportsOrm(id_client=99, country='Belgium'),
        PassportsOrm(id_client=99, country='Netherlands'),
        PassportsOrm(id_client=99, country='Luxembourg'),
        PassportsOrm(id_client=99, country='Switzerland'),
        PassportsOrm(id_client=99, country='Austria'),

        PassportsOrm(id_client=100, country='United Kingdom'),
        PassportsOrm(id_client=100, country='Ireland'),
        PassportsOrm(id_client=100, country='France'),
        PassportsOrm(id_client=100, country='Germany'),
        PassportsOrm(id_client=100, country='Italy'),
        PassportsOrm(id_client=100, country='Spain'),
        PassportsOrm(id_client=100, country='Netherlands'),
        PassportsOrm(id_client=100, country='Belgium'),
        PassportsOrm(id_client=100, country='Luxembourg'),
        PassportsOrm(id_client=100, country='Portugal'),

    ]

    with session_factory() as session:
        session.add_all(passports_10)
        session.commit()

def select_data():
    with session_factory() as sess:
        query = select(ProviderOrm)
        result = sess.execute(query)
        providers = result.scalars().all()
        lst_provider = []

        for provider in providers:
            print(f"ID: {provider.id_provider}, Name: {provider.name_of_provider}, "
                  f"Representative: {provider.representative}, Speak To: {provider.speak_to}, "
                  f"Phone: {provider.phone}, Address: {provider.address}")
            lst_provider.append(provider.name_of_provider)
        return lst_provider

def select_data_join():
    with session_factory() as sess:
        result = sess.query(SupplyOrm, ProviderOrm) \
            .join(ProviderOrm, SupplyOrm.id_provider == ProviderOrm.id_provider) \
            .all()

        lst_result = []
        for supply, provider in result:
            print(
                f"Supply ID: {supply.id_supply}, Provider: {provider.name_of_provider}, Date: {supply.date_of_supply}")
            lst_result.append([supply.id_supply, provider.name_of_provider, supply.date_of_supply])
        return lst_result

def update_data(id_provider: int):
    with session_factory() as sess:
        provider_line = sess.get(ProviderOrm, id_provider)
        provider_line.representative = 'Станислалво Вактор'
        sess.commit()

def insert_line_provider():
    with session_factory() as sess:
        new_worker = ProviderOrm(name_of_provider = 'ООО Крольчанск', representative = 'Кирстн Данст', speak_to = 'мисс Данст', phone = "+78457654738", address = 'село Капустино')
        sess.add(new_worker)
        sess.commit()

def delete_line_provider(id_provider: int):
    with session_factory() as sess:
        provider_line = sess.get(ProviderOrm, id_provider)
        sess.delete(provider_line)
        sess.commit()

#Получите данные вместе с WHERE, ORDER BY, GROUP BY, DISTINCT и выведите на экран.
#Примените несколько функций агрегации и выведите результат на экран

def select_where():
    with session_factory() as sess:
        query = select(ProviderOrm).where(ProviderOrm.name_of_provider == 'STC')
        result = sess.execute(query)
        providers = result.scalars().all()

        for provider in providers:
            print(f"ID: {provider.id_provider}, Name: {provider.name_of_provider}, "
                  f"Representative: {provider.representative}, Speak To: {provider.speak_to}, "
                  f"Phone: {provider.phone}, Address: {provider.address}")

def select_order_by():
    with session_factory() as sess:
        query = select(ProviderOrm).order_by(ProviderOrm.id_provider.desc())
        result = sess.execute(query)
        providers = result.scalars().all()

        for provider in providers:
            print(f"ID: {provider.id_provider}, Name: {provider.name_of_provider}, "
                  f"Representative: {provider.representative}, Speak To: {provider.speak_to}, "
                  f"Phone: {provider.phone}, Address: {provider.address}")

def select_group_by():
    with session_factory() as sess:
        query = (
            select(SupplyOrm.id_provider, func.count(SupplyOrm.id_supply).label("provider_count"))
            .group_by(SupplyOrm.id_provider)
        )
        result = sess.execute(query)
        supplys = result.all()

        supplys_lib={}
        for supply in supplys:
            print(f"Provider: {supply.id_provider}, Count: {supply.provider_count}")
            supplys_lib[supply.id_provider] = supply.provider_count
        return supplys_lib

def select_distinct_dates():
    with session_factory() as sess:
        # Получаем уникальные даты из таблицы SupplyOrm
        result = sess.query(SupplyOrm.date_of_supply).distinct().all()
        lst = []
        print("Уникальные даты поставок:")
        for date in result:
            print(date[0])  # Каждая запись — это кортеж, поэтому берем первый элемент
            lst.append(date[0])
        return lst
#Воспроизвёл проблему M+1. #0.36
def get_passports_and_client_id():
    with session_factory() as sess:

        passports = sess.query(PassportsOrm).all()  # 1 запрос для получения всех паспортов

        for passport in passports:
            client = sess.query(ClientOrm).filter_by(id=passport.id_client).first()  # 1 запрос для каждого паспорта
            print(f"Passport ID: {passport.id_passport}, Client Name: {client.full_name}, Country of Passpport: {passport.country}")

from sqlalchemy.orm import joinedload

# Решил проблему M+1 #0.02
def joined_load_passports_and_client_id():
    with session_factory() as sess:
        passports = (
            sess.query(PassportsOrm)
            .options(joinedload(PassportsOrm.client))  # Подключаем данные клиентов в один запрос
            .all()
        )
        for passport in passports:
            print(f"Passport ID: {passport.id_passport}, Client Name: {passport.client.full_name}, Country: {passport.country}")