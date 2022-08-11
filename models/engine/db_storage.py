from models.models_base import Base
from os import getenv
from mysqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity


MySQL_user = getenv("HBNB_MYSQL_USER")
MySQL_password = getenv("HBNB_MYSQL_PWD")
MySQL_host = getenv("HBNB_MYSQL_HOST")
MySQL_database = getenv("HBNB_MYSQL_DB")


class DBStorage:
    """new engine"""
    __engine = None
    __session = None

    def __init__(self):
        """instance"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}.{}@{}.{}".format(MySQL_user, MySQL_password,
                                                 MySQL_host, MySQL_database,
                                                 pool_pre_ping=True))

    if getenv(HBNB_ENV == "test"):
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current db"""
        o_d = []

        if cls is None:
            objects = self.__session.query(User, State, Review,
                                   City, Amenity, Place).all()

            for obj in objects:
                obj_name = obj.__class__.__name__
                obj_id = obj.id

                key = obj_name + "." + obj_id
                o_d[key] = obj
        else:
            objects = self.__session.query(cls).all()

            for obj in objects:
                obj_name = objects.__class__.__name__
                obj_id = obj.id

            key = obj_name + "." + obj_id

            o_d[key] = obj

        return o_d

    def new(self, obj):
        """add theobj to the current db"""
        self.__session.add(obj)

    def save(self):
        """commit all changes in current db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current db"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables"""
        Base.metadata.create_all(sef.__engine)

        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))

        self.__session = Session()
