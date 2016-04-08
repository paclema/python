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
    #print soup.prettify()


    # Obtenemos todos los divs donde estan las entradas
    related_videos = html.find_all("div",class_="content-wrapper")
    #print related_videos
    #print type(related_videos)
    #print related_videos[0]


    for element in related_videos:
        date = element.find(class_="title").get_text()

    """
    for i,related_video in enumerate(related_videos):

        #content_wrapper = related_video.find('div', {'class' : 'content-wrapper'})
        # Recorremos todas las entradas para extraer el título, autor y fecha
        #for i,content_wrapper in enumerate(content_wrappers):
            # Con el método "getText()" no nos devuelve el HTML
        titulo = related_video.find('div', {'class' : 'tittle'}).getText()
        titulo = related_video.find('span', {'class' : 'tittle'}).getText()
            # Sino llamamos al método "getText()" nos devuelve también el HTML
        visualizaciones = related_video.find('span', {'class' : 'view-count'}).getText()

            # Imprimo el Título, Autor y Fecha de las entradas
        print "%d - %s  |  %s " %(i+1,titulo,visualizaciones)
    """
else:
    print "Status Code %d" %statusCode
