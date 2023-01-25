from bs4 import BeautifulSoup
import requests
import lxml

url="https://www.imdb.com/chart/top/"
response=requests.get(url)

soup=BeautifulSoup(response.content,"lxml")
top_250=soup.find("tbody",attrs={"class":"lister-list"}).find_all("tr")
sayac=0

for index,movie in enumerate(top_250):
    name=movie.find("td",attrs={"class":"titleColumn"}).a.text
    history=movie.find("td",attrs={"class":"titleColumn"}).span.text
    vote=movie.find("td",attrs={"class":"ratingColumn"}).strong.text
    sayac=sayac+1
    print("{}. {} | {} | {}".format(sayac,name,history,vote))