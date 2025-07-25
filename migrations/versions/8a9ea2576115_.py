"""empty message

Revision ID: 8a9ea2576115
Revises: 4f5b307a556f
Create Date: 2025-07-07 10:18:03.020348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a9ea2576115'
down_revision = '4f5b307a556f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'post', ['post_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
