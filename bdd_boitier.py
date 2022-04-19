liste = [('Fractal Design Focus G Black Window', 'noir', 'non','ATX/EPS', 69.95),
('Zalman T6', 'noir', 'non','ATX/EPS', 37.94),
('Antec NX300', 'noir', 'oui','ATX/EPS', 68.95),
('Fractal Design Meshify S2 Black - Dark TG', 'noir', 'non','ATX/EPS', 199.94),
('IN WIN 309', 'noir', 'oui','ATX/EPS', 249.95),
('Kolink Inspire K1 RGB', 'Noir,verre trempé', 'oui','ATX/EPS', 69.99),
('Be Quiet Pure Base 600 Window Orange', 'noir', 'non','ATX/EPS', 112.96),
('Thermaltake S300 TG- Blanc', 'blanc', 'non','ATX/EPS', 109.94)]


import sqlite3
conn = sqlite3.connect('BDD_boitier.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS boitier(boitier_model,couleur TEXT,rgb TEXT,alimentation TEXT,prix FLOAT)")
for i in liste:
    cur.execute("INSERT INTO boitier(boitier_model,couleur,rgb,alimentation,prix)VALUES (?,?,?,?,?)",i)
conn.commit()
cur.close()
conn.close()