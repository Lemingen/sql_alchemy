from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Boolean
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


#декларативный стиль
class ProviderOrm(Base):
    __tablename__ = 'provider'

    id_provider: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name_of_provider: Mapped[str] = mapped_column(nullable=False)
    representative: Mapped[str] = mapped_column(nullable=False)
    speak_to: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)

class SupplyOrm(Base):
    __tablename__ = 'supply'

    id_supply: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    id_provider: Mapped[int] = mapped_column(ForeignKey('provider.id_provider', ondelete='CASCADE'))
    date_of_supply: Mapped[str]
    test: Mapped[str]

class ProductsOrm(Base):
    __tablename__ = 'products'

    id_product: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    id_supply: Mapped[int] = mapped_column(ForeignKey('supply.id_supply', ondelete='CASCADE'))
    name_of_product: Mapped[str]
    specifications: Mapped[str]
    description: Mapped[str]
    image: Mapped[str]
    purchase_cost: Mapped[int]
    availability: Mapped[bool] = mapped_column(Boolean, default = False)
    quantity: Mapped[int]
    selling_cost: Mapped[int]

class EmployeesOrm(Base):
    __tablename__ = 'employees'

    id_employee: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    family: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    job_title: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    home_phone: Mapped[str] = mapped_column(nullable=False)
    birthday: Mapped[str] = mapped_column(nullable=False)

class ClientOrm(Base):
    __tablename__ = 'client'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    full_name: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)

    passports = relationship("PassportsOrm", back_populates="client")  # Один клиент - много паспортов


class OrdersOrm(Base):
    __tablename__ = 'orders'

    id_order: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    id_employee: Mapped[int] = mapped_column(ForeignKey('employees.id_employee', ondelete='CASCADE'))
    id_product: Mapped[int] = mapped_column(ForeignKey('products.id_product', ondelete='CASCADE'))
    id_client: Mapped[int] = mapped_column(ForeignKey('client.id', ondelete='CASCADE'))
    posting_date: Mapped[str]
    execution_date: Mapped[str]

class PassportsOrm(Base):
    __tablename__ = 'pasports'

    id_passport: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    id_client: Mapped[int] = mapped_column(ForeignKey('client.id', ondelete='CASCADE'))
    country: Mapped[str]

    client = relationship("ClientOrm", back_populates="passports")  # Много паспортов - один клиент


metadata_obj = MetaData()

provider_table = Table(
    "provider",
    metadata_obj,
    Column("id_provider", Integer, nullable=False, primary_key=True),
    Column("name_of_provider", String, nullable=False),
    Column("representative", String, nullable=False),
    Column("speak_to", String, nullable=False),
    Column("phone", String, nullable=False),
    Column("address", String, nullable=False),
)