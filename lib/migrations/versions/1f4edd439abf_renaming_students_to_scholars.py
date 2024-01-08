"""Renaming students to scholars

Revision ID: 1f4edd439abf
Revises: 60214e54f184
Create Date: 2024-01-08 17:47:56.448364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f4edd439abf'
down_revision = '60214e54f184'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')