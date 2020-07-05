"""empty message

Revision ID: 9883c888226d
Revises: 1d5867139837
Create Date: 2020-07-02 16:06:36.472262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9883c888226d'
down_revision = '1d5867139837'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'artists', ['id'])
    op.create_unique_constraint(None, 'venues', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'venues', type_='unique')
    op.drop_constraint(None, 'artists', type_='unique')
    op.drop_table('shows')
    # ### end Alembic commands ###