from .item import Item
from .base import Session


class utilities:
    
    def FillTable():
        
        #Create a session
        session = Session()
        
        #Create some items
        session.add_all([
            Item("2007522", "1\" Nails - Box of 20", "A-325","199"),
            Item("2434484", "16oz Steel Hammer", "C-165","18"),
            Item("2376424", "12\" Hand Saw", "C-147", "10")]
        )
        
        #Commit item addition
        session.commit()
        
        #Close session
        session.close()
