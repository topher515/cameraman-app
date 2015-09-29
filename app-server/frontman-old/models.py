
from sqlalchemy import Column, Integer, String, Float, Text, DateTime #, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from flask.ext.login import UserMixin


class User(UserMixin, Base):
    __tablename__ = 'users'

    


# class Location(Base):
#     __tablename__ = 'locations'

#     id = Column(Integer, primary_key=True)
#     latitude = Column(Float)
#     longitude = Column(Float)
#     name = Column(String)
#     status = Column(String)
#     capacity = Column(Integer)
#     spots_taken = Column(Integer)

#     def as_dict(self):
#         d = {c.name: getattr(self, c.name) for c in self.__table__.columns}
#         d["type"] = "location"
#         return d


# class Scooter(Base):
#     __tablename__ = 'scooters'

#     id = Column(Integer, primary_key=True)
#     physical_scoot_id = Column(Integer)
#     estimated_range = Column(Integer)
#     current_location_id = Column(Integer)

#     def as_dict(self):
#         d = {c.name: getattr(self, c.name) for c in self.__table__.columns}
#         d["type"] = "scooter"
#         return d



# class Watcher(Base):
#     __tablename__ = 'watchers'

#     id = Column(Integer, primary_key=True)
#     locations = Column(Text) # JSON!
#     active = Column(Integer, default=1) # 0 or 1

#     locations_as_list = property(lambda self: json.loads(self.locations), 
#                                 lambda self, x: setattr(self,locations,json.dumps(x)))

#     # TODO: Support timeframes

#     def as_dict(self):
#         d = {c.name: getattr(self, c.name) for c in self.__table__.columns}
#         d["locations"] = json.loads(d["locations"])
#         d["type"] = "watcher"
#         return d

