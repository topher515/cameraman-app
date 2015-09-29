import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.exc import NoResultFound
from models import Location, Scooter
from os import environ


# Database Stuff
engine = create_engine("postgresql://postgres@db_1:5432", echo=True)
make_session = sessionmaker(bind=engine)



def refresh_locations():
    
    sesh = make_session()

    loc_attributes = ('name','latitude','longitude','status', 'spots_taken', 'capacity');
    response = requests.get("https://app.scootnetworks.com/api/v2/locations.json")

    for loc_data in response.json()['locations']:
        try:
            loc = sesh.query(Location).filter(Location.id==loc_data["id"]).one()
        except NoResultFound, e:
            loc = Location(id=loc_data["id"])
        for attrib in loc_attributes:
            setattr(loc, attrib, loc_data[attrib])
        sesh.add(loc)

    sesh.commit()



def refresh_scooters():
    
    sesh = make_session()

    scoot_attributes = ('physical_scoot_id','estimated_range','current_location_id')
    response = requests.get("https://app.scootnetworks.com/api/v1/scooters.json")

    for scoot_data in response.json()['scooters']:
        try:
            scoot = sesh.query(Scooter).filter(Scooter.id==scoot_data["id"]).one();
        except NoResultFound, e:
            scoot = Scooter(id=scoot_data["id"])
        for attrib in scoot_attributes:
            setattr(scoot, attrib, scoot_data[attrib])
        sesh.add(scoot)

    sesh.commit()

refresh_locations()
refresh_scooters()
    