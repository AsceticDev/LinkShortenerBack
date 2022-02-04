"""changes to shortenedLink

Revision ID: 3c26510ff7ac
Revises: a27049ed88ba
Create Date: 2021-12-09 22:20:34.547449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c26510ff7ac'
down_revision = 'a27049ed88ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shortened_link', sa.Column('_linkHash', sa.String(length=50), nullable=False))
    op.drop_column('shortened_link', 'linkHash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shortened_link', sa.Column('linkHash', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.drop_column('shortened_link', '_linkHash')
    # ### end Alembic commands ###
