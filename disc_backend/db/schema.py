from sqlalchemy import MetaData
from sqlalchemy.sql import func

from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer, String, Table
)


convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),

    # Именование индексов
    'ix': 'ix__%(table_name)s__%(all_column_names)s',

    # Именование уникальных индексов
    'uq': 'uq__%(table_name)s__%(all_column_names)s',

    # Именование CHECK-constraint-ов
    'ck': 'ck__%(table_name)s__%(constraint_name)s',

    # Именование внешних ключей
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',

    # Именование первичных ключей
    'pk': 'pk__%(table_name)s'
}
metadata = MetaData(naming_convention=convention)


imports_table = Table(
    'imports',
    metadata,
    Column('import_id', Integer, primary_key=True)
)

items_table = Table(
    'items',
    metadata,
    Column('import_id', Integer, ForeignKey('imports.import_id')),
    Column('id', String, primary_key=True),
    Column('url', String, nullable=True),
    Column('parentId', String, nullable=True),
    Column('size', Integer, nullable=True),
    Column('type', String, nullable=False),
    Column('updateDate', DateTime, nullable=False)
)

# relations_table = Table(
#     'relations',
#     metadata,
#     Column('import_id', Integer, primary_key=True),
#     Column('id', String, primary_key=True),
#     Column('parentId', String, primary_key=True)
# )

history_table = Table(
    'history',
    metadata,
    Column('import_id', Integer, ForeignKey('imports.import_id'), primary_key=True),
    Column('id', String, primary_key=True),
    Column('url', String, nullable=True),
    Column('parentId', String, nullable=True),
    Column('size', Integer, nullable=True),
    Column('type', String, nullable=False),
    Column('updateDate', DateTime, nullable=False),
    Column('OperationDateTime', DateTime, server_default=func.now())
)
