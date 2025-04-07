from bs4 import BeautifulSoup
import requests

url = "https://"pt.wikipedia.org/wiki/Stars_Wars"

response = requests.get(url)

if response.status_code == 200:
    print("Sucesso ao acessar a página!")
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.title.string
    print(f"Título da página: {title}")
    
    paragrafo_um = soup.find("p").text
    print(f"Primeiro parágrafo: {paragrafo_um}")
    
    paragrafos = soup.find_all("p")
    
    if len(paragrafos) > 1:
        print(paragrafos[1].text)
    else:
        print("Não há um segundo parágrafo.")
        
    links = soup.find_all("a", href=True)[:5]
    
    
    for links in links:
        print(links["href"])

    
        