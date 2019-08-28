import csv
import requests
import urllib.request
from bs4 import BeautifulSoup
f=open('data2.csv','w',newline='')
writer=csv.writer(f)
url=requests.get('http://nepalstock.com.np/todaysprice')
soup=BeautifulSoup(url,'html.parser')
tbody=soup('table',{'class':'table'})[0].find_all('tr')
for row in tbody:
    cols=row.findChildren(recursive=False)
    cols=[ele.text.strip() for ele in cols]    
    writer.writerow(cols)
    print(cols)
