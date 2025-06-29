import os
from dotenv import load_dotenv
from langchain_community.document_loaders.firecrawl import FireCrawlLoader

# Load API key from .env
load_dotenv()
api_key = os.getenv("FIRECRAWL_API_KEY")

# Correct way: use 'params' to pass options like formats, etc.
loader = FireCrawlLoader(
    url="website url",
    api_key=api_key,
    mode="scrape",  # or "crawl", "extract", etc.
    params={
        "formats": ["markdown", "html"],
        "onlyMainContent": True  # if supported
    }
)

# Load the data
docs = list(loader.lazy_load())

# Print the first document
print(docs[0].page_content[:500])  # or full content
print(docs[0].metadata)
