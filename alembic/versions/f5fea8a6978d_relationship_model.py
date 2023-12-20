"""Relationship model

Revision ID: f5fea8a6978d
Revises: 99987533da1b
Create Date: 2023-12-19 11:15:42.335857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'f5fea8a6978d'
down_revision: Union[str, None] = '99987533da1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relationships',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('createdAt', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updatedAt', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.String(length=350),
               type_=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('users', 'id',
               existing_type=sa.UUID(),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=False)
    op.alter_column('states', 'countryCode',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('states', 'isoCode',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('identifications', 'id',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=False)
    op.alter_column('cities', 'stateCode',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('cities', 'countryCode',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('cities', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.create_table('decedent_request_documents_draft',
    sa.Column('id', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('request_id', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('document', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('status', mysql.TINYINT(), server_default=sa.text("'1'"), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('size', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('relationships')
    # ### end Alembic commands ###
