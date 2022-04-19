dixt =[(1, 'TUF Z390-PLUS GAMING', 'LGA1151 V2', '9 Intel','PCI-Express 16x',139.96),
(2, 'MPG B550 GAMING PLUS', 'Socket AM4', '3 AMD','PCI-Express 16x',165.95),
(2, 'MAG B550 TOMAHAWK', 'Socket AM4', '3 AMD','PCI-Express 16x',209.95),
(3, 'B450 AORUS M', 'AM4', '3 AMD','PCI-Express 16x',99.95),
(3, 'B550 Aorus Elite V2', 'AM4', '3 AMD','PCI-Express 16x',159.95),
(1, 'ROG STRIX B450-F GAMING', 'AM4', 'Serie 3000','PCI-Express 16x',149.95),
(1, 'TUF GAMING Z490-PLUS', 'LGA1200', '10 Intel','PCI-Express 16x',204.95),
(3, 'GA-H110M-S2H', '1151', '7 Intel','PCI-Express 16x',62.95),
(2, 'B450 TOMAHAWK MAX', 'AM4', 'AMD','PCI-Express 16x',134.95),
(2, 'MPG Z390 GAMING PLUS', 'LGA1151', '9 Intel','PCI-Express 16x',164.95),
(1, 'TUF GAMING B460M-PLUS', 'LGA1200', '10 Intel','PCI-Express 16x',124.96),
(1, 'PRIME Z390-P', 'LGA1151 V2', '9 Intel','PCI-Express 16x',162.94),
(2, 'B450M PRO-M2 MAX', 'AM4', 'AMD','PCI-Express 16x',78.95),
(2, 'MPG Z490 UNIFY', 'LGA1200', '10 Intel','PCI-Express 16x',345.95),
(3, 'Z490 M', 'LGA1200', '10 Intel','PCI-Express 16x',144.95),
(3, 'H310M H 2.0', '1151', '8 Intel','PCI-Express 16x',72.95),
(2, 'B550M PRO-VDH WIFI', 'AM4', '3 AMD','PCI-Express 16x',124.96),
(3, 'A520M S2H', 'AM4', '3 AMD','PCI-Express 16x',74.95),
(1, 'ROG Crosshair VIII Hero WIFI', 'AM4', '3 AMD','PCI-Express 16x',515.95),
(1, 'PRIME Z490-P', 'LGA1200', '10 Intel','PCI-Express 16x',99.95)]

motherboard_list = [('ASUS'), ('MSI'), ('Gigabyte')]

import sqlite3
conn = sqlite3.connect('BDD_motherboard.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS motherboard_marque(Id_marque_motherboard INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, NOM_MARQUE TEXT)")

for i in motherboard_list:
    cur.execute("INSERT INTO motherboard_marque(NOM_MARQUE)VALUES (?)",(i,))

cur.execute("PRAGMA foreign_keys = ON")

cur.execute("CREATE TABLE IF NOT EXISTS motherboard(Id_marque_motherboard INTEGER NOT NULL, MODEL TEXT,Socket TEXT,generation TEXT,port TEXT, prix FLOAT, FOREIGN KEY(Id_marque_motherboard) REFERENCES motherboard_marque(Id_marque_motherboard))")

for i in dixt:
    cur.execute("INSERT INTO motherboard(Id_marque_motherboard,MODEL,Socket,generation,port,prix)VALUES (?,?,?,?,?,?)",i)
conn.commit()
cur.close()
conn.close()
