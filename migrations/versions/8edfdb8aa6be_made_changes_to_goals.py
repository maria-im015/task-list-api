"""made changes to goals

Revision ID: 8edfdb8aa6be
Revises: 05ca64e08f9b
Create Date: 2021-05-11 17:26:18.775914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8edfdb8aa6be'
down_revision = '05ca64e08f9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
