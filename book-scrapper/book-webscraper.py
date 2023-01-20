import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

#empty list to store 
book_list = []

# for tag in range(1,51): 
def getBooks(tag):
    print(tag)
    url = f'https://books.toscrape.com/catalogue/page-{tag}.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    catalog = soup.find_all("article", {"class": "product_pod"})

    for book in catalog:
        title = book.find_all("a")[1]['title']
        price = float(book.find("p", {"class" : "price_color"}).text[2:]) #replace("Â£", "")
        status = book.find("p", {"class" : "instock availability"}).text.strip()
        rating = book.find("p")["class"][1]
        img = book.find_all("img")[0]["src"]

        books = {
            'title': title,
            'price': price,
            'status': status,
            'rating': rating,
            'image': img
        }
        book_list.write(books)

for tag in range(2,11):
    getBooks(tag)
    df = pd.DataFrame(book_list)
    print(df.head())
    
    #to CSV
    # filename = f'result_csv/page_{tag}.csv' 
    # df.to_csv(filename, index=False)
    
    #to JSON
    filename = f'page_{tag}.json'
    df.to_json(filename, orient="index")
    

# tag = 0
# for page_number in range(1, tag + 1):
#     # Scrape the data for the current page
#     data = getBooks(page_number)

#     # Create a DataFrame from the scraped data
#     df = pd.DataFrame(data, columns=['title', 'price', 'status', 'rating', 'image'])

#     # Create a new CSV file with the name "page_[page_number].csv"
#     filename = 'page_{}.csv'.format(page_number)
#     df.to_csv(filename, index=False)
