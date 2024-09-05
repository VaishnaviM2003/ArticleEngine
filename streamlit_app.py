import streamlit as st
import requests
from bs4 import BeautifulSoup

# Scraper function
def scrape_page(url):
    response = requests.get(url)
    response.raise_for_status()  # Catch any HTTP errors
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# Data extraction function
def extract_data(soup):
    articles = soup.find_all('div', class_='widget-listing')  

    if not articles:
        st.write("No articles found!")
        return []

    scraped_data = []
    for article in articles:
        topic_link = article.find('a')
        if topic_link:
            topic_name = topic_link.get_text(strip=True)
            topic_url = topic_link['href']
        else:
            topic_name = 'No topic name'
            topic_url = 'No URL'

        snippet = article.find('p')  
        if snippet:
            snippet_text = snippet.get_text(strip=True)
        else:
            snippet_text = 'No summary available'

        scraped_data.append({
            'Topic Name': topic_name,
            'Topic URL': topic_url,
            'Summary': snippet_text
        })

    return scraped_data

# Streamlit app layout
st.title('AI-Based Topic Scraper and Article Generator')

# Adding a button to trigger scraping
if st.button('Scrape Data'):
    url = 'https://www.businesstoday.in/latest/policy'
    
    with st.spinner('Scraping data...'):
        try:
            soup = scrape_page(url)
            scraped_articles = extract_data(soup)

            if scraped_articles:
                st.write(f"Scraped {len(scraped_articles)} articles from {url}")
                
                # Display the scraped data on the page
                for article in scraped_articles:
                    st.subheader(article['Topic Name'])
                    st.write(f"URL: [Link]({article['Topic URL']})")
                    st.write(f"Summary: {article['Summary']}")
                    st.write("-" * 50)
            else:
                st.write("No articles to display.")

        except requests.exceptions.HTTPError as e:
            st.error(f"HTTP error occurred: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Generate article 
if st.button('Generate Article'):
    # displaying the scraped data in the form of an article
    st.subheader("Latest policies in Latest Topics")
    st.write("Introduction")
    st.write("The world of Latest Topics is rapidly evolving. In this article, we explore the latest policies as of today.")
    st.write("Key Updates")

    # formatting the content
    if 'scraped_articles' in locals() and scraped_articles:
        for article in scraped_articles:
            st.write(f"- **{article['Topic Name']}**: {article['Summary']} (Read more [here]({article['Topic URL']}))")

    st.write("Conclusion")
    st.write("These are the most recent developments in Latest Topics. Stay tuned for more updates.")
