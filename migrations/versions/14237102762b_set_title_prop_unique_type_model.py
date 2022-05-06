"""set title prop unique type model

Revision ID: 14237102762b
Revises: 489241e392f3
Create Date: 2022-05-06 12:11:05.671869

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '14237102762b'
down_revision = '489241e392f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_types_title', table_name='types')
    op.create_unique_constraint(None, 'types', ['title'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'types', type_='unique')
    op.create_index('ix_types_title', 'types', ['title'], unique=False)
    # ### end Alembic commands ###
