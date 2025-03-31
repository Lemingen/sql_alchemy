from time import time

from queries.core import create, drop, insert_data
from queries.orm import create_orm, insert_provider_orm, insert_supply_orm, insert_product_orm, insert_client_orm, \
    insert_orders_orm, get_passports_and_client_id, joined_load_passports_and_client_id
from src.queries.orm import insert_employee_orm, select_data, update_data, insert_line_provider, delete_line_provider, \
    select_data_join, select_where, select_group_by, select_order_by, select_distinct_dates, delete_orm, insert_passports_orm

#create()
#insert_data()
#drop()

#create_orm()
#insert_provider_orm()
#insert_supply_orm()
#insert_product_orm()
#insert_employee_orm()
#insert_client_orm()
#insert_orders_orm()

#select_data()
#update_data(2)
#insert_line_provider()
#select_data()
#print()
#delete_line_provider(6)
#print()

#select_data()
#select_data_join()
#select_where()
#select_group_by()
#select_distinct_dates()
#delete_orm()

#insert_client_orm()
#insert_passports_orm()

"""first_time = time()
get_passports_and_client_id()
result_time = time() - first_time
print(result_time)"""

"""first_time = time()
joined_load_passports_and_client_id()
result_time = time() - first_time
print(result_time)"""

#select_where()
#select_order_by()
#print(select_group_by())
