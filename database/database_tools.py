from .item import Item
from .base import Session

class db_tool:
    
    def deleteAll(self):
        
        session = Session()
        session.query(Item).delete()
        
        session.commit()
        
        session.close()
    
    def addItems(self):
        
        session = Session()
        
        session.add_all([ Item("2376424","12\" Hand Saw", "C-134", "8"),
                          Item("2434484","16oz Steel Hammer", "C-157", "27"),
                          Item("2295457","2\" Nail - 1lb Box", "A-405", "47"),
                          Item("2295525","1.5\" Nail - 5lb Box", "A-318", "33"),
                          Item("2413222","Cordless Hammer Drill","D-222","4"),
                          Item("2741022","5/8\"x100' Vinyl Garden Hose", "G-307", "20"),
                          Item("1792914","8x16\" Riverfront Paver", "G-189","500"),
                          Item("5508330","Interior Latex Paint + Primer","B-547", "46"),
                          Item("5611712","1\" Paint Brush","B-311","14"),
                          Item("5612371","12\" Heavy-Duty Paint Roller Frame","B-315","8"),
                          Item("5610292","12\" Paint Roller Cover - Polyester", "B-215", "39"),
                          Item("6482910","5-Gallon Bucket", "A-179", "85"),
                          Item("3700116","40' Extension Cord", "B-289", "20"),
                          Item("2512218", "Elmer's Wood Glue - 8oz", "B-665", "43"),
                          Item("3633840", "15-amp GFCI Outlet", "E-438", "2"),
                          Item("3645008", "8\" Wire Stripper/Crimper", "E-156","7"),
                          Item("3632475", "15-amp Single Pole Toggle Switch - Tan", "E-329", "12")
                          ])
        
        session.commit()
        
        session.close()

if __name__ == '__main__':
	db = db_tool()
	db.deleteAll()
	db.addItems()
