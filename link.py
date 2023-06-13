import requests #Запрос к сайту
from bs4 import BeautifulSoup # Парсинг данных с сайта
import time
import pandas as pd

domains = str(input()).split()
domains = [ i.strip() for i in domains]

my_drop_links = []    
for i in domains:    
    res = drop_links_aceptor (i)
    res = res.split("\t")
    ahrefs = ahrefs_link (i)
    ahrefs = ahrefs.split("\t")
    result = res + ahrefs
    my_drop_links.append(result)
    
df = pd.DataFrame(my_drop_links, columns=['url','links','anchor','dr','backlinks', 'refdomains', 'dofollow', 'text_link'])
df['yandex_index'] = df.apply (lambda x: anchor_index_yandex (x['anchor'], x['url'] ), axis=1 )
df['google_index'] = df.apply (lambda x: anchor_index_google (x['anchor'], x['url'] ), axis=1 )
df.to_csv('result_link.csv')
df.head()
