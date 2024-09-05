from datetime import datetime

def generate_structured_article(articles, topic):
    """
    This function takes a list of articles and a topic and returns a formatted string
    representing a structured article that can be displayed in the Streamlit app.
    """
    article_content = []

    article_content.append(f"### {topic}")
    article_content.append("#### Introduction")
    article_content.append(f"The world of {topic} is rapidly evolving. In this article, we explore the latest policies as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")
    
    article_content.append("#### Key Updates")
    if articles:
        for article in articles:
            article_content.append(f"- **{article['Topic Name']}**: {article['Summary']} (Read more [here]({article['Topic URL']}))")
    else:
        article_content.append("No updates available at the moment.")

    article_content.append("#### Conclusion")
    article_content.append(f"These are the most recent developments in {topic}. Stay tuned for more updates.")

    return "\n\n".join(article_content)
