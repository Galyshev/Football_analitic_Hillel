"""init

Revision ID: 747c07e2e66a
Revises: 
Create Date: 2023-03-14 12:39:58.730058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '747c07e2e66a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('england_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('club_name', sa.String(), nullable=True),
    sa.Column('club_stat_url', sa.String(), nullable=True),
    sa.Column('game', sa.Integer(), nullable=True),
    sa.Column('won', sa.Integer(), nullable=True),
    sa.Column('drawn', sa.Integer(), nullable=True),
    sa.Column('lost', sa.Integer(), nullable=True),
    sa.Column('goals_for', sa.Integer(), nullable=True),
    sa.Column('goals_against', sa.Integer(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('date_add', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('france_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('club_name', sa.String(), nullable=True),
    sa.Column('club_stat_url', sa.String(), nullable=True),
    sa.Column('game', sa.Integer(), nullable=True),
    sa.Column('won', sa.Integer(), nullable=True),
    sa.Column('drawn', sa.Integer(), nullable=True),
    sa.Column('lost', sa.Integer(), nullable=True),
    sa.Column('goals_for', sa.Integer(), nullable=True),
    sa.Column('goals_against', sa.Integer(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('date_add', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('germany_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('club_name', sa.String(), nullable=True),
    sa.Column('club_stat_url', sa.String(), nullable=True),
    sa.Column('game', sa.Integer(), nullable=True),
    sa.Column('won', sa.Integer(), nullable=True),
    sa.Column('drawn', sa.Integer(), nullable=True),
    sa.Column('lost', sa.Integer(), nullable=True),
    sa.Column('goals_for', sa.Integer(), nullable=True),
    sa.Column('goals_against', sa.Integer(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('date_add', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('italy_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('club_name', sa.String(), nullable=True),
    sa.Column('club_stat_url', sa.String(), nullable=True),
    sa.Column('game', sa.Integer(), nullable=True),
    sa.Column('won', sa.Integer(), nullable=True),
    sa.Column('drawn', sa.Integer(), nullable=True),
    sa.Column('lost', sa.Integer(), nullable=True),
    sa.Column('goals_for', sa.Integer(), nullable=True),
    sa.Column('goals_against', sa.Integer(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('date_add', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spain_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('club_name', sa.String(), nullable=True),
    sa.Column('club_stat_url', sa.String(), nullable=True),
    sa.Column('game', sa.Integer(), nullable=True),
    sa.Column('won', sa.Integer(), nullable=True),
    sa.Column('drawn', sa.Integer(), nullable=True),
    sa.Column('lost', sa.Integer(), nullable=True),
    sa.Column('goals_for', sa.Integer(), nullable=True),
    sa.Column('goals_against', sa.Integer(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('date_add', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spain_table')
    op.drop_table('italy_table')
    op.drop_table('germany_table')
    op.drop_table('france_table')
    op.drop_table('england_table')
    op.drop_table('Users')
    # ### end Alembic commands ###
