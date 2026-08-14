from sqlalchemy import Column, Integer, String
from .database import Base


class MasterCategory(Base):

    __tablename__ = "MasterCategory"

    MasterCategoryId = Column(
        Integer,
        primary_key=True,
        index=True
    )

    MasterCategoryName = Column(
        String(100),
        nullable=False
    )