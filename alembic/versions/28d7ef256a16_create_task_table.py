"""create task table

Revision ID: 28d7ef256a16
Revises: 
Create Date: 2020-10-12 10:11:09.206127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28d7ef256a16'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    	'tasks',
    	sa.Column('id', sa.Integer, primary_key=True)

	)
def downgrade():
    op.drop_table('tasks')
