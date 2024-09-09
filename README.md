# ArticleEngine
An engine capable of scraping the latest information on a chosen topic, organizing it into well-structured articles.

# AI-Based Topic Scraper and Article Generator Engine

This project builds an engine capable of scraping the latest information from a chosen website, organizing it into well-structured articles ensuring uniqueness by maintaining logs to avoid repetition.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Streamlit App](#running-the-streamlit-app)
  - [Scraping Data](#scraping-data)
  - [Generating an Article](#generating-an-article)
- [Directory Structure](#directory-structure)
- [Streamlit App](#streamlit-app)
- [Project Files](#project-files)
- [Contributing](#contributing)
- [License](#license)

## Overview
This engine automatically scrapes the latest information from a given website (e.g., Business Today - Latest Policies), generates well-organized articles with summaries and links, and checks for content uniqueness using a hashing mechanism.

The articles generated are displayed on the Streamlit page, and users can trigger the scraping and article generation with the press of a button.

## Features
- **Scraping:** Scrapes real-time data from news websites.
- **Article Generation:** Automatically creates articles with a title, introduction, key updates, and conclusion.
- **Uniqueness Check:** Uses hash-based uniqueness checking to ensure no duplicate content is generated.
- **Streamlit Interface:** Provides a user-friendly interface to scrape data and generate articles with just a click.
- **Log File:** Logs unique articles in a text file for future reference.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.9+
- pip (Python package manager)
- Internet connection (for scraping)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/https://github.com/VaishnaviM2003/ArticleEngine/ArticleEngine.git
   cd ArticleEngine
2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
3. **Add Environment Variables**
   You might need to configure environment variables (e.g., paths for saving logs) if necessary.

## Usage
### Running the Streamlit App
To start the Streamlit application:

  ```bash
  streamlit run streamlit_app.py
  ```
The app will open in your web browser. You can scrape data and generate unique articles with buttons available on the interface.

### Scraping Data
1. Click on the Scrape Data button.
2. The latest data will be scraped from Business Today.
3. The scraped data will be displayed in the Streamlit app and also saved to <div class="highlight-box"> latest_policies.txt </div>

## Directory Structure

  ```plaintext
ai-topic-scraper/
│
├── streamlit_app.py                 # Main Streamlit application
├── scraper.py             # Script for scraping website data
├── content_generator.py   # Logic for generating structured articles
├── uniqueness_checker.py  # Hash-based uniqueness checker
├── latest_policies.txt    # File where scraped data is stored
├── uniqueness_log.txt     # File where unique article hashes are logged
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Streamlit App
The Streamlit app allows you to scrape data, generate articles, and ensure content uniqueness. Here's an overview of the key sections:
- Scrape Data: Scrapes the latest data from Business Today.
- Generate Article: Automatically generates a well-structured article and displays it on the page.
- Uniqueness Check: Ensures that no duplicate articles are generated, using hash-based content comparison.

## Project Files

- #### app.py
Main Streamlit application that integrates scraping, article generation, and uniqueness checking into a user-friendly interface.

- #### scraper.py
Handles scraping of website data. Retrieves article links, summaries, and metadata from the target website.

- #### content_generator.py
Generates structured articles from the scraped data, including an introduction, key updates, and conclusion.

- #### uniqueness_checker.py
Contains the functionality to check whether an article is unique, using MD5 hashing to compare content and log new entries.






