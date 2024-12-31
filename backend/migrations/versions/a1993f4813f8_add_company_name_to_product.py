from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1993f4813f8'
down_revision = '6ddb435bfe4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # Create a new table with the updated schema
    op.create_table('new_product',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('description', sa.String(length=200), nullable=True),
        sa.Column('company_name', sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Copy data from the old table to the new table
    op.execute('''
        INSERT INTO new_product (id, name, price, description, company_name)
        SELECT id, name, price, description, company_name FROM product
    ''')
    
    # Drop the old table
    op.drop_table('product')
    
    # Rename the new table to the old table's name
    op.rename_table('new_product', 'product')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # Create the old table
    op.create_table('old_product',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('name', sa.VARCHAR(length=50), nullable=False),
        sa.Column('price', sa.FLOAT(), nullable=False),
        sa.Column('description', sa.VARCHAR(length=200), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Copy data back from the new table to the old table
    op.execute('''
        INSERT INTO old_product (id, name, price, description)
        SELECT id, name, price, description FROM product
    ''')
    
    # Drop the new table
    op.drop_table('product')
    
    # Rename the old table back to the original name
    op.rename_table('old_product', 'product')
    # ### end Alembic commands ###
