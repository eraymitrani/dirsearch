import urllib.request

dominio = input("URL: ")
listdir = open("dictionary.txt", "r")
for line in listdir.readlines():
    url = dominio + '/' + line.strip()
    try:
        site = urllib.request.urlopen(url)
        status = site.getcode()
        if status == 200:
            print (dominio + '/' + line.strip(),"OK")
        elif status == 200:
            print (dominio + '/' + line.strip(),"OK")
        
    except:
        site.status == 404 # Remover paginas 404
