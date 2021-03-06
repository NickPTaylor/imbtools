"""Create visit table

Revision ID: 19ee01761281
Revises: b70dc221a2fd
Create Date: 2019-02-24 21:28:22.610097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19ee01761281'
down_revision = 'b70dc221a2fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('visit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imb_member', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('visit_date', sa.Date(), nullable=True),
    sa.Column('visit_start', sa.Time(), nullable=True),
    sa.Column('visit_finish', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['imb_member'], ['imb_member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_visit_created'), 'visit', ['created'], unique=False)
    op.create_index(op.f('ix_visit_visit_date'), 'visit', ['visit_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_visit_visit_date'), table_name='visit')
    op.drop_index(op.f('ix_visit_created'), table_name='visit')
    op.drop_table('visit')
    # ### end Alembic commands ###
