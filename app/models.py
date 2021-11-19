from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger, BigInteger
from sqlalchemy.orm import mapper
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(BigInteger, primary_key=True, nullable=False)
    title = Column(String(128), nullable=False)
    content = Column(String(1024), nullable=False)
    published = Column(SmallInteger, server_default="1", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    #ondelte是处理外键策略
    # owner_id = Column(BigInteger, ForeignKey(
    #     "users.id", ondelete="CASCADE"), nullable=False)
    owner_id = Column(BigInteger, nullable=False)

    # owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(BigInteger, primary_key=True)
    post_id = Column(BigInteger, primary_key=True)