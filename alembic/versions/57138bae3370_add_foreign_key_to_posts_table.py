"""add foreign-key to posts table

Revision ID: 57138bae3370
Revises: ec41973a7f84
Create Date: 2021-11-11 13:11:25.861840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57138bae3370'
down_revision = 'ec41973a7f84'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
        'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
