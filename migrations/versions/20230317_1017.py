"""empty message

Revision ID: 02232220d2e7
Revises: 
Create Date: 2023-03-17 10:17:18.757571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02232220d2e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currency',
    sa.Column('currency_id', sa.String(length=3), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('symbol', sa.String(length=3), nullable=True),
    sa.PrimaryKeyConstraint('currency_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('currency')
    # ### end Alembic commands ###
