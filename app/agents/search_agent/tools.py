"""Search agent tools for web search and content scraping.

This module provides tools for the search agent to perform web searches and scrape
website content. It includes functions for searching the web using DuckDuckGo
and scraping text content from websites.

The tools are designed to be used with LangChain's tool decorator and provide
formatted, clean output suitable for AI agent consumption.

Example:
    >>> from app.agents.search_agent.tools import search_web, scrape_website
    >>> results = search_web("Python programming", 3)
    >>> content = scrape_website("https://example.com")
"""

from langchain_core.tools import tool
from ddgs import DDGS
import requests
from bs4 import BeautifulSoup


@tool
def search_web(query: str, max_results: int = 5) -> str:
    """Search the web using DuckDuckGo and return results as text.
    
    This function performs a web search using DuckDuckGo's search API and formats
    the results into a readable text format. Each result includes the title,
    description, and URL.
    
    Args:
        query: The search query string to look up on the web.
        max_results: Maximum number of search results to return. Defaults to 5.
        
    Returns:
        A formatted string containing search results with titles, descriptions, and URLs.
        Each result is numbered and includes the title, body text, and link.
        If no results are found, returns "No search results found."
        If an error occurs, returns an error message.
        
    Raises:
        Exception: If the search operation fails due to network issues or API errors.
        
    Example:
        >>> result = search_web("Python programming", 3)
        >>> print(result)
        1. Python Programming Language
        Learn Python programming with tutorials and examples...
        URL: https://python.org
        
        2. Python Tutorial
        Comprehensive guide to Python programming...
        URL: https://docs.python.org
    """
    try:
        with DDGS() as ddgs_instance:
            results = list(ddgs_instance.text(query, max_results=max_results))
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


@tool
def scrape_website(url: str) -> str:
    """Scrape content from a website URL.
    
    This function fetches a webpage, parses its HTML content, and extracts
    clean text while removing scripts, styles, and other non-content elements.
    The content is limited to 2000 characters to avoid token limits.
    
    Args:
        url: The URL of the website to scrape. If the URL starts with "URL: ",
             this prefix will be automatically removed.
             
    Returns:
        A string containing the scraped text content from the website.
        The content is cleaned of HTML tags, scripts, and styles.
        Limited to 2000 characters to avoid token limits.
        If an error occurs, returns an error message.
        
    Raises:
        requests.RequestException: If the HTTP request fails (timeout, connection error, etc.)
        Exception: For other scraping-related errors.
        
    Example:
        >>> content = scrape_website("https://example.com")
        >>> print(content[:100])
        Example Domain
        This domain is for use in illustrative examples...
    """
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


# List of available tools for the search agent
search_agent_tools = [search_web, scrape_website]
