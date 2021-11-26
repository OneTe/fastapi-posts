"""create posts table

Revision ID: 587e2dd82e37
Revises: 
Create Date: 2021-11-25 17:46:35.426634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '587e2dd82e37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.BigInteger, nullable=False,
                    primary_key=True), sa.Column('title', sa.String(128), nullable=False),
                    sa.Column('content', sa.String(1024), nullable=False),sa.Column(
        'published', sa.SmallInteger, nullable=False, server_default='1'),sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_table('posts')
    pass
