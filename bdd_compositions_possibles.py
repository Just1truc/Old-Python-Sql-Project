import sqlite3

"""creation de la liste processor"""
    
conn = sqlite3.connect('BDD_processor.db')
cur = conn.cursor()
cur.execute("SELECT processor_marque.NOM_MARQUE,processor.MODEL,processor.generation,processor.prix FROM processor_marque INNER JOIN processor ON processor_marque.Id_marque_processor=processor.Id_marque_processor")
processor = cur.fetchall()

"""gen en 3ème position"""
cur.close()
conn.close()

"""creation de la liste motherboard"""

conn = sqlite3.connect('BDD_motherboard.db')
cur = conn.cursor()
cur.execute("SELECT motherboard_marque.NOM_MARQUE,motherboard.MODEL,motherboard.generation,motherboard.port,motherboard.prix FROM motherboard_marque INNER JOIN motherboard ON motherboard_marque.Id_marque_motherboard=motherboard.Id_marque_motherboard")
motherboard = cur.fetchall()

"""gen en 3 eme position"""
cur.close()
conn.close()

"""creation de la liste graphic_card"""

conn = sqlite3.connect('BDD_graphic_card.db')
cur = conn.cursor()
cur.execute("SELECT graphic_card_marque.NOM_MARQUE,graphic_card.MODEL,graphic_card.port,graphic_card.prix FROM graphic_card_marque INNER JOIN graphic_card ON graphic_card_marque.Id_marque_graphic_card=graphic_card.Id_marque_graphic_card")
graphic_card = cur.fetchall()
"""gen en 3 eme position"""
cur.close()
conn.close()    


"""creation de la liste boitier"""

conn = sqlite3.connect('BDD_boitier.db')
cur = conn.cursor()
cur.execute('SELECT boitier_model,prix FROM boitier')
boitier = cur.fetchall()
cur.close()
conn.close()

"""creation de la liste ram"""

conn = sqlite3.connect('BDD_ram.db')
cur = conn.cursor()
cur.execute("SELECT ram_marque.NOM_MARQUE,ram_bars.Model,ram_bars.prix FROM ram_marque INNER JOIN ram_bars ON ram_marque.Id_marque_ram=ram_bars.Id_marque_ram")
ram_bars = cur.fetchall()
cur.close()
conn.close()
    
"""creation de la liste disque_dur"""

conn = sqlite3.connect('BDD_disque_dur.db')
cur = conn.cursor()
cur.execute("SELECT disque_dur_marque.NOM_MARQUE,disque_dur.capacite_en_To,disque_dur.prix FROM disque_dur_marque INNER JOIN disque_dur ON disque_dur_marque.Id_marque_disque_dur=disque_dur.Id_marque_disque_dur")
disque_dur = cur.fetchall()
cur.close()
conn.close()


""" fonction permettant de créer des compositions pour un prix toujours inférieur à celui énnoncé sans se soucier de détails particuliers et sans barre de ram"""
""""[(carte_mere,carte_graphique,processeur,boitier,disque_dur)]"""
processor_motherboard = []

for i in range(len(motherboard)):
    for j in range(len(processor)):
        if motherboard[i][2] == processor[j][2]:
                processor_motherboard.append(((motherboard[i][0]+motherboard[i][1]),(processor[j][0]+processor[j][1]),(round(motherboard[i][4]+processor[j][3],2))))
              

composition_add_graphic_card = []

for i in range(len(processor_motherboard)):
    for j in range(len(graphic_card)):
        prixe = [processor_motherboard[i][2]+ graphic_card[j][3]]
        tab = [processor_motherboard[i][0],processor_motherboard[i][1]]+[graphic_card[j][0]+graphic_card[j][1]] + prixe
        composition_add_graphic_card.append(tab)

composition_add_disque = []

for i in range(len(composition_add_graphic_card)):
    for j in range(len(disque_dur)):
        prixe = [round(composition_add_graphic_card[i][3] + disque_dur[j][2],2)]
        tab = composition_add_graphic_card[i][0:3] + [disque_dur[j][0],disque_dur[j][1]]+prixe
        composition_add_disque.append(tab)
            

composition_add_boitier = []

for i in range(len(composition_add_disque)):
    for j in range(len(boitier)):
        prixe = [round(composition_add_disque[i][5] + boitier[j][1],2)]
        tab = composition_add_disque[i][0:5] + [boitier[j][0]]+prixe
        composition_add_boitier.append(tab)
        
conn = sqlite3.connect('BDD_compositions_compatibles.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS compositions_compatibles(motherboard TEXT, processor TEXT,graphic_card TEXT,disque TEXT,disque_capacite FLOAT,boitier TEXT,prix FLOAT)") 

for i in composition_add_boitier:
    cur.execute("INSERT INTO compositions_compatibles(motherboard, processor,graphic_card,disque,disque_capacite,boitier,prix)VALUES (?,?,?,?,?,?,?)",i)

conn.commit()
cur.close()
conn.close()


        


