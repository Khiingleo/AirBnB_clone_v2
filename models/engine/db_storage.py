#!/usr/bin/python3
""" defines a class DBStorage """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    SQL alchemy database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        initializes Database storage
        """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, passwd, host, db), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        from console import HBNBCommand
        dicts = {}
        for cl in HBNBCommand.classes:
            if cls is None or cls is HBNBCommand.classes[cl] or cls is cl:
                objects =  self.__session.query(HBNBCommand.classes[cl]).all()
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dicts[key] = obj

        return dicts

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        creates tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        closes the session
        """
        self.__session.close()
