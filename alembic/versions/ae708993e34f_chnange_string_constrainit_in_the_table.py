"""chnange string constrainit in the table

Revision ID: ae708993e34f
Revises: 55786cd0895a
Create Date: 2023-12-13 17:28:46.716518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae708993e34f'
down_revision: Union[str, None] = '55786cd0895a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('cities', 'name', existing_type=sa.String(100), type_=sa.String(250))



def downgrade() -> None:
    pass
