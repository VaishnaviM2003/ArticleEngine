import streamlit as st
import requests
from bs4 import BeautifulSoup
import datetime
import hashlib
import os

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

# Uniqueness checker
def generate_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def check_uniqueness(content, log_file="uniqueness_log.txt"):
    content_hash = generate_hash(content)

    if not os.path.exists(log_file):
        with open(log_file, 'w', encoding='utf-8') as f: 
            f.write('')  # Create the log file if it doesn't exist

    with open(log_file, 'r', encoding='utf-8') as f:  # Use 'utf-8' encoding when reading file
        logged_hashes = f.read().splitlines()

    if content_hash in logged_hashes:
        return False  # Duplicate content
    else:
        with open(log_file, 'a', encoding='utf-8') as f:  
            f.write(content_hash + '\n')
        return True  # Unique content

# Streamlit app layout
st.title('AI-Based Topic Scraper and Article Generator')

# Define session state to hold scraped articles
if 'scraped_articles' not in st.session_state:
    st.session_state.scraped_articles = []

# Adding a button to trigger scraping
if st.button('Scrape Data'):
    url = 'https://www.businesstoday.in/latest/policy'
    
    with st.spinner('Scraping data...'):
        try:
            soup = scrape_page(url)
            st.session_state.scraped_articles = extract_data(soup)

            if st.session_state.scraped_articles:
                st.write(f"Scraped {len(st.session_state.scraped_articles)} articles from {url}")
                
                # Display the scraped data on the page
                for article in st.session_state.scraped_articles:
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
    if st.session_state.scraped_articles:
        # Generate article content
        today_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        topic = "Latest Topics on Gov policy"
        article_content = f"# {topic}\n"
        article_content += f"**Generated on:** {today_date}\n\n"
        article_content += f"### Introduction\n"
        article_content += f"The world of {topic} is rapidly evolving. In this article, we explore the latest policies as of {today_date}.\n\n"

        article_content += "### Key Updates\n"
        for i, article in enumerate(st.session_state.scraped_articles, start=1):
            title = article.get('Topic Name', 'No Title')
            summary = article.get('Summary', 'No Summary Available')
            url = article.get('Topic URL', '#')
            
            article_content += f"**Update {i}:**\n"
            article_content += f"- **Title**: [{title}]({url})\n"
            article_content += f"- **Summary**: {summary}\n"
            article_content += f"- **Read more at**: [{url}]({url})\n\n"

        article_content += "### Conclusion\n"
        article_content += f"These are the most recent developments in {topic}. Stay tuned for more updates.\n"

        # Check for uniqueness and display the article
        if check_uniqueness(article_content):
            st.subheader("Generated Article")
            st.write(article_content)
            st.write("This article is unique and has been logged.")
        else:
            st.write("This article is a duplicate.")

    else:
        st.write("No articles have been scraped yet. Please click 'Scrape Data' first.")
