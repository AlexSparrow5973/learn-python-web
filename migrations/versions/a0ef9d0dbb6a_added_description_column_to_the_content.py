"""added description column to the Content

Revision ID: a0ef9d0dbb6a
Revises: b1d19d2039ec
Create Date: 2022-07-05 22:56:21.809391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0ef9d0dbb6a'
down_revision = 'b1d19d2039ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('content', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('content', 'description')
    # ### end Alembic commands ###
