import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
url='https://www.tiobe.com/tiobe-index/'
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
table=soup.find('table',class_='table table-striped table-top20') 
landveds=table.find_all('td')
langveg=[]
for i in range(1,len(landveds)):
    w=landveds[i].get_text()
    langveg.append(' '.join(w))

b=4
for i in range(1,21):
    
     print(i,landveds[b].get_text(),landveds[b+1].get_text())
     b+=7
  