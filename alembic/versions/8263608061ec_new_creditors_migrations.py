"""new creditors migrations

Revision ID: 8263608061ec
Revises: 6611a3566eb5
Create Date: 2023-12-11 20:20:06.581442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '8263608061ec'
down_revision: Union[str, None] = '6611a3566eb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('decedent_new_creditors_draft')
    op.drop_table('decedent_new_creditors')
    # ### end Alembic commands ###
