"""empty message

Revision ID: 902156d9cffb
Revises: 
Create Date: 2022-06-12 11:44:29.879073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '902156d9cffb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personaje',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('hair_color', sa.String(length=30), nullable=False),
    sa.Column('eyes_color', sa.String(length=30), nullable=False),
    sa.Column('gender', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planeta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=30), nullable=False),
    sa.Column('terrain', sa.String(length=30), nullable=False),
    sa.Column('gravity', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('apellido', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favorito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorito')
    op.drop_table('usuario')
    op.drop_table('planeta')
    op.drop_table('personaje')
    # ### end Alembic commands ###