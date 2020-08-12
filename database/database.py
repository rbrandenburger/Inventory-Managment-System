from .item import Item
from .base import Session

class Database:
    
    #Tool to add item to database
    def addItem(self, serial, name, location, amount):
        
        session = Session()
        
        session.add(Item(serial, name, location, amount));
        
        session.commit()
        
        session.close()
        
    #Perform a database query by serial number
    def getBySerial(self, serial_num):
        
        session = Session()
        
        results = session.query(Item).filter_by(serial=serial_num).first()
        
        session.close()
        
        return results
    
    #Change the item amount
    def changeItemAmount(self,serial_num, amount):
        
        session = Session()
        
        session.query(Item).filter_by(serial=serial_num).update({Item.amount : amount})
    
        session.commit()
    
        session.close()
        
    #Returns every item in the database
    def getAllItems(self):
        
        session = Session()
        
        all_items = session.query(Item).all()
        
        session.close()
        
        return all_items
    
    #Deletes an item based on a serial number match
    def deleteItem(self, serial_num):
        
        session = Session()
        
        session.query(Item).filter_by(serial=serial_num).delete()
        
        session.commit()
        
        session.close()
    
    #Perform a database query by item name
    def getByName(self, item_name):
        
        session = Session()
        
        results = session.query(Item).filter(Item.name.contains(item_name)).all()
        
        session.close()
        
        return results
