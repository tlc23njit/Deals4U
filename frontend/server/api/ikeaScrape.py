import requests
from bs4 import BeautifulSoup
def ikeaScrape():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    headers = {'User-Agent': user_agent}
    URL = "https://www.ikea.com/us/en/cat/lower-price/"
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find_all("div", class_="plp-fragment-wrapper")
    job_elements = results
    ikeaProducts = []
    for job_element in job_elements:
        products = {}
        link_url = job_element.find_all("a")[0]["href"]
        img_element = job_element.find_all("img")[0]["src"]
        job_element = job_element.text.strip()
        #print(job_element)
        name_element = job_element.split("Price")[1].split("$")[0]
        sale_element = float(job_element.split("$")[1].split("Price")[0].replace(',',''))
        price_element  = float(job_element.split("Previous price: $")[1].split("$")[0].replace(',',''))
        products['title'] = name_element
        products['sale_price'] = sale_element
        products['regular_price'] = price_element
        products['href'] = link_url
        products['image_url'] = img_element
        ikeaProducts.append(products)
    return ikeaProducts

print(ikeaScrape())