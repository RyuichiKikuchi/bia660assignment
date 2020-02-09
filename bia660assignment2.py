from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import re
import requests

import csv


url = 'https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domains'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('td')
#using re to extr
pattern1 = re.compile('<td>([.].*?)</td>')
pattern2 = re.compile('title=".+?">([.].*?)</a>')
list_1 = re.findall(pattern1,str(links))
list_2 = re.findall(pattern2,str(links))

del list_1[0:2] 
del list_1[16]


domain_list = list_1 + list_2
print(domain_list)

with open('./Desktop/img/domain_list.csv','w',encoding='utf-8') as csv_file1:
    writer = csv.writer(csv_file1)
    for i in domain_list:
        writer.writerow([i])

with open('./Desktop/img/example_domain.csv','w',encoding='utf-8') as csv_file2:
    writer = csv.writer(csv_file2)
    for i in domain_list:
        try:
            response = requests.get("http://example"+i)
            example_domain = {"example"+i:response.status_code}
            print(example_domain)
        except RequestException:    # RequestException includes all exceptions
            example_domain = {"example"+i:"error"}
            print(example_domain)
        writer.writerow([example_domain])


