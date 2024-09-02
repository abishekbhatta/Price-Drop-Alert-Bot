import requests
from bs4 import BeautifulSoup

def scrape_price():
    URL = 'https://www.amazon.com/Apple-MacBook-Laptop-12%E2%80%91core-18%E2%80%91core/dp/B0CM5KK44S/ref=sr_1_1?dib=eyJ2IjoiMSJ9.rG6fbPywtPP9ovI037pco4PVhpJeQ8j8fHLUinumIc7byZdnuYJyZCnpeLiNJEbA_P1Nu6RR1TlzSff5hJYjbQaGxgypE-Dvpf7aZbcN26lLKLZRPYOorNyqrgTnM_PrUMHs7XCDIZoLkdOEx13AXoqCkIEqHXsWlRdJ73KqKv4KcsTtS5lRAfNVTaPugHgjMzO3O_1YfbEk__umlCMdUur6Yr2FiLEaA9vQ3p125pE.p8R_2c6q9aqPk9HpOTL2WcxPTeHCq4ZMLDaj1wKh4RY&dib_tag=se&keywords=macbook&qid=1725213926&sr=8-1&th=1'

    #sending get request to the url in order to recieve HTML
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    webpage = requests.get(URL, headers=headers)

    #parsing the HTML content using Beautiful Soup
    soup = BeautifulSoup(webpage.content, "html.parser")

    #making a list of span tag with class= "a-offscreen"
    tags_corresponding_prices = soup.find_all('span', class_="a-offscreen")

    #getting actual price
    return int(float(tags_corresponding_prices[0].text[1:9].replace(",","")))