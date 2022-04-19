processor__generation_list = [(1, '2 AMD'), (2, '3 AMD'), (3, '5 AMD'), (4, '7 AMD'), (5, '4 Intel'), (6, '5 Intel'), (7, '8 Intel'), (8, '9 Intel'), (9, '10 Intel'), (10, 'Serie 3000')]
import sqlite3
conn = sqlite3.connect('BDD_processor_generations.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS processor_generations(Id_generation INT PRIMARY KEY, NOM_GENERATION TEXT)")
for i in processor__generation_list:
    cur.execute("INSERT INTO processor_generations(Id_generation,NOM_GENERATION)VALUES (?,?)",i)
conn.commit()
cur.close()
conn.close()