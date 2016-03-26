"""empty message

Revision ID: 07e8c7892096
Revises: 941edf57fc25
Create Date: 2016-03-26 16:45:58.993329

"""

# revision identifiers, used by Alembic.
revision = '07e8c7892096'
down_revision = '941edf57fc25'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('myprofile',
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('userid'),
    sa.UniqueConstraint('email')
    )
    op.create_table('mywish',
    sa.Column('wishid', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('description_url', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['myprofile.userid'], ),
    sa.PrimaryKeyConstraint('wishid')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mywish')
    op.drop_table('myprofile')
    ### end Alembic commands ###