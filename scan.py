#!/usr/bin/env python

import urllib.request

dominio = input("Informe a url: ")
listdir = open("spse2.txt", "r")
for line in listdir.readlines(): # pega cada linha do arquivo do listdir
    url = dominio + '/' + line.strip()
    try:
        site = urllib.request.urlopen(url)
        status = site.getcode()
        if status == 200:
            print (dominio + '/' + line.strip(),"OK")
        elif status == 302:
            print (dominio + '/' + line.strip(),"Redir")
        
    except:
        site.status == 404 # Remover paginas 404
            
        
        
