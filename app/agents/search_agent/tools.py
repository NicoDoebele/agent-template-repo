from langchain.tools import Tool
from ddgs import DDGS
import requests
from bs4 import BeautifulSoup
import re


def search_web(query: str) -> str:
    """Search the web using DuckDuckGo and return results as text."""
    try:
        with DDGS() as ddgs_instance:
            results = list(ddgs_instance.text(query, max_results=5))
            if not results:
                return "No search results found."

            formatted_results = []
            for i, result in enumerate(results, 1):
                title = result.get('title', 'No title')
                body = result.get('body', 'No description')
                link = result.get('href', 'No URL')

                formatted_results.append(f"{i}. {title}\n{body}\nURL: {link}\n")

            return "\n".join(formatted_results)
    except Exception as e:
        return f"Search failed: {str(e)}"


def scrape_website(url: str) -> str:
    """Scrape content from a website URL."""
    try:
        # Clean the URL input - remove "URL: " prefix if present
        if url.startswith("URL: "):
            url = url[5:]

        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Get text content
        text = soup.get_text()

        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (
            phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)

        # Limit to first 2000 characters to avoid token limits
        return text[:2000] + "..." if len(text) > 2000 else text

    except Exception as e:
        return f"Failed to scrape website: {str(e)}"


search_agent_tools = [
    Tool(
        name="Search",
        func=search_web,
        description=
        "Search the web for information using DuckDuckGo. Input should be a search query."
    ),
    Tool(name="ScrapeWebsite",
         func=scrape_website,
         description=
         "Scrape content from a website URL. Input should be a valid URL.")
]
