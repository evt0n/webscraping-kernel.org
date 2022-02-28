import requests
import re
from bs4 import BeautifulSoup

url = requests.get('https://www.kernel.org')
soup = BeautifulSoup(url.content, "html.parser")

scrap = soup.find_all('table', attrs={'id':'latest'})
kernel_latest = scrap[0].find('a').get_text()
download = scrap[0].find('a').get('href')

print('The Linux Kernel Archives - https://www.kernel.org/ \nKernel Latest Release: '+kernel_latest)
print('Download: wget ' +download)

print('\n--- Others releases ')
scrap2 = soup.find_all('table', attrs={'id':'releases'})
tr_list = scrap2[0].find_all('tr')

rellist = []
for all_td_list in tr_list:
    for td_list in all_td_list.select('td:not(a)'):
        releases = td_list.get_text()
        releases=re.sub("\[.*?\]","",releases)
        rellist.append(releases)
print(' '.join(rellist).replace('                 ','\n').replace('2022-','-> 2022-'))
