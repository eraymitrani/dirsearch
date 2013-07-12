import urllib.request

dominio = input("Informe a url: ") 
listdir = open("FILE TXT HERE", "r") # Open file
for line in listdir.readlines():
    url = dominio + '/' + line.strip()
    try:
        site = urllib.request.urlopen(url)
        status = site.getcode()
        if status == 200:
            print (dominio + '/' + line.strip(),"OK")
        elif status == 302:
            print (dominio + '/' + line.strip(),"REDIR")
        
    except:
        site.status == 404 # Remove pages with 404 error
