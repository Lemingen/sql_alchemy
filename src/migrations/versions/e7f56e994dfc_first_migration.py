"""first_migration

Revision ID: e7f56e994dfc
Revises: 
Create Date: 2025-03-29 19:08:22.844277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7f56e994dfc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id_employee', sa.Integer(), nullable=False),
    sa.Column('family', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('job_title', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('home_phone', sa.String(), nullable=False),
    sa.Column('birthday', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id_employee')
    )
    op.create_table('provider',
    sa.Column('id_provider', sa.Integer(), nullable=False),
    sa.Column('name_of_provider', sa.String(), nullable=False),
    sa.Column('representative', sa.String(), nullable=False),
    sa.Column('speak_to', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id_provider')
    )
    op.create_table('supply',
    sa.Column('id_supply', sa.Integer(), nullable=False),
    sa.Column('id_provider', sa.Integer(), nullable=False),
    sa.Column('date_of_supply', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_provider'], ['provider.id_provider'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_supply')
    )
    op.create_table('products',
    sa.Column('id_product', sa.Integer(), nullable=False),
    sa.Column('id_supply', sa.Integer(), nullable=False),
    sa.Column('name_of_product', sa.String(), nullable=False),
    sa.Column('specifications', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('purchase_cost', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('selling_cost', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_supply'], ['supply.id_supply'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_product')
    )
    op.create_table('orders',
    sa.Column('id_order', sa.Integer(), nullable=False),
    sa.Column('id_employee', sa.Integer(), nullable=False),
    sa.Column('id_product', sa.Integer(), nullable=False),
    sa.Column('id_client', sa.Integer(), nullable=False),
    sa.Column('posting_date', sa.String(), nullable=False),
    sa.Column('execution_date', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_client'], ['client.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_employee'], ['employees.id_employee'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_product'], ['products.id_product'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_order')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('products')
    op.drop_table('supply')
    op.drop_table('provider')
    op.drop_table('employees')
    op.drop_table('client')
    # ### end Alembic commands ###
