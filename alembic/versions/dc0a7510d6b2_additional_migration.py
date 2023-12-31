"""additional migration

Revision ID: dc0a7510d6b2
Revises: 9fb06a4c1792
Create Date: 2023-12-11 19:57:59.070472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'dc0a7510d6b2'
down_revision: Union[str, None] = '9fb06a4c1792'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('creditor_property_utility_draft')
    op.drop_table('creditor_property_utility')
    # ### end Alembic commands ###
