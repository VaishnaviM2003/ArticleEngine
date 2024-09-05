import datetime

def generate_structured_article(articles, topic):
    """
    Generate a structured article using the fetched articles and the given topic.
    """
    today_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    article_content = f"# {topic}\n"
    article_content += f"**Generated on:** {today_date}\n\n"
    article_content += f"### Introduction\n"
    article_content += f"The world of {topic} is rapidly evolving. In this article, we explore the latest policies as of {today_date}.\n\n"

    article_content += "### Key Updates\n"
    if articles:
        for i, article in enumerate(articles, start=1):
            title = article.get('title', 'No Title')
            summary = article.get('summary', 'No Summary Available')
            url = article.get('url', '#')
            
            article_content += f"**Update {i}:**\n"
            article_content += f"- **Title**: [{title}]({url})\n"
            article_content += f"- **Summary**: {summary}\n"
            article_content += f"- **Read more at**: [{url}]({url})\n\n"
    else:
        article_content += "No new updates found at the moment.\n"

    article_content += "### Conclusion\n"
    article_content += f"These are the most recent developments in {topic}. Stay tuned for more updates.\n"
    
    return article_content
