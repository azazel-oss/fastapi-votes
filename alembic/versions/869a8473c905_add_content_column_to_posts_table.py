"""add content column to posts table

Revision ID: 869a8473c905
Revises: 03f47b39ffbf
Create Date: 2021-11-11 12:51:45.300235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '869a8473c905'
down_revision = '03f47b39ffbf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
