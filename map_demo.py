# Input a website and get all the urls on the website - extremely fast
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("FIRECRAWL_API_KEY")


import asyncio
from firecrawl import AsyncFirecrawlApp

async def main():
    app = AsyncFirecrawlApp(api_key)
    response = await app.map_url(
        url='website url',
        include_subdomains=True
    )
    print(response)

asyncio.run(main())
