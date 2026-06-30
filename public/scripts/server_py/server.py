#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 18:11:39 2019

@author: erictixidor
https://python.doctor/page-python-serveur-web-creer-rapidement

"""

import http.server

 
PORT = 8800
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print("Serveur actif sur le port :", PORT)
print("handler.cgi_directories ", handler.cgi_directories)
print("handler ", handler)
httpd = server(server_address, handler)


httpd.serve_forever()