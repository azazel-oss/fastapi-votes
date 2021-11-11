"""create posts table

Revision ID: 03f47b39ffbf
Revises: 
Create Date: 2021-11-11 12:24:12.050050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03f47b39ffbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
