"""rename column

Revision ID: 91b8236deba3
Revises: cc3e4d83e20f
Create Date: 2023-12-20 10:53:10.421956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91b8236deba3'
down_revision: Union[str, None] = 'cc3e4d83e20f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
      op.alter_column('identifications', 'createdAt', new_column_name='created_at', existing_type=sa.TIMESTAMP(timezone=True))
      op.alter_column('identifications', 'updatedAt', new_column_name='updated_at',existing_type=sa.TIMESTAMP(timezone=True))
      op.alter_column('users', 'createdAt', new_column_name='created_at', existing_type=sa.TIMESTAMP(timezone=True))
      op.alter_column('users', 'updatedAt', new_column_name='updated_at', existing_type=sa.TIMESTAMP(timezone=True))
      op.alter_column('relationships', 'createdAt', new_column_name='created_at', existing_type=sa.TIMESTAMP(timezone=True))
      op.alter_column('relationships', 'updatedAt', new_column_name='updated_at', existing_type=sa.TIMESTAMP(timezone=True))





def downgrade() -> None:
    pass
