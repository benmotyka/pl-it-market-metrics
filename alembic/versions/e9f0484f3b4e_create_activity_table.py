"""create activity table

Revision ID: e9f0484f3b4e
Revises: 
Create Date: 2023-04-18 23:34:05.322627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9f0484f3b4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'activity',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.String(20), nullable=False),
        sa.Column('domain', sa.String(30), nullable=False),
    )


def downgrade():
    op.drop_table('activity')
