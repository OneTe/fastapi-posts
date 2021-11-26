"""create user table

Revision ID: 774755d36759
Revises: 587e2dd82e37
Create Date: 2021-11-25 17:49:54.677277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '774755d36759'
down_revision = '587e2dd82e37'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.BigInteger, nullable=False),
                    sa.Column('email', sa.String(128), nullable=False),
                    sa.Column('password', sa.String(128), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
