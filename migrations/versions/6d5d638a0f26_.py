"""empty message

Revision ID: 6d5d638a0f26
Revises: 1a0c0c972818
Create Date: 2019-05-14 15:31:38.054208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d5d638a0f26'
down_revision = '1a0c0c972818'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plan', sa.Column('problem_id', sa.Integer(), nullable=False))
    op.add_column('plan', sa.Column('units_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'plan', 'districting_problem', ['problem_id'], ['id'])
    op.create_foreign_key(None, 'plan', 'unit_set', ['units_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'plan', type_='foreignkey')
    op.drop_constraint(None, 'plan', type_='foreignkey')
    op.drop_column('plan', 'units_id')
    op.drop_column('plan', 'problem_id')
    # ### end Alembic commands ###