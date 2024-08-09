import mysql.connector
import configparser
from threading import Lock


class DBManager:
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
                'database': config['mysql']['database']
            }
            self.conn = None
            self._initialized = True

    def connect(self):
        if self.conn is None or not self.conn.is_connected():
            self.conn = mysql.connector.connect(**self.db_config)
        return self.conn

    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
