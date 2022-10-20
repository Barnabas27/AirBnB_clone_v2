#!/usr/bin/python3
"""DB storage"""

from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """DB Storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """init for DBStorage"""
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(username,
                                              password,
                                              host,
                                              db_name),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all objects"""
        _obj = {}
        if cls is None:
            _objects = []
            classes = ['User', 'State', 'City', 'Place', 'Review', 'Amenity']
            for _class in classes:
                results = self.__session.query(eval(_class))
                for result in results:
                    _objects.append(result)
        else:
            _objects = self.__session.query(cls).all()
        for obj in _objects:
            key = type(obj).__name__ + "." + str(obj.id)
            _obj[key] = obj
        return _obj

    def new(self, obj):
        """Add object"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete if none"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """call close"""
        self.__session.close()

    def reset(self):
        """Reset"""
        self.__session.close()
        Base.metadata.drop_all(self.__engine)
        self.reload()