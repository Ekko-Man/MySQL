"""update_Bar_Table

Revision ID: 448cc85edd43
Revises: 34f2334e9939
Create Date: 2019-04-02 13:01:52.820549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '448cc85edd43'
down_revision = '34f2334e9939'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mainbar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=80), nullable=True),
    sa.Column('url', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('title',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=80), nullable=True),
    sa.Column('url', sa.String(length=140), nullable=True),
    sa.Column('MainID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['MainID'], ['mainbar.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('title')
    op.drop_table('mainbar')
    # ### end Alembic commands ###
