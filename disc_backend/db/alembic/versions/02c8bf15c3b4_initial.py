"""Initial

Revision ID: 02c8bf15c3b4
Revises: 
Create Date: 2022-09-15 02:43:00.003778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02c8bf15c3b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('imports',
    sa.Column('import_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('import_id', name=op.f('pk__imports'))
    )
    op.create_table('relations',
    sa.Column('import_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('parentId', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('import_id', 'id', 'parentId', name=op.f('pk__relations'))
    )
    op.create_table('history',
    sa.Column('import_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('parentId', sa.String(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('updateDate', sa.DateTime(), nullable=False),
    sa.Column('OperationDateTime', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['import_id'], ['imports.import_id'], name=op.f('fk__history__import_id__imports')),
    sa.PrimaryKeyConstraint('import_id', 'id', name=op.f('pk__history'))
    )
    op.create_table('items',
    sa.Column('import_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('parentId', sa.String(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('updateDate', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['import_id'], ['imports.import_id'], name=op.f('fk__items__import_id__imports')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__items'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('history')
    op.drop_table('relations')
    op.drop_table('imports')
    # ### end Alembic commands ###
