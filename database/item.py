from sqlalchemy import Column, Integer, String, Float, Table
from .base import Base
from sqlalchemy.orm import relationship

#Represents the table in the database.  Can add/delete/update rows with this
class Item(Base):
    __tablename__ = 'tblItems'
    ID = Column('itemID', Integer, nullable=False, primary_key=True, autoincrement=True)
    serial = Column('itemSerial', String(255))
    name = Column('itemName', String(255))
    location = Column('itemLocation', String(255))
    amount = Column('itemAmount', Integer)

    def __init__(self, itemSerial, itemName, itemLocation, itemAmount):
        self.serial = itemSerial
        self.name = itemName
        self.location = itemLocation
        self.amount = itemAmount
