import hashlib
import os

def generate_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()  # Ensuring content is encoded to UTF-8

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

if __name__ == "__main__":
    from content_generator import generate_structured_article
    from scraper import scrape_page, extract_data

    # Scrape real articles from your site (https://www.businesstoday.in/latest/policy)
    url = 'https://www.businesstoday.in/latest/policy'
    soup = scrape_page(url)
    
    articles = []
    with open('latest_policies.txt', 'w', encoding='utf-8') as file:
        extract_data(soup, file)  # Extract and save the data to the file
        
    with open('latest_policies.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        
    topic = "Latest Topics on Gov policy"
    structured_article = generate_structured_article(articles, topic)

    if check_uniqueness(structured_article):
        print("This article is unique and has been logged.")
    else:
        print("This article is a duplicate.")
