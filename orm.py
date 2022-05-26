from sqlalchemy import create_engine
from sqlalchemy.orm import registry, relationship, Session

import database
import domain


def start_mappers():
    """Until these are called, the models are regular python classes, which could help
    with testing. A cleaner approach should probably be sought if applying more than a
    few.
    """
    mapper_registry = registry(database.metadata)

    mapper_registry.map_imperatively(
        domain.User,
        database.user,
        properties={
            'addresses': relationship('Address', backref='user'),
        },
    )

    mapper_registry.map_imperatively(
        domain.Address,
        database.address,
    )


def init_db(url='sqlite://'):
    start_mappers()
    engine = create_engine(url)
    database.metadata.create_all(bind=engine)

    return Session(bind=engine)
