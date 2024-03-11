"""Tweaked models

Revision ID: 1f351877e981
Revises: ef3de0d2ab7a
Create Date: 2024-03-11 23:30:59.201682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f351877e981'
down_revision = 'ef3de0d2ab7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('pizza_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.alter_column('pizza_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
