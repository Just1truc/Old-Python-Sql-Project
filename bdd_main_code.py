from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
###### Initialisation des variables

entree = 0
""" Variable qui permet de récupérer l'entrée d'un utilisateur lorsque celui-ci fait un recherche par mots clés"""
all_texte = []
all_find = []

###### Fonctions :



###### Classes


class texte:
    all_texte =[]
    def __init__(self,texte_label):
        self.texte_label = texte_label
        self.all_textes = self.texte_ajoute()
        
    def texte_ajoute(self):
        all_texte.append(self)
        
""" S'affiche avec la commande all_texte[len(tab)].texte_label"""


class find:
    all_find = []
    def __init__(self,find_label):
        self.find_label = find_label
        self.all_finds = self.find_ajoute()
        
    def find_ajoute(self):
        all_find.append(self)

"""Utilisée pour les noms de colonne, cette classe enregistre les finds_label pour permettre leur supression plus tard"""





##--Recherche--##
def recherche():
    """
    Fonction affiliée au bouton recherche qui permet de choisir son mode de recherche
    Deux possibilités :
    --Par mot clés
    --Par catégorie
    Il y a 6 catégories différentes et 6 boutons en lien.
    """
    
    
    bouton_categorie.destroy()
    bouton_creer_composition.destroy()
    
    """Text : 'par catégorie'"""
    
    Texte = Label(fenetre, text = 'Par catégorie :')
    Texte.grid(row = 0, column = 0)
    
    """--- Bouton Par catégories ---"""
    
    """Carte Mères :"""
    bouton_carte_meres = Button(fenetre, text ="Carte mère",width=20,command=carte_mere_bdd)
    bouton_carte_meres.grid(row = 1,column = 0,padx=3, pady=3)
    """Processeur/ CPU"""
    bouton_processeur = Button(fenetre, text = "Processeur",width = 20, command = processeur)
    bouton_processeur.grid(row = 1,column = 1, padx=3, pady=3)
    """Carte Graphique"""
    bouton_carte_graphique = Button(fenetre, text = "Carte Graphique",width = 20, command = carte_graphique)
    bouton_carte_graphique.grid(row = 1,column = 2, padx=3, pady=3)
    """Disque_dur"""
    bouton_disque_dur = Button(fenetre, text = "Disque Dur",width = 20, command = disque_dur)
    bouton_disque_dur.grid(row = 1, column = 3, padx=3, pady=3)
    """Boitier"""
    bouton_boitier = Button(fenetre, text = "Boitier",width = 20, command = boitier)
    bouton_boitier.grid(row = 1,column = 4, padx=3, pady=3)
    """Barre de ram"""
    bouton_ram = Button(fenetre,text = "Barres de ram",width = 20,command = ram_bar_bdd)
    bouton_ram.grid(row = 1,column = 5, padx=3, pady=3)
    
    
    
    
def carte_graphique():
    """Fonction affiche toute les cartes mères présentes dans la bdd ainsi que les informations qui y sont affiliées"""
    
    """--Suppresions des possibles labels deja existants--"""
    if all_texte != []:
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
    if all_find != []:
        for i in range(len(all_find)):
            all_find[i].find_label.destroy()
    
    
    conn = sqlite3.connect('BDD_graphic_card.db')
    cur = conn.cursor()
    cur.execute("SELECT graphic_card_marque.NOM_MARQUE,graphic_card.MODEL,graphic_card.ram,graphic_card.frequence_mémoire,graphic_card.port,graphic_card.prix FROM graphic_card_marque INNER JOIN graphic_card ON graphic_card_marque.Id_marque_graphic_card=graphic_card.Id_marque_graphic_card ORDER BY prix ASC")
    resultat = cur.fetchall()
    """Affichage des résultats"""
    finds = Label(fenetre,text = "Marque")
    finds.grid(row = 4,column =0)
    finds.config(bg = 'black',fg = 'white')
    find(finds)  
    
    finds = Label(fenetre,text = "Model")    
    finds.grid(row = 4,column =1)
    finds.config(bg = 'black',fg = 'white')
    find(finds) 
    
    finds = Label(fenetre,text = "vram en Go")    
    finds.grid(row = 4,column =2)
    finds.config(bg = 'black',fg = 'white')
    find(finds) 
    
    finds = Label(fenetre,text = "Fréquence mémoire en GHz")    
    finds.grid(row = 4,column =3)
    finds.config(bg = 'black',fg = 'white')
    find(finds) 
    
    finds = Label(fenetre,text = "Port")
    finds.grid(row = 4,column =4)
    finds.config(bg = 'black',fg = 'white')
    find(finds) 
    
    finds = Label(fenetre,text = "Prix")
    finds.grid(row = 4,column =5)
    finds.config(bg = 'black',fg = 'white')
    find(finds) 
    
    finds = Label(fenetre,text = " ")
    finds.grid(row = 5,column =0)
    finds.config(bg = 'white')
    find(finds)
    
    row = 0
    colonne = 0
    for resultot in resultat:
        row +=1
        for info in resultot:
            colonne += 1
            texte1 = Label(fenetre,text = info)
            texte1.grid(row = 6+row,column = colonne -1)
            """Enregistrement des labels dans un tableau de la class Texte"""
            texte(texte1)
            
        colonne = 0
        
        
    def action1(event):
        """Reset de la page par supression des labels et tri par la marque choisie par l'utilisateur."""
        
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
        
        """ Ouverture du dossier pour la récupération d'infrmation"""
        
        conn = sqlite3.connect('BDD_graphic_card.db')
        cur = conn.cursor()
        
        """Création d'une liste déroulante contenant les marques"""
        
        marque = listeCombo.get()
        print(marque)
        
        
        cur.execute("SELECT Id_marque_graphic_card FROM graphic_card_marque WHERE NOM_MARQUE = ?",(marque,))
        id_marque = cur.fetchone()
        
        """requete sql pour récupérer les lines corespondant à la marque choisie"""
        
        cur.execute("SELECT * FROM graphic_card WHERE Id_marque_graphic_card = ? ORDER BY prix ASC",id_marque)
        resultat = cur.fetchall()
        
        """lignes en y"""
        row = 0 
        """lignes en x"""
        colonne = 0  
        for resultot in resultat:
            row +=1
            for info in resultot:
                colonne += 1
                if resultot[0] == info:
                    texte1 = Label(fenetre,text = marque)
                else: texte1 = Label(fenetre,text = info)
                texte1.grid(row = 5+row,column = colonne -1)
                texte(texte1)
            colonne = 0
        cur.close()
        conn.close()
            
        
    cur.execute("SELECT NOM_MARQUE FROM graphic_card_marque") 
    listeMarques = cur.fetchall()
    print(listeMarques)
    
    Texte = Label(fenetre, text = 'Filtrer par marque :')
    Texte.grid(row = 3, column = 0)
    find(Texte)
    
    listeCombo = ttk.Combobox(fenetre, values=listeMarques)
    listeCombo.grid(row = 3, column = 1)
    listeCombo.bind("<<ComboboxSelected>>", action1)
    listeCombo.current(0)
    find(listeCombo)
    
    cur.close()
    conn.close()
    
    
    

def processeur():
    """Fonction affiche tout les processeurs présents dans la bdd ainsi que les informations qui y sont affiliées"""
    
    """--Suppresions des possibles labels deja existants--"""
    if all_texte != []:
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
    if all_find != []:
        for i in range(len(all_find)):
            all_find[i].find_label.destroy()
    
    
    conn = sqlite3.connect('BDD_processor.db')
    cur = conn.cursor()
    cur.execute("SELECT processor_marque.NOM_MARQUE,processor.MODEL,processor.generation,processor.Coeurs,processor.fréquence,processor.taille_de_gravure,processor.puissanceEnWatt,processor.prix FROM processor_marque INNER JOIN processor ON processor_marque.Id_marque_processor=processor.Id_marque_processor ORDER BY prix ASC")
    resultat = cur.fetchall()
    
    """Affichage des résultats"""
    
    finds = Label(fenetre,text = "Marque")
    finds.grid(row = 4,column =0)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Model")
    finds.grid(row = 4,column =1)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Génération")
    finds.grid(row = 4,column =2)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Coeurs")
    finds.grid(row = 4,column =3)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Fréquence CPU")
    finds.grid(row = 4,column =4)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Taille de Gravure")
    finds.grid(row = 4,column =5)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Puissance")
    finds.grid(row = 4,column =6)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Prix")
    finds.grid(row = 4,column =7)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = " ")
    finds.grid(row = 5,column =0)
    finds.config(bg = 'white')
    find(finds)
    
    row = 0
    colonne = 0
    for resultot in resultat:
        row +=1
        for info in resultot:
            colonne += 1
            texte1 = Label(fenetre,text = info)
            texte1.grid(row = 6+row,column = colonne -1)
            """Enregistrement des labels dans un tableau de la class Texte"""
            texte(texte1)
            
        colonne = 0
        
        
    def action1(event):
        """Reset de la page par supression des labels"""
        
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
        
        """ Ouverture du dossier pour la récupération d'infrmation"""
        
        conn = sqlite3.connect('BDD_processor.db')
        cur = conn.cursor()
        
        """Création d'une liste déroulante contenant les marques"""
        
        marque = listeCombo.get()
        print(marque)
        
        
        cur.execute("SELECT Id_marque_processor FROM processor_marque WHERE NOM_MARQUE = ?",(marque,))
        id_marque = cur.fetchone()
        print(id_marque)
        
        """requete sql pour récupérer les lignes corespondant à la marque choisie"""
        
        cur.execute("SELECT Id_marque_processor,MODEL,generation,Coeurs,fréquence,taille_de_gravure,puissanceEnWatt,prix FROM processor WHERE Id_marque_processor = ? ORDER BY prix ASC",id_marque)
        resultat = cur.fetchall()
        
        """lignes en y"""
        row = 0 
        """lignes en x"""
        colonne = 0  
        for resultot in resultat:
            row +=1
            for info in resultot:
                colonne += 1
                if resultot[0] == info:
                    """Permet l'affichage de la marque à la place de l'ancien indice"""
                    texte1 = Label(fenetre,text = marque)
                else: texte1 = Label(fenetre,text = info)
                texte1.grid(row = 5+row,column = colonne -1)
                texte(texte1)
            colonne = 0
        cur.close()
        conn.close()
            
        
    cur.execute("SELECT NOM_MARQUE FROM processor_marque") 
    listeMarques = cur.fetchall()
    print(listeMarques)
    for i in range(len(listeMarques)):
        listeMarques[i]= listeMarques[i][0]
    
    Texte = Label(fenetre, text = 'Filtrer par marque :')
    Texte.grid(row = 3, column = 0)
    find(Texte)
    
    listeCombo = ttk.Combobox(fenetre, values=listeMarques)
    listeCombo.grid(row = 3, column = 1)
    listeCombo.bind("<<ComboboxSelected>>", action1)
    listeCombo.current(0)
    find(listeCombo)
    
    cur.close()
    conn.close()
    
    
    

def carte_mere_bdd():
    
    if all_texte != []:
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
    if all_find != []:
        for i in range(len(all_find)):
            all_find[i].find_label.destroy()
    
    
    conn = sqlite3.connect('BDD_motherboard.db')
    cur = conn.cursor()
    cur.execute("SELECT motherboard_marque.NOM_MARQUE,motherboard.MODEL,motherboard.Socket,motherboard.generation,motherboard.port,motherboard.prix FROM motherboard_marque INNER JOIN motherboard ON motherboard_marque.Id_marque_motherboard=motherboard.Id_marque_motherboard ORDER BY prix ASC")
    resultat = cur.fetchall()
    
    """Affichage des résultats"""
    
    finds = Label(fenetre,text = "Marque")
    finds.grid(row = 4,column =0)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Model")
    finds.grid(row = 4,column =1)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Socket")
    finds.grid(row = 4,column =2)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    
    finds = Label(fenetre,text = "Génération")
    finds.grid(row = 4,column =3)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Port")
    finds.grid(row = 4,column =4)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    
    finds = Label(fenetre,text = "Prix")
    finds.grid(row = 4,column =5)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = " ")
    finds.grid(row = 5,column =0)
    finds.config(bg = 'white')
    find(finds)
    
    row = 0
    colonne = 0
    for resultot in resultat:
        row +=1
        for info in resultot:
            colonne += 1
            texte1 = Label(fenetre,text = info)
            texte1.grid(row = 6+row,column = colonne -1)
            """Enregistrement des labels dans un tableau de la class Texte"""
            texte(texte1)
            
        colonne = 0
        
        
    def action1(event):
        """Reset de la page par supression des labels"""
        
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
        
        """ Ouverture du dossier pour la récupération d'infrmation"""
        
        conn = sqlite3.connect('BDD_motherboard.db')
        cur = conn.cursor()
        
        """Création d'une liste déroulante contenant les marques"""
        
        marque = listeCombo.get()
        print(marque)
        
        
        cur.execute("SELECT Id_marque_motherboard FROM motherboard_marque WHERE NOM_MARQUE = ?",(marque,))
        id_marque = cur.fetchone()
        print(id_marque)
        
        """requete sql pour récupérer les lignes corespondant à la marque choisie"""
        
        cur.execute("SELECT Id_marque_motherboard,MODEL,Socket,generation,port,prix FROM motherboard WHERE Id_marque_motherboard = ? ORDER BY prix ASC",id_marque)
        resultat = cur.fetchall()
        
        """lignes en y"""
        row = 0 
        """lignes en x"""
        colonne = 0  
        for resultot in resultat:
            row +=1
            for info in resultot:
                colonne += 1
                if resultot[0] == info:
                    """Permet l'affichage de la marque à la place de l'ancien indice"""
                    texte1 = Label(fenetre,text = marque)
                else: texte1 = Label(fenetre,text = info)
                texte1.grid(row = 5+row,column = colonne -1)
                texte(texte1)
            colonne = 0
        cur.close()
        conn.close()
            
        
    cur.execute("SELECT NOM_MARQUE FROM motherboard_marque") 
    listeMarques = cur.fetchall()
    print(listeMarques)
    for i in range(len(listeMarques)):
        listeMarques[i]= listeMarques[i][0]
    
    Texte = Label(fenetre, text = 'Filtrer par marque :')
    Texte.grid(row = 3, column = 0)
    find(Texte)
    
    listeCombo = ttk.Combobox(fenetre, values=listeMarques)
    listeCombo.grid(row = 3, column = 1)
    listeCombo.bind("<<ComboboxSelected>>", action1)
    listeCombo.current(0)
    find(listeCombo)
    
    cur.close()
    conn.close()

def disque_dur():
    
    if all_texte != []:
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
    if all_find != []:
        for i in range(len(all_find)):
            all_find[i].find_label.destroy()
    
    
    conn = sqlite3.connect('BDD_disque_dur.db')
    cur = conn.cursor()
    cur.execute("SELECT disque_dur_marque.NOM_MARQUE,disque_dur.capacite_en_To,disque_dur.cache_en_Mo,disque_dur.tour_minute,disque_dur.prix FROM disque_dur_marque INNER JOIN disque_dur ON disque_dur_marque.Id_marque_disque_dur=disque_dur.Id_marque_disque_dur ORDER BY prix ASC")
    resultat = cur.fetchall()
    
    """Affichage des résultats"""
    
    finds = Label(fenetre,text = "Marque")
    finds.grid(row = 4,column =0)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Capacité en To")
    finds.grid(row = 4,column =1)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Cache en Mo")
    finds.grid(row = 4,column =2)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    
    finds = Label(fenetre,text = "Tour minute")
    finds.grid(row = 4,column =3)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    
    finds = Label(fenetre,text = "Prix")
    finds.grid(row = 4,column =4)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = " ")
    finds.grid(row = 5,column =0)
    finds.config(bg = 'white')
    find(finds)
    
    row = 0
    colonne = 0
    for resultot in resultat:
        row +=1
        for info in resultot:
            colonne += 1
            texte1 = Label(fenetre,text = info)
            texte1.grid(row = 6+row,column = colonne -1)
            """Enregistrement des labels dans un tableau de la class Texte"""
            texte(texte1)
            
        colonne = 0
        
        
    def action1(event):
        """Reset de la page par supression des labels"""
        
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
        
        """ Ouverture du dossier pour la récupération d'infrmation"""
        
        conn = sqlite3.connect('BDD_disque_dur.db')
        cur = conn.cursor()
        
        """Création d'une liste déroulante contenant les marques"""
        
        marque = listeCombo.get()
        print(marque)
        
        
        cur.execute("SELECT Id_marque_disque_dur FROM disque_dur_marque WHERE NOM_MARQUE = ?",(marque,))
        id_marque = cur.fetchone()
        print(id_marque)
        
        """requete sql pour récupérer les lignes corespondant à la marque choisie"""
        
        cur.execute("SELECT Id_marque_disque_dur,capacite_en_To,cache_en_Mo,tour_minute,prix FROM disque_dur WHERE Id_marque_disque_dur = ? ORDER BY prix ASC",id_marque)
        resultat = cur.fetchall()
        
        """lignes en y"""
        row = 0 
        """lignes en x"""
        colonne = 0  
        for resultot in resultat:
            row +=1
            for info in resultot:
                colonne += 1
                if resultot[0] == info and isinstance(info,int):
                    """Permet l'affichage de la marque à la place de l'ancien indice"""
                    texte1 = Label(fenetre,text = marque)
                else: texte1 = Label(fenetre,text = info)
                texte1.grid(row = 5+row,column = colonne -1)
                texte(texte1)
            colonne = 0
        cur.close()
        conn.close()
            
        
    cur.execute("SELECT NOM_MARQUE FROM disque_dur_marque") 
    listeMarques = cur.fetchall()
    print(listeMarques)
    for i in range(len(listeMarques)):
        listeMarques[i]= listeMarques[i][0]
    
    Texte = Label(fenetre, text = 'Filtrer par marque :')
    Texte.grid(row = 3, column = 0)
    find(Texte)
    
    listeCombo = ttk.Combobox(fenetre, values=listeMarques)
    listeCombo.grid(row = 3, column = 1)
    listeCombo.bind("<<ComboboxSelected>>", action1)
    listeCombo.current(0)
    find(listeCombo)
    
    cur.close()
    conn.close()

def boitier():
    
    if all_texte != []:
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
    if all_find != []:
        for i in range(len(all_find)):
            all_find[i].find_label.destroy()
    
    
    conn = sqlite3.connect('BDD_boitier.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM boitier")
    resultat = cur.fetchall()
    
    """Affichage des résultats"""
    
    finds = Label(fenetre,text = "Model")
    finds.grid(row = 4,column =0)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Couleur")
    finds.grid(row = 4,column =1)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "RGB")
    finds.grid(row = 4,column =2)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    
    finds = Label(fenetre,text = "Alimentation")
    finds.grid(row = 4,column =3)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    
    
    finds = Label(fenetre,text = "Prix")
    finds.grid(row = 4,column =4)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = " ")
    finds.grid(row = 5,column =0)
    finds.config(bg = 'white')
    find(finds)
    
    row = 0
    colonne = 0
    for resultot in resultat:
        row +=1
        for info in resultot:
            colonne += 1
            texte1 = Label(fenetre,text = info)
            texte1.grid(row = 6+row,column = colonne -1)
            """Enregistrement des labels dans un tableau de la class Texte"""
            texte(texte1)
            
        colonne = 0
        
        
    
    
    cur.close()
    conn.close()

def ram_bar_bdd():
    
    if all_texte != []:
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
    if all_find != []:
        for i in range(len(all_find)):
            all_find[i].find_label.destroy()
    
    
    conn = sqlite3.connect('BDD_ram.db')
    cur = conn.cursor()
    cur.execute("SELECT ram_marque.NOM_MARQUE,ram_bars.Model,ram_bars.Go,ram_bars.prix FROM ram_marque INNER JOIN ram_bars ON ram_marque.Id_marque_ram=ram_bars.Id_marque_ram ORDER BY prix ASC")
    resultat = cur.fetchall()
    
    """Affichage des résultats"""
    
    finds = Label(fenetre,text = "Marque")
    finds.grid(row = 4,column =0)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Model")
    finds.grid(row = 4,column =1)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = "Go")
    finds.grid(row = 4,column =2)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    
    finds = Label(fenetre,text = "Prix")
    finds.grid(row = 4,column =3)
    finds.config(bg = 'black',fg = 'white')
    find(finds)
    
    finds = Label(fenetre,text = " ")
    finds.grid(row = 5,column =0)
    finds.config(bg = 'white')
    find(finds)
    
    row = 0
    colonne = 0
    for resultot in resultat:
        row +=1
        for info in resultot:
            colonne += 1
            texte1 = Label(fenetre,text = info)
            texte1.grid(row = 6+row,column = colonne -1)
            """Enregistrement des labels dans un tableau de la class Texte"""
            texte(texte1)
            
        colonne = 0
        
        
    def action1(event):
        """Reset de la page par supression des labels"""
        
        for i in range(len(all_texte)):
            all_texte[i].texte_label.destroy()
        
        """ Ouverture du dossier pour la récupération d'infrmation"""
        
        conn = sqlite3.connect('BDD_ram.db')
        cur = conn.cursor()
        
        """Création d'une liste déroulante contenant les marques"""
        
        marque = listeCombo.get()
        print(marque)
        
        
        cur.execute("SELECT Id_marque_ram FROM ram_marque WHERE NOM_MARQUE = ?",(marque,))
        id_marque = cur.fetchone()
        print(id_marque)
        
        """requete sql pour récupérer les lignes corespondant à la marque choisie"""
        
        cur.execute("SELECT Id_marque_ram,Model,Go,prix FROM ram_bars WHERE Id_marque_ram = ? ORDER BY prix ASC",id_marque)
        resultat = cur.fetchall()
        
        """lignes en y"""
        row = 0 
        """lignes en x"""
        colonne = 0  
        for resultot in resultat:
            row +=1
            for info in resultot:
                colonne += 1
                if resultot[0] == info:
                    """Permet l'affichage de la marque à la place de l'ancien indice"""
                    texte1 = Label(fenetre,text = marque)
                else: texte1 = Label(fenetre,text = info)
                texte1.grid(row = 5+row,column = colonne -1)
                texte(texte1)
            colonne = 0
        cur.close()
        conn.close()
            
        
    cur.execute("SELECT NOM_MARQUE FROM ram_marque") 
    listeMarques = cur.fetchall()
    print(listeMarques)
    for i in range(len(listeMarques)):
        listeMarques[i]= listeMarques[i][0]
    
    Texte = Label(fenetre, text = 'Filtrer par marque :')
    Texte.grid(row = 3, column = 0)
    find(Texte)
    
    listeCombo = ttk.Combobox(fenetre, values=listeMarques)
    listeCombo.grid(row = 3, column = 1)
    listeCombo.bind("<<ComboboxSelected>>", action1)
    listeCombo.current(0)
    find(listeCombo)
    
    cur.close()
    conn.close()


##--Composition--##
    
def composition():
    """ Fonction permettant de créer une interface graphique et de conduire le client lors de la création d'un composition pc performante."""
    
    """Destruction des boutons pour permettre la réinitialisationde la fenetre"""
    bouton_categorie.destroy()
    bouton_creer_composition.destroy()
    
    """Entrée du prix de l'utilisateur"""
    
    fenetre.configure(bg='white')
    
    Texte = Label(fenetre, text =' Veuillez entrer votre budget :')
    Texte.grid(row = 0, column = 0)
    Texte.configure(bg='white')

    
    entree = Entry(textvariable =StringVar(),bd = 5 )
    entree.grid(row = 0, column = 1)
    
    def get_entry():
        global prix
        prix = float(entree.get())
        
        """supression de l'interface"""
        Texte.configure(text =  'Quel est votre besoin pour cette configuration? (Veuillez choisir une option)')
        entree.destroy()
        valider.destroy()
        
        """création de l'interface avec des boutons"""
        
            
        button1Var = IntVar()
        
        button1 = Checkbutton(fenetre,text = 'Vitesse/Puissance',variable=button1Var, onvalue=1, offvalue=0)
        button1.grid(row = 1,column = 0)
        button1.config(bg = 'white',fg = 'black')
        
        button2Var = IntVar()
        
        button2 = Checkbutton(fenetre,text = "Graphismes/Qualité d'affichage",variable=button2Var, onvalue=1, offvalue=0)
        button2.grid(row = 2,column = 0)
        button2.config(bg = 'white',fg = 'black')
        
        button3Var = IntVar()
        
        button3 = Checkbutton(fenetre,text = "Bureautique/traitement de textes",variable=button3Var, onvalue=1, offvalue=0)
        button3.grid(row = 3,column = 0)
        button3.config(bg = 'white',fg = 'black')
        
        button4Var = IntVar()
        
        button4 = Checkbutton(fenetre,text = "Traitement et stockage de donnée",variable=button4Var, onvalue=1, offvalue=0)
        button4.grid(row = 4,column = 0)
        button4.config(bg = 'white',fg = 'black')
        
        
        def try_validation():
            global choix,error_message
            if (button1Var.get() + button2Var.get() + button3Var.get() + button4Var.get()) == 1:
                if button1Var.get() == 1:
                    choix = 'Vitesse/Puissance'
                elif button2Var.get() == 1:
                    choix = "Graphismes/Qualité d'affichage"
                elif button3Var.get() == 1:
                    choix = "Bureautique/traitement de textes"
                else : choix = "Traitement et stockage de donnée"
                
                
                """ Réinitialistion de la fenetre """
                Texte.destroy()
                button1.destroy()
                button2.destroy()
                button3.destroy()
                button4.destroy()
                validation.destroy()
                if all_find != []:
                    for i in range(len(all_find)):
                        all_find[i].find_label.destroy()
                    
                
                search_for_choice(choix,prix) 
                
            else : 
                error_message = Label(fenetre,text = "Veillez à ne cocher qu'une seule case")
                error_message.grid(row= 6,column = 0)
                error_message.config(bg = 'white', fg = 'red')
                find(error_message)
        
        
        validation = Button(fenetre,text = 'Valider', command = try_validation)
        validation.grid(row = 5,column = 0)
        
        
    valider = Button(fenetre,text = 'Valider',command = get_entry)
    valider.grid(row = 0,column = 2)


def search_for_choice(choix,prix):
    global nb_page,nb_max_page

    Texte = Label(fenetre, text ='Voici les compositions accessibles à votre budget dans la catégorie:')
    Texte.grid(row = 0, column = 0)
    Texte.configure(bg='white')
    Texte1 = Label(fenetre, text =choix)
    Texte1.grid(row = 0, column = 1)
    Texte1.configure(bg='yellow')
    Texte2 = Label(fenetre, text = 'Budget : ')
    Texte2.grid(row = 1, column = 0)
    Texte2.configure(bg='white')
    Texte3 = Label(fenetre, text =prix)
    Texte3.grid(row = 1, column = 1)
    Texte3.configure(bg='yellow')
    
    def Bureautique_traitement_de_texte():
        global prix,nb_page,nb_max_page
        
        """ fonction permettant de créer des compositions pour un prix toujours inférieur à celui énnoncé sans se soucier de détails particuliers et sans barre de ram"""
        """    """
        conn = sqlite3.connect('BDD_compositions_compatibles.db')
        cur = conn.cursor()
        cur.execute("SELECT motherboard, processor,graphic_card,disque,disque_capacite,boitier,prix FROM compositions_compatibles WHERE prix <= ? and prix>?",(prix,prix-1))
        compositions_compatibles = cur.fetchall()
        for i in range(len(compositions_compatibles)):
            compositions_compatibles[i] = list(compositions_compatibles[i])
            compositions_compatibles[i].insert(6,'Aucune')
            compositions_compatibles[i] = tuple(compositions_compatibles[i])
            
        cur.close()
        conn.close()
        return compositions_compatibles
    
    def graphisme_image_quality():
        global prix
        conn = sqlite3.connect('BDD_compositions_compatibles.db')
        cur = conn.cursor()
        cur.execute("SELECT motherboard, processor,graphic_card,disque,disque_capacite,boitier,prix FROM compositions_compatibles")
        compositions_compatibles = cur.fetchall()
        cur.close()
        conn.close()
        conn = sqlite3.connect('BDD_ram.db')
        cur = conn.cursor()
        cur.execute("SELECT ram_marque.NOM_MARQUE,ram_bars.Model,ram_bars.prix FROM ram_marque INNER JOIN ram_bars ON ram_marque.Id_marque_ram=ram_bars.Id_marque_ram")
        ram_bars = cur.fetchall()
        cur.close()
        conn.close()
        compo = []
        for i in range(len(compositions_compatibles)):
            for j in range(len(ram_bars)):
                liste = (list(compositions_compatibles[i]))
                liste.insert(6,ram_bars[j][1])
                liste[7] = round(liste[7] + ram_bars[j][2],2)
                if liste[7]<=prix and liste[7] > prix - 3000 :
                    compo.append(liste)
        
        conn = sqlite3.connect('BDD_graphic_card.db')
        cur = conn.cursor()
        cur.execute("SELECT graphic_card_marque.NOM_MARQUE,graphic_card.MODEL,graphic_card.ram,graphic_card.frequence_mémoire,graphic_card.port,graphic_card.prix FROM graphic_card_marque INNER JOIN graphic_card ON graphic_card_marque.Id_marque_graphic_card=graphic_card.Id_marque_graphic_card ORDER BY prix ASC")
        graphic_card = cur.fetchall()
        
        composition = []
        for i in range(len(compo)):
            for j in range(len(graphic_card)):
                if graphic_card[j][2]>= 6 and (graphic_card[j][0] + graphic_card[j][1]) == compo[i][2]:
                    composition.append(compo[i])
        return composition
        
        
    def vitesse_puissance():
        
        global prix
        conn = sqlite3.connect('BDD_compositions_compatibles.db')
        cur = conn.cursor()
        cur.execute("SELECT motherboard, processor,graphic_card,disque,disque_capacite,boitier,prix FROM compositions_compatibles")
        compositions_compatibles = cur.fetchall()
        cur.close()
        conn.close()
        conn = sqlite3.connect('BDD_ram.db')
        cur = conn.cursor()
        cur.execute("SELECT ram_marque.NOM_MARQUE,ram_bars.Model,ram_bars.prix FROM ram_marque INNER JOIN ram_bars ON ram_marque.Id_marque_ram=ram_bars.Id_marque_ram")
        ram_bars = cur.fetchall()
        cur.close()
        conn.close()
        compo = []
        for i in range(len(compositions_compatibles)):
            for j in range(len(ram_bars)):
                liste = (list(compositions_compatibles[i]))
                liste.insert(6,ram_bars[j][1])
                liste[7] = round(liste[7] + ram_bars[j][2],2)
                if liste[7]<=prix and liste[7]>prix-0.5 :
                    compo.append(liste)
                    
        conn = sqlite3.connect('BDD_processor.db')
        cur = conn.cursor()
        cur.execute("SELECT processor_marque.NOM_MARQUE,processor.MODEL,processor.Coeurs,processor.prix FROM processor_marque INNER JOIN processor ON processor_marque.Id_marque_processor=processor.Id_marque_processor ORDER BY prix ASC")
        processor = cur.fetchall()
        
        composition = []
        for i in range(len(compo)):
            for j in range(len(processor)):
                if processor[j][2]>= 8 and (processor[j][0] + processor[j][1]) == compo[i][1]:
                    composition.append(compo[i])
        return composition
    
    def traitement_stockage():
        global prix
        conn = sqlite3.connect('BDD_compositions_compatibles.db')
        cur = conn.cursor()
        cur.execute("SELECT motherboard, processor,graphic_card,disque,disque_capacite,boitier,prix FROM compositions_compatibles")
        compositions_compatibles = cur.fetchall()
        cur.close()
        conn.close()
        conn = sqlite3.connect('BDD_ram.db')
        cur = conn.cursor()
        cur.execute("SELECT ram_marque.NOM_MARQUE,ram_bars.Model,ram_bars.prix FROM ram_marque INNER JOIN ram_bars ON ram_marque.Id_marque_ram=ram_bars.Id_marque_ram")
        ram_bars = cur.fetchall()
        cur.close()
        conn.close()
        compo = []
        for i in range(len(compositions_compatibles)):
            for j in range(len(ram_bars)):
                liste = (list(compositions_compatibles[i]))
                liste.insert(6,ram_bars[j][1])
                liste[7] = round(liste[7] + ram_bars[j][2],2)
                if liste[7]<=prix and liste[7]>prix-0.5 :
                    compo.append(liste)
                             
                
        composition = []
        for i in range(len(compo)):
            if compo[i][4]>= 8:
                composition.append(compo[i])
        return composition            
        
        
    if choix == 'Vitesse/Puissance':
        compositions_compatibles = vitesse_puissance()
    elif choix == "Graphismes/Qualité d'affichage":
        compositions_compatibles = graphisme_image_quality()
    elif choix == "Bureautique/traitement de textes":
        compositions_compatibles = Bureautique_traitement_de_texte()
    else :
        compositions_compatibles = traitement_stockage()
        
        
    if compositions_compatibles == []:
        error_text = Label(fenetre,text = " Aucun résultat.\n Il n'y a pas de composition possible à ce budget.\n Réessayez avec un budget plus élevé ou moins élevé")
        error_text.grid(row = 2,column =0)
        error_text.config(bg ='white', fg = 'red')
    else :
        finds = Label(fenetre,text = "motherboard")
        finds.grid(row = 3,column =0)
        finds.config(bg = 'black',fg = 'white')
        find(finds)
        
        finds = Label(fenetre,text = "processor")
        finds.grid(row = 3,column =1)
        finds.config(bg = 'black',fg = 'white')
        find(finds)
        
        finds = Label(fenetre,text = "graphic_card")
        finds.grid(row = 3,column =2)
        finds.config(bg = 'black',fg = 'white')
        find(finds)
        
        finds = Label(fenetre,text = "disque")
        finds.grid(row = 3,column =3)
        finds.config(bg = 'black',fg = 'white')
        find(finds)
        
        finds = Label(fenetre,text = "disque_capacite")
        finds.grid(row = 3,column =4)
        finds.config(bg = 'black',fg = 'white')
        find(finds)
        
        finds = Label(fenetre,text = "boitier")
        finds.grid(row = 3,column =5)
        finds.config(bg = 'black',fg = 'white')
        find(finds)
        
        finds = Label(fenetre,text = "Ram")
        finds.grid(row = 3,column =6)
        finds.config(bg = 'black',fg = 'white')
        find(finds)
        
        finds = Label(fenetre,text = "prix")
        finds.grid(row = 3,column =7)
        finds.config(bg = 'black',fg = 'white')
        find(finds)
        
        saut_de_ligne = Label(fenetre,text = " ")
        saut_de_ligne.grid(row = 4,column =6)
        saut_de_ligne.config(bg ='white')
        
        nombre_ligne_affichage = 16
        nb_page = 0
        nb_max_page = (len(compositions_compatibles))//nombre_ligne_affichage
        reste = (len(compositions_compatibles))%nombre_ligne_affichage
        
        nombre_de_page = Label(fenetre, text = "Nombre de Pages:")
        nombre_de_page.grid(row = 2,column = 3)
        nombre_de_page = Label(fenetre,text = str(nb_page)+'/'+str(nb_max_page))
        nombre_de_page.grid(row = 2,column = 4)
        
        
        
        
        def affichage(compositions_compatibles):
            global nb_page,nb_max_page
            
            row = 0
            colonne = 0
            for compositions in compositions_compatibles:
                row +=1
                for info in compositions:
                    colonne += 1
                    texte1 = Label(fenetre,text = info)
                    texte1.grid(row = 4+row,column = colonne -1)
                    """Enregistrement des labels dans un tableau de la class Texte"""
                    texte(texte1)
                
                colonne = 0
            nombre_de_page.configure(text = str(nb_page)+'/'+str(nb_max_page))
        
        def page_increment():
            global nb_page,nb_max_page
            
            for i in range(len(all_texte)):
                all_texte[i].texte_label.destroy()
                
            if nb_page < nb_max_page:
                nb_page +=1
                
                affichage(compositions_compatibles[nombre_ligne_affichage*(nb_page):nombre_ligne_affichage*(nb_page+1)])
                
            else: affichage(compositions_compatibles[nombre_ligne_affichage*(nb_page):len(compositions_compatibles)])
            
        def page_decrement():
            global nb_page
            
            if nb_page > 0:
                for i in range(len(all_texte)):
                    all_texte[i].texte_label.destroy()
                nb_page -=1
                affichage(compositions_compatibles[nombre_ligne_affichage*(nb_page):nombre_ligne_affichage*(nb_page+1)])
    
        bouton_suivant = Button(fenetre, text ="Page suivante",width=20,command=page_increment)
        bouton_suivant.grid(row = 2,column = 6)
        
        bouton_precedent = Button(fenetre, text ="Page Précédente",width=20,command = page_decrement)
        bouton_precedent.grid(row = 2,column = 0)
        
        affichage(compositions_compatibles[0:16])

##----- Création de la fenêtre -----##

fenetre = Tk()
fenetre.title('PC - Composants Base De Donnée')
fenetre.configure(bg='white')

##----- Création des boutons -----##

""" Bouton qui permettent de choisir le type de composant souhaité"""
bouton_categorie = Button(fenetre, text="Recherche d'un composant", width=50, command=recherche)
bouton_categorie.grid(row = 0, column = 0, padx=3, pady=3)

bouton_creer_composition = Button(fenetre, text='Creer une composition', width=50, command=composition)
bouton_creer_composition.grid(row = 0,column = 1, padx=3, pady=3)

##----- Boucle d'attente des événements -----##

fenetre.mainloop()




