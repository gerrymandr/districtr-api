"""empty message

Revision ID: b4c1256e19ea
Revises: 609a04eee503
Create Date: 2019-05-11 22:14:01.618601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b4c1256e19ea"
down_revision = "609a04eee503"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("place", sa.Column("slug", sa.String(length=80), nullable=False))
    op.add_column("place", sa.Column("state", sa.String(length=80), nullable=False))
    op.create_index(op.f("ix_place_slug"), "place", ["slug"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_place_slug"), table_name="place")
    op.drop_column("place", "state")
    op.drop_column("place", "slug")
    # ### end Alembic commands ###