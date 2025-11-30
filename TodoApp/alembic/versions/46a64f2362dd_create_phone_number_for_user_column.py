"""Create Phone Number for user column

Revision ID: 46a64f2362dd
Revises: 
Create Date: 2025-11-30 21:19:57.255787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46a64f2362dd'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    pass
