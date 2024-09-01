from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
from pydantic import BaseModel


# SQLAlchemy model
class UserProject(Base):
    __tablename__ = 'user_project'
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    git_link = Column(String)
    online_service = Column(String)
    skills = Column(String)

    @staticmethod
    def from_json(data):
        user_project = UserProjectModel(**data)  # use Pydantic model to test data
        return UserProject(**user_project.dict())  # trans to SQLAlchemy object



# Pydantic model
class UserProjectModel(BaseModel):
    user_id: int
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    git_link: str
    online_service: str
    skills: str
