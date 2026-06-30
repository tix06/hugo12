#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 18:15:15 2019

@author: erictixidor

https://python.doctor/page-python-serveur-web-creer-rapidement

"""

# coding: utf-8
#! /usr/bin/python
import cgi
import cgitb
import html
cgitb.enable()

import sqlite3 as lite
#import sys

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

con = None
con = lite.connect('clients.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS clients_login(id INT, name TEXT, pass TEXT, PRIMARY KEY(id AUTOINCREMENT))")
    cur.execute("SELECT * FROM clients_login")
    rows = cur.fetchall()




if (form.getvalue("name") != None) :
    nom = html.escape(form.getvalue("name"))
    mdp = html.escape(form.getvalue("pass"))
    titre_paragraphe = "<h2>VALIDER la saisie: {} => {}</h2>".format(nom,mdp)
    
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO clients_login (name,pass) VALUES(?,?)",(nom,mdp))
        con.commit()

else:
    titre_paragraphe = "<h2>Entrez les identifiants des clients</h2>"



html1 = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
    <style>
    button, input, select, textarea {
        font-family : inherit;
        font-size   : 100%;
    }
    input:focus, textarea:focus {
        background   : rgba(0,0,0,.1);
        border-radius: 5px;
        outline      : none;
    }
    </style>
</head>
<body>
"""

html2 = """
    <form action="/store_copy.py" method="post">
        <input type="text" name="name" placeholder="Nom Prenom" />
        <input type="text" name="pass" placeholder="mot de passe" />
        <input type="submit" name="send" value="AJOUTER">
    </form> 
"""

html3 = """</body>
</html>"""

table_affiche = '<h2>Table clients</h2><table border=1><tr>'
	
table_affiche += '<td>ID</td><td>nom</td><td>Pass</td>'
table_affiche+= '</tr>'
for row in rows:
    table_affiche += '<tr>'
    for i in row:
        table_affiche += '<td>'+str(i)+'</td>'
    table_affiche += '</tr>'
table_affiche += '</table>'

print(html1)
print()
print(titre_paragraphe)
print()
print(html2)
print(table_affiche)
print(html3)