CREATE DATABASE IF NOT EXISTS remipzuw_inventory;
USE remipzuw_inventory;
CREATE TABLE IF NOT EXISTS tblItems(
itemID INT NOT NULL AUTO_INCREMENT,
itemSerial VARCHAR(255),
itemName VARCHAR(255),
itemLocation VARCHAR(255),
itemAmount INT,
PRIMARY KEY(itemID)
);
