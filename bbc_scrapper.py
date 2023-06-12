import requests
from bs4 import BeautifulSoup
import time

def scrape_bbc_news(url):
    start_time = time.time()
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the news article titles
        article_titles = soup.find_all('h3')

        # Extract the text from the first 10 article titles
        
        news_titles = [title.text for title in article_titles]
        news_titles = news_titles[:10]
        end_time = time.time()
        elapsed_time = end_time - start_time

        return news_titles, elapsed_time
    else:
        return "Error: Failed to retrieve BBC News content.", 0

# Example usage
bbc_news_url = "https://www.bbc.com/news"
titles, execution_time = scrape_bbc_news(bbc_news_url)

print("Scraped News Titles:")
for title in titles:
    print("- ", title)

print("Execution Time:", execution_time, "seconds")
