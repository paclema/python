import requests
from bs4 import BeautifulSoup

root_url = 'http://youtube.com'

def get_video_page_urls():
    #Sending the http request
    response = requests.get('https://www.youtube.com/watch?v=QtXby3twMmI')
    # making the soup! yummy ;)
    soup = BeautifulSoup(response.text, "html.parser")
    video_page_urls =  [a.attrs.get('href') for a in soup.select('ul.video-list a[href^=/watch]')]
    return video_page_urls

def get_video_data(video_page_url):
    video_data = {}
    response = requests.get(root_url + video_page_url)
    soup = BeautifulSoup(response.text, "html.parser")
    video_data['url'] =  root_url + video_page_url
    video_data['title'] =  soup.select('span#eow-title')[0].get_text()
    video_data['visitas'] = soup.select('div.watch-view-count')[0].get_text()
    return video_data

def show_video_stats():
    video_page_urls = get_video_page_urls()
    for video_page_url in video_page_urls:
        print get_video_data(video_page_url)

print(show_video_stats())
