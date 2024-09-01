from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
from pydantic import BaseModel


# SQLAlchemy模型
class UserSkill(Base):
    __tablename__ = 'user_skill'
    skill_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    skill_name = Column(String)
    rate = Column(Integer)

    @staticmethod
    def from_json(data):
        user_skill = UserSkillModel(**data)  # 使用 Pydantic 模型验证数据
        return UserSkill(**user_skill.dict())  # 转换为 SQLAlchemy 对象


# Pydantic模型
class UserSkillModel(BaseModel):
    user_id: int
    skill_name: str
    rate: int
