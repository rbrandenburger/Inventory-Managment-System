from .item import Item
from .base import Session

class Database:
    
    def addItem(self, serial, name, location, amount):
        
        session = Session()
        
        session.add(Item(serial, name, location, amount));
        
        session.commit()
        
        session.close()
    
    def getBySerial(self, serial_num):
        
        session = Session()
        
        results =session.query(Item).filter_by(serial=serial_num).first()
        
        session.close()
        
        return results
        
    def changeItemAmount(self,serial_num, how_much):
        
        session = Session()
        
        session.query(Item).filter_by(serial=serial_num).update({Item.amount : Item.amount + how_much})
        
        session.commit()
        
        session.close()
        
    def getAllItems(self):
        
        session = Session()
        
        all_items = session.query(Item).all()
        
        session.close()
        
        return all_items
        
    def deleteItem(self, serial_num):
        
        session = Session()
        
        session.query(Item).filter_by(serial=serial_num).delete()
        
        session.commit()
        
        session.close()

    def getByName(self, item_name):
        
        session = Session()
        
        results = session.query(Item).filter(Item.name.contains(item_name)).all()
        
        session.close()
        
        return results
