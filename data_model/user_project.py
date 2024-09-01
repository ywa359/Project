from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
from pydantic import BaseModel


# SQLAlchemy模型
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
        user_project = UserProjectModel(**data)  # 使用 Pydantic 模型验证数据
        return UserProject(**user_project.dict())  # 转换为 SQLAlchemy 对象


# Pydantic模型
class UserProjectModel(BaseModel):
    user_id: int
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    git_link: str
    online_service: str
    skills: str
