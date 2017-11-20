import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

file_name = "generic_%s.csv" % datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
generic_url = "https://www.coindesk.com/the-ultimate-list-of-resources-for-researching-and-launching-icos/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

links_final = []

page = requests.get(generic_url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
# print soup.prettify()


for link in soup.find_all('a'):
    if link.parent.name == "strong":
        links_final.append([link.get('href')])
    # HERE!!!
    # if link.contents[0].get('class') and link.contents[0].get('class')[0] == u"directLink":
    #     links_final.append([link.get('href').replace("/url?q=", "")])

with open(file_name, 'wb') as file:
    for link in links_final:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        wr.writerow(link)

