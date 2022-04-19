#####Exercice 1

dixt = [(1,'7 3700X',2,'3 AMD',8,'3.6 GHz','7nm',65,374.95),
        (1,'7 2700X Wraith Prism Cooler',1,'2 AMD',8,'3.7 GHz','12nm',105,239.95),
        (2,'i5 10400F',9,'10 Intel',6,'2.9 GHz','14 nm',65,179.95),
        (2, 'i7 10700KF',9,'10 Intel', 8, '3.8 GHz', '14 nm',125, 429.95),
        (1, '5 3400G',2,'3 AMD', 4, '3.7 GHz', '12 nm',65, 179.95),
        (1, '3 3100',2,'3 AMD', 4, '3.6 GHz', '7 nm',65, 124.96),
        (2, 'i5 9600KF',8,'9 Intel', 6, '3.7 GHz', '14 nm',95, 234.95),
        (2, 'i7 9700F',8,'9 Intel', 8, '3 GHz', '14 nm',65, 329.95),
        (2, 'i3 10100F',9,'10 Intel', 4, '3.6 GHz', '14 nm',65, 99.95),
        (2, 'i9 9900KF',8,'9 Intel', 8, '3.6 GHz', '14 nm',95, 469.96),
        (2, 'i7 9700KF',8,'9 Intel', 8, '3.6 GHz', '14 nm',95, 369.95),
        (2, 'i9 10850K',9,'10 Intel', 10, '3.6 GHz', '14 nm',125, 559.94),
        (1, '7 5800X',3,'5 AMD', 8, '3.8 GHz', '7 nm',105, 589.96),
        (1, '5 3500X',2,'3 AMD', 6, '3.6 GHz', '7 nm',65, 189.95),
        (2, 'i5 9400',8,'9 Intel', 6, '2.9 GHz', '14 nm',65, 189.95),
        (2, 'i9 10900F',9,'10 Intel', 10, '2.8 GHz', '14 nm',65, 499.96),
        (3, 'G5905',6,'5 Intel', 2, '3.5 GHz', '14 nm',58, 45.95),
        (2, 'i5 9400F',8,'9 Intel', 6, '2.9 GHz', '14 nm',65, 173.95),
        (1, '5 3600X',2,'3 AMD', 6, '3.8 GHz', '7 nm',95, 289.96),
        (1, '5 3600',2,'3 AMD', 6, '3.6 GHz', '7 nm',65, 245.95),
        (2, 'i9 10940X',9,'10 Intel', 14, '3.3 GHz', '14 nm',165, 979.94),
        (3, 'G4930',5,'4 Intel', 2, '3.2 GHz', '14 nm',54, 45.95),
        (1, '3 3300X',2,'3 AMD', 4, '3.8 GHz', '14 nm',65, 149.95),
        (1, 'Threadripper 3970X',2,'3 AMD', 32, '3.7 GHz', '7',280, 2239.94),
        (1, '9 3900X',2,'3 AMD', 12, '3.8 GHz', '7 nm',105, 559.96),
        (1, '9 5950X',3,'5 AMD', 16, '3.4 GHz', '7 nm',105, 979.94),
        (2, 'i3 8300',7,'8 Intel', 4, '3.7 GHz', '14 nm',62, 179.95),
        (1, '3 3200G',2,'3 AMD', 4, '3.6 GHz', '12 nm',65, 139.95),
        (4, '3000G',10,'Serie 3000', 2, '3.5 GHz', '14 nm',65, 61.94),
        (5, 'G5420',6,'5 Intel', 2, '3.8 GHz', '14 nm',54, 69.95),
        (2, 'i9 10980XE Extreme Edition',9,'10 Intel', 18, '3 GHz', '14 nm',165, 1229.95),
        (6, '9700',4,'7 AMD' , 4, '3.5 GHz', '28 nm',65, 71.95),
        (1, 'Threadripper 3990X',2,'3 AMD', 64, '2.9 GHz', '7 nm',280, 4725.95)]


processor_list = [('AMD Ryzen'), ('Intel Core'), ('Intel Celeron'), ('AMD Athlon'), ('Intel Pentium'),('AMD A10')]

import sqlite3
conn = sqlite3.connect('BDD_processor.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS processor_marque(Id_marque_processor INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, NOM_MARQUE TEXT)")

for i in processor_list:
    cur.execute("INSERT INTO processor_marque(NOM_MARQUE)VALUES (?)",(i,))

cur.execute("PRAGMA foreign_keys = ON")

cur.execute("CREATE TABLE IF NOT EXISTS processor(Id_marque_processor INTEGER NOT NULL, MODEL TEXT, Id_generation INT REFERENCES processor_generations(Id_generation), generation TEXT, Coeurs INT, fréquence TEXT,taille_de_gravure INT,puissanceEnWatt INT, prix FLOAT,FOREIGN KEY(Id_marque_processor) REFERENCES processor_marque(Id_marque_processor))")


for i in dixt:
    cur.execute("INSERT INTO PROCESSOR(Id_marque_processor,MODEL,Id_generation,generation,Coeurs,fréquence,taille_de_gravure,puissanceEnWatt,prix)VALUES (?,?,?,?,?,?,?,?,?)",i)
conn.commit()
cur.close()
conn.close()
""" A la deuxième execution, python nous préviens que la tale éxiste déja, pour régler le problème, i; faut ajouter un IF NOT EXISTS"""

