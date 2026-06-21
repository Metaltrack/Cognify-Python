import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_default():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        books_data = []

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            link = book.h3.a["href"]

            books_data.append({
                "Title": title,
                "Price": price,
                "Link": url + link
            })

        df = pd.DataFrame(books_data)
        print(df)

        df.to_csv("webData.csv", index=False)

        print("\nData saved to webData.csv")

    else:
        print(f"Failed to retrieve webpage, err: {response.status_code}")


#If we are webscraping we already need to know what data we are looking for, but if I wanna
#scrape random webpages not knowing what data I need, This function will scrape for the 
#most common data in a web page (headings, links, etc)
def get_custom(custom_url :str):
    response = requests.get(custom_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        scraped_data = []

        if soup.title:
            scraped_data.append({
                "Type": "Page Title",
                "Content": soup.title.text.strip()
            })
        for h in soup.find_all(["h1","h2","h3","h4","h5","h6"]):
            scraped_data.append({
                "Type": "Heading",
                "Content": h.text.strip()
            })
        for p in soup.find_all("p"):
            scraped_data.append({
                "Type": "Paragraph",
                "Content": p.text.strip()
            })
        for a in soup.find_all("a", href=True):
            scraped_data.append({
                "Type": "Link",
                "Content": a["href"]
            })
        for img in soup.find_all("img", src=True):
            scraped_data.append({
                "Type": "Image",
                "Content": img["src"]
            })

        df = pd.DataFrame(scraped_data)

        print(df)

        df.to_csv("webData.csv", index=False)
        print("\nData saved to webData.csv")
    else:
        print(f"Failed to retrieve webpage, err: {response.status_code}")



if __name__ == "__main__":
    while(True):
        print("""Level 3 Web Scraping...
                    press [1] to start.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            user_url = str(input("Enter url (press enter to use default url ['http://books.toscrape.com/']): "))
            if user_url:
                get_custom(user_url)
            else:
                get_default()
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue
