

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.exc import NoResultFound
from models import Location, Scooter, Watcher
from os import environ


# Database Stuff
engine = create_engine("postgresql://postgres@db_1:5432", echo=True)
make_session = sessionmaker(bind=engine)



def check_availability():


    sesh = make_session()

    for watcher in sesh.query(Watcher).filter_by(active=1).all():


