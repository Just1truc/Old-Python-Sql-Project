dixt =[(1, 2.0, 256,7200, 69.95),
       (1, 1.0, 64,7200, 51.95),
       (1, 4.0, 256,5400, 122.95),
       (2, 1.0, 64,7200, 49.95),
       (3, 2.0, 64,7200, 74.95),
       (2, 2.0, 256,5400, 74.95),
       (2, 8.0, 256,7200, 269.95),
       (1, 8.0, 256,5400, 219.95)]

listE = [("Seagate BarraCuda"),
("Western Digital"),
("Toshiba")]

import sqlite3

conn = sqlite3.connect('BDD_disque_dur.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS disque_dur_marque(Id_marque_disque_dur INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, NOM_MARQUE TEXT)")

for i in listE:
    cur.execute("INSERT INTO disque_dur_marque(NOM_MARQUE) VALUES (?)",(i,))

cur.execute("PRAGMA foreign_keys = ON")

cur.execute("CREATE TABLE IF NOT EXISTS disque_dur(id_marque_disque_dur INTEGER NOT NULL,capacite_en_To FLOAT ,cache_en_Mo INT,tour_minute INT,prix FLOAT,FOREIGN KEY(Id_marque_disque_dur) REFERENCES disque_dur_marque(Id_marque_disque_dur))")
cur = conn.cursor()

for i in dixt:
    cur.execute("INSERT INTO disque_dur(id_marque_disque_dur,capacite_en_To,cache_en_Mo,tour_minute,prix)VALUES (?,?,?,?,?)",i)
conn.commit()
cur.close()
conn.close()



