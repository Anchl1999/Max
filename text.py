# import requests
# response = requests.get('https://nstidehradun.dgt.gov.in/')
# print(response.headers)

# import requests
# from bs4 import BeautifulSoup
# def scrape_example():
#     url = 'https://www.magicedtech.com/'
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text,'html.parser')
#         title = soup.title.get_text()
#         print(f'Title of the page: {title}')
#     else:
#         print(f'Failed to retreive the page. Status code: {response.status_code}')
# if __name__ == "__main__":
#     scrape_example()

# import requests
# from bs4 import BeautifulSoup
# url = 'https://books.toscrape.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text,'html.parser')
# product_price = soup.find_all("div",class_ = "product_price")
# for price in product_price:
#     print(price.p.text)






