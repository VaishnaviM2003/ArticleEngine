import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    response.raise_for_status()  
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_data(soup, file):
    # Find article containers based on real structure of Business Today
    articles = soup.find_all('div', class_='widget-listing')

    if not articles:
        print("No articles found!")
        return

    for article in articles:
        # Extract topic details based on Business Today's structure
        topic_link = article.find('a')
        if topic_link:
            topic_name = topic_link.get_text(strip=True)
            topic_url = topic_link['href']
        else:
            topic_name = 'No topic name'
            topic_url = 'No URL'
        
        # Extract summary if available
        snippet = article.find('p')  
        if snippet:
            snippet_text = snippet.get_text(strip=True)
        else:
            snippet_text = 'No summary available'
        
        file.write(f"Topic Name: {topic_name}\n")
        file.write(f"Topic URL: {topic_url}\n")
        file.write(f"Summary: {snippet_text}\n")
        file.write("-" * 50 + "\n")

def main():
    url = 'https://www.businesstoday.in/latest/policy'  # Scraping just the first page for now
    with open('latest_policies.txt', 'w', encoding='utf-8') as file:
        print(f"Scraping {url}...")
        soup = scrape_page(url)
        articles = soup.find_all('div', class_='widget-listing')  

        if not articles:
            print("No articles found!")
        else:
            extract_data(soup, file)

    print("Data has been saved to latest_policies.txt")

if __name__ == '__main__':
    main()
