"""create task table full

Revision ID: caffd67504b8
Revises: 28d7ef256a16
Create Date: 2020-10-12 10:36:35.748121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caffd67504b8'
down_revision = '28d7ef256a16'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('tasks',sa.Column('title',sa.String(50))),
    op.add_column('tasks',sa.Column('description',sa.String(255))),
    op.add_column('tasks',sa.Column('done',sa.String(50)))


def downgrade():
    op.drop_column('tasks','title'),
    op.drop_column('tasks','description'),
	
	
