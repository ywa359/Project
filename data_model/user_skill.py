from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
from pydantic import BaseModel


# SQLAlchemy model
class UserSkill(Base):
    __tablename__ = 'user_skill'
    skill_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    skill_name = Column(String)
    rate = Column(Integer)

    @staticmethod
    def from_json(data):
        user_skill = UserSkillModel(**data)  # use Pydantic model to test data
        return UserSkill(**user_skill.dict())  # trans to SQLAlchemy object


# Pydantic model
class UserSkillModel(BaseModel):
    user_id: int
    skill_name: str
    rate: int
