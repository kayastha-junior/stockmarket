import csv
import requests
from bs4 import BeautifulSoup
f=open('stock.csv','w',newline='')
writer=csv.writer(f)
url=requests.get('http://www.nepalstock.com/main/calculation/index/2/?startDate=2018-01-01&endDate=2019-09-05&stock-symbol=&_limit=500').text
soup=BeautifulSoup(url,'html.parser')
mtable=soup.find('table',{'class':'table'})
tdata=mtable.find_all('tr')[1:-1]
#print(tdata)
for row in tdata:
    cols=row.findChildren(recursive=False)
    cols=[ele.text.strip() for ele in cols]    
    writer.writerow(cols)
    print(cols)


