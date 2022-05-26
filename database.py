from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(50)),
)

address = Table(
    'address',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('email', String(50)),
)
