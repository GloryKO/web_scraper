

import requests
from bs4 import BeautifulSoup
import time

def scrape_website_url(url):
    start_time = time.time()

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        titles = soup.find_all('h3')
        if titles:
            extracted_data = [title.text for title in titles]
        else:
            extracted_data = ["No titles found on this page."]

        end_time = time.time()
        elapsed_time = end_time - start_time

        return extracted_data, elapsed_time
    else:
        return None, 0

# List of website URLs
website_urls = [
    "https://www.bbc.com/news",
    "https://blog.hubspot.com",
     "https://neilpatel.com/blog",
     "https://backlinko.com/blog",
     "https://www.copyblogger.com/blog",
     "https://kissmetrics.com/blog",
     "https://www.quicksprout.com/blog",
 ]

for url in website_urls:
    titles, execution_time = scrape_website_url(url)

    print(f"Scraped titles from {url}:")
    if titles is not None:
        for i, title in enumerate(titles, start=1):
            print(f"{i}. {title}")
    else:
        print("Failed to retrieve website content.")

    print("Execution Time:", execution_time, "seconds")
    print()
