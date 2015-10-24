"""empty message

Revision ID: 1f64071609af
Revises: 4d29ac5957cd
Create Date: 2015-10-23 23:15:35.748701

"""

# revision identifiers, used by Alembic.
revision = '1f64071609af'
down_revision = '4d29ac5957cd'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('job', 'layer_height',
               type_=mysql.DECIMAL(precision=11, scale=2),
               nullable=False)
    op.alter_column('job', 'temperature',
                    type_=mysql.DECIMAL(precision=11, scale=2),
                    nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('job', 'layer_height',
               type_=mysql.DECIMAL(precision=10, scale=0),
               nullable=False)
    op.alter_column('job', 'temperature',
                    type_=mysql.DECIMAL(precision=10, scale=0),
                    nullable=False)
    ### end Alembic commands ###