"""decedent request migrations

Revision ID: 73b772416c71
Revises: 8263608061ec
Create Date: 2023-12-11 20:25:45.323644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '73b772416c71'
down_revision: Union[str, None] = '8263608061ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('decedent_request_creditors',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('request_id', sa.String(length=36), nullable=False),
    sa.Column('creditor_id', sa.String(length=36), nullable=False),
    sa.Column('asset_type', sa.String(length=255), nullable=False),
    sa.Column('account_number', mysql.LONGTEXT(), nullable=False),
    sa.Column('meter_read', sa.String(length=255), nullable=True),
    sa.Column('meter_read_date', sa.String(length=255), nullable=True),
    sa.Column('is_approved', mysql.TINYINT(), server_default='0', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('data_id', sa.String(length=255), nullable=True),
    sa.Column('delete_status', sa.BigInteger(), server_default='0', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('decedent_request_creditors_draft',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('request_id', sa.String(length=36), nullable=False),
    sa.Column('creditor_id', sa.String(length=36), nullable=False),
    sa.Column('asset_type', sa.String(length=255), nullable=False),
    sa.Column('account_number', mysql.LONGTEXT(), nullable=False),
    sa.Column('meter_read', sa.String(length=255), nullable=True),
    sa.Column('meter_read_date', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('data_id', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('decedent_request_documents_draft',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('request_id', sa.String(length=36), nullable=False),
    sa.Column('document', sa.String(length=255), nullable=False),
    sa.Column('status', mysql.TINYINT(), server_default='1', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('size', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('decedent_request_documents_draft')
    op.drop_table('decedent_request_creditors_draft')
    op.drop_table('decedent_request_creditors')
    # ### end Alembic commands ###
