# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

url = "http://www.youtube.com/watch?v=QtXby3twMmI"

# Realizamos la peticion a la web
req = requests.get(url)

# Comprobamos que la petición nos devuelve un Status Code = 200
statusCode = req.status_code
if statusCode == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text,"html.parser")

    # Obtenemos todos los divs donde estan las entradas
    views = html.find_all('div',{'class':'watch-view-count'})

    # Recorremos todas las entradas para extraer el título, autor y fecha
    for i,view in enumerate(views):
        # Con el método "getText()" no nos devuelve el HTML
        numero_view = view.getText()

        # Imprimo el Título, Autor y Fecha de las entradas
        print "%s" %(numero_view)

else:
    print "Status Code %d" %statusCode
