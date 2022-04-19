dixt = [(1, 'GeForce RTX 3070 GAMING OC', 8, 14.0, 'PCI-Express 16x', 689.95),
(2, 'Radeon RX 5600 XT Pulse', 6, 14.0, 'PCI-Express 16x', 369.95),
(3, 'GeForce RTX 3070 Gaming X TRIO', 8, 14.0, 'PCI-Express 16x', 779.95),
(4, 'GeForce RTX 3070 Twin Edge OC', 8, 14.0, 'PCI-Express 16x', 629.95),
(5, 'GeForce RTX 3080 FTW3 ULTRA GAMING', 10, 19.0, 'PCI-Express 16x', 999.95),
(3, 'GeForce RTX 3080 Gaming X TRIO', 10, 19.0, 'PCI-Express 16x', 949.96),
(6, 'GeForce RTX 3080 TUF OC', 10, 19.0, 'PCI-Express 16x', 939.95),
(6, 'GeForce GT 710', 2, 5.012, 'PCI-Express 16x', 74.95),
(1, 'GeForce GTX 1650 D6 WINDFORCE OC', 4, 12.0, 'PCI-Express 16x', 184.96),
(1, 'GeForce GTX 1660 Ti OC', 6, 12.0, 'PCI-Express 16x', 319.96),
(1, 'Radeon RX 5500 XT OC', 8, 14.0, 'PCI-Express 16x', 229.96),
(3, 'GeForce RTX 3090 Gaming X TRIO', 24, 19.5, 'PCI-Express 16x', 1849.94),
(7, 'Radeon RX 6800', 16, 16.0, 'PCI-Express 16x', 719.95),
(5, 'GeForce GTX 1650 KO Ultra GDDR6 GAMING', 4, 12.0, 'PCI-Express 16x', 189.95)]

liste=[('Gigabyte'), ('Sapphire'), ('MSI'), ('Zotac'), ('EVGA'), ('ASUS'), ('ASRock')]




import sqlite3
conn = sqlite3.connect('BDD_graphic_card.db')
cur = conn.cursor()



cur.execute("CREATE TABLE IF NOT EXISTS graphic_card_marque(Id_marque_graphic_card INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, NOM_MARQUE TEXT)")

for i in liste:

    cur.execute("INSERT INTO graphic_card_marque(NOM_MARQUE)VALUES (?)",(i,))


cur.execute("PRAGMA foreign_keys = ON")

cur.execute("CREATE TABLE IF NOT EXISTS graphic_card(Id_marque_graphic_card INTEGER NOT NULL, MODEL TEXT,ram INT,frequence_mémoire FLOAT,port TEXT, prix FLOAT, FOREIGN KEY(Id_marque_graphic_card) REFERENCES graphic_card_marque(Id_marque_graphic_card))")

for i in dixt:
    cur.execute("INSERT INTO graphic_card(Id_marque_graphic_card,MODEL,ram,frequence_mémoire,port, prix)VALUES (?,?,?,?,?,?)",i)
conn.commit()
cur.close()
conn.close()
