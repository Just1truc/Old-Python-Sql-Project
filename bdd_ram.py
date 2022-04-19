dixt =[(1,'G Skill Aegis DDR4', 8, 37.16),
(2,'Corsair Vengeance LPX Black DDR4', 8, 40.11),
(2,'Corsair Vengeance LPX Black DDR4', 16, 70.34),
(3,'HyperX Impact DDR4',8 ,41.46 ),
(3,'HyperX Fury DDR4',8,45.69),
(4,'Timetec Hynix DDR4',8 ,32.68)]


liste = [('G Skill'), ('Corsair'), ('HyperX'), ('Timetec')]


import sqlite3
conn = sqlite3.connect('BDD_ram.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS ram_marque(Id_marque_ram INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, NOM_MARQUE TEXT)")

for i in liste:
    cur.execute("INSERT INTO ram_marque(NOM_MARQUE)VALUES (?)",(i,))

cur.execute("PRAGMA foreign_keys = ON")

cur.execute("CREATE TABLE IF NOT EXISTS ram_bars(Id_marque_ram INTEGER NOT NULL, Model TEXT,Go INT,prix FLOAT, FOREIGN KEY(Id_marque_ram) REFERENCES ram_marque(Id_marque_ram))")

for i in dixt:
    cur.execute("INSERT INTO ram_bars(Id_marque_ram, Model, Go, prix)VALUES (?,?,?,?)",i)
conn.commit()
cur.close()
conn.close()