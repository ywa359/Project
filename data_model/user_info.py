from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserInfo(Base):
    __tablename__ = 'user_info'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    gender = Column(Enum('Male', 'Female', 'Other'), nullable=False)
    email_address = Column(String(255), nullable=False)
    student_id = Column(String(100), nullable=False)
    github = Column(String(255), nullable=True)
    gitlab = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<UserInfo(user_id={self.user_id}, name={self.name}, gender={self.gender}, email_address={self.email_address})>"
