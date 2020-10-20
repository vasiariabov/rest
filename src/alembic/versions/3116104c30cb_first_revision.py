"""First revision

Revision ID: 3116104c30cb
Revises: 
Create Date: 2020-10-20 14:01:41.954779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3116104c30cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    	'task',
    	sa.Column('id', sa.Integer, primary_key=True),
    	sa.Column('title', sa.String(50)),
    	sa.Column('description', sa.String(255)),
    	sa.Column('done', sa.String(50)),
    )	


def downgrade():
    op.drop_table('account')
