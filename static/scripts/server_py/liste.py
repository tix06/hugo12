#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import html
cgitb.enable()

import sqlite3 as lite


form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

con = None
con = lite.connect('clients.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS clients_login(id INTEGER, name TEXT, pass TEXT)")
    cur.execute("SELECT * FROM clients_login")
    rows = cur.fetchall()




if (form.getvalue("alphab") == 'a') :

    
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM clients_login WHERE substr(name,1,1) IN ('A','B','C','D','E','F','G','H')")
        rows = cur.fetchall()
        con.commit()
elif form.getvalue("alphab") == 'i':
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM clients_login WHERE substr(name,1,1) IN ('I','J','K','L','M','N','O','P')")
        rows = cur.fetchall()
        con.commit()

else:
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM clients_login WHERE substr(name,1,1) IN ('Q','R','S','T','U','V','X','Y','Z')")
        rows = cur.fetchall()
        con.commit()

titre_paragraphe = '<h2>Choisissez</h2>'
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
    <form action="/liste.py" method="post">
        <div>
        <input type="radio" id="a" name="alphab" value="a"
         checked>
        <label for="huey">a-h</label>
        </div>

        <div>
        <input type="radio" id="i" name="alphab" value="i">
        <label for="dewey">i-p</label>
        </div>

        <div>
        <input type="radio" id="q" name="alphab" value="q">
        <label for="louie">q-z</label>
        </div>


        <input type="submit" name="send" value="Valider">
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