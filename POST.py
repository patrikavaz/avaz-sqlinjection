import requests 
from bs4 import BeautifulSoup

# Burp 
proxy = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

URL = 'http://'

header = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
with open('text.txt','r') as file:
    
    for i in file:
        
        paylod = i.strip()

        date = {
            'login': paylod,
            # 'pass' : '1234',
        }

        req = requests.post(URL, data=date, headers=header, proxies=proxy, verify=False)

        suop = BeautifulSoup(req.text, 'html.parser')
        plan_txst = suop.get_text()
        if 'Attack detected!' not in plan_txst:
            print(f'patlod -> {paylod}')
            print(f'[+] Status Code: {req.status_code}.')
            print(plan_txst.strip())
            print('-'*50)
