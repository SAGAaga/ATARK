from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Boolean
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

class IoT(Base):
    __tablename__ = 'iot'
    iot_id = Column(Integer, primary_key=True)
    phone_number = Column(Text, nullable=False)
    is_working = Column(Boolean, nullable=False, default=False)
