from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="your api key")

# Scrape a website:
scrape_result = app.scrape_url('website url', formats=['markdown', 'html'])
print(scrape_result)