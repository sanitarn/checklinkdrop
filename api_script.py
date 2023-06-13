from config import TOKEN_Ahrefs, TOKEN_XMLRiver

TOKEN_Ahrefs = TOKEN_Ahrefs
TOKEN_XMLRiver = TOKEN_XMLRiver

def ahrefs_link (link:str):
    """Получение показателей Ahrefs dr_momain, backlinks, refdomains, dofollow, text_link"""
    try:
        link = link.strip()    
        ahrefs_urls_param = {
          "token": TOKEN_Ahrefs,
          "from": "metrics_extended",
          "target": link,
          "mode": "exact",
          "output": "json"
        }
        ahrefs_dr = {
          "token": TOKEN_Ahrefs",
          "from": "domain_rating",
          "target": link,
          "mode": "domain",
          "output": "json"
        }
        api_ahrefs = requests.post('https://apiv2.ahrefs.com/', data=ahrefs_urls_param)
        dr_api_ahrefs = requests.post('https://apiv2.ahrefs.com/', data=ahrefs_dr)
        backlinks = api_ahrefs.json()['metrics']['backlinks']
        refdomains = api_ahrefs.json()['metrics']['refdomains']
        dofollow = api_ahrefs.json()['metrics']['dofollow']
        text_link = api_ahrefs.json()['metrics']['text']
        dr_momain = dr_api_ahrefs.json()['domain']['domain_rating']
        return (f'{dr_momain} \t  {backlinks} \t  {refdomains} \t  {dofollow} \t {text_link}')
    except:
        return (f'0 \t 0 \t 0 \t 0 \t 0')
    
def drop_links_aceptor (url: str):
    try:
        headers = {"User-Agent":"Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"}
        response = requests.get(url, headers=headers,  allow_redirects=True)
        html = BeautifulSoup(response.text, "html.parser")
        for tag in html.findAll():
            if tag.name == 'a':
                if 'fon.bet' in str(tag):  
                    return(f"{url.strip()} \t {tag['href']} \t {tag.text}")
        return (f'{url.strip()} \t ссылка отсутствует \t Анкор отсутствует')
    except:
        return (f'{url.strip()} \t Проблемы с сайтом или Сайт не доступен \t NAN')
    
    
def anchor_index_yandex (anchor, page):
    site_url = "url:"+ str(page) + f' "{anchor}"'
    xml_yandex = f"http://xmlriver.com/search_yandex/xml?user=453&key={TOKEN_XMLRiver}&query=" +\
    site_url +\
    "&lr=213"
    query = requests.get(xml_yandex.strip(), timeout=20) 
    xml = BeautifulSoup(query.text, 'html.parser')
    try:
        if xml.find('found',{'priority':"all"}):
            find_count_page =  int (xml.find('found',  priority="all").text)            
            if find_count_page > 0:
                return (1)
        else:    
            return (0) 
    except:
        return (0)

def anchor_index_google (anchor, page):
    site_url = "site:"+ str(page) + f' "{anchor}"'
    xml_yandex = "http://xmlriver.com/search/xml?user=453&key={TOKEN_XMLRiver}&query=" +\
    site_url 
    query = requests.get(xml_yandex.strip(), timeout=20) 
    xml = BeautifulSoup(query.text, 'html.parser')
    try:
        if xml.find('found',{'priority':"all"}):
            find_count_page =  int (xml.find('found',  priority="all").text)            
            if find_count_page > 0:
                return (1)
        else:    
            return (0) 
    except:
        return (0)