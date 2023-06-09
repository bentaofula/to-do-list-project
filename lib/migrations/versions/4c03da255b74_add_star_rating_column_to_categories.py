"""Add star_rating column to categories

Revision ID: 4c03da255b74
Revises: f24c040b6786
Create Date: 2023-06-08 02:29:28.848899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c03da255b74'
down_revision = 'f24c040b6786'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('star_rating', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('categories', 'star_rating')
    # ### end Alembic commands ###
