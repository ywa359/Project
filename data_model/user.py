from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    # 数据库中表的名字
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    update_time = Column(TIMESTAMP, server_default=func.now(),
                         onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, user_name={self.user_name})>"
