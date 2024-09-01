import configparser
from threading import Lock

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class DBSession:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            config = configparser.ConfigParser()
            config.read('config.ini')
            self.db_config = {
                'host': config['mysql']['host'],
                'user': config['mysql']['user'],
                'password': config['mysql']['password'],
                'database': config['mysql']['database'],
                'ssl_disabled': config['mysql']['ssl_disabled']
            }
            self._initialized = True
            engine = create_engine(
                'mysql+mysqlconnector://{}:{}@{}/{}'.format(
                    self.db_config['user'], self.db_config['password'],
                    self.db_config['host'], self.db_config['database'],
                ),
                pool_recycle=3600)
            Base.metadata.create_all(engine)
            self.session = scoped_session(
                sessionmaker(autocommit=False, autoflush=False, bind=engine))


db_session = DBSession().session
