# firecrawl_demo
This repo shows how to use firecrawl, which crawls webpages and returns results in markdown format

# Steps

1. Install package.

  ```bash
  pip install firecrawl-py
  ```

2.Scraping

  ```bash
  from firecrawl import FirecrawlApp

  app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

  # Scrape a website:
  scrape_result = app.scrape_url('website url', formats=['markdown', 'html'])
  print(scrape_result)
  ```

3. Multi-Page Scrapping

   ```bash
   from firecrawl import FirecrawlApp, ScrapeOptions
   app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
  
   # Crawl a website:
   crawl_result = app.crawl_url('https://firecrawl.dev',limit=10,scrape_options=ScrapeOptions(formats=['markdown', 'html']),)
   print(crawl_result)
   ```

**Note**
 - If you’re using cURL or async crawl functions on SDKs, this will return an ID where you can use to check the status of the crawl.

 - Check Crawl Job:
    ```bash
    crawl_status = app.check_crawl_status("<crawl_id>")
    print(crawl_status)
    ```

4. LLM Extraction
   - With LLM extraction, you can easily extract structured data from any URL. We support pydantic schemas to make it easier for you too. Here is how you to use it:
    ```bash
    from firecrawl import JsonConfig, FirecrawlApp
    from pydantic import BaseModel
    app = FirecrawlApp(api_key="<YOUR_API_KEY>")
    
    class ExtractSchema(BaseModel):
        company_mission: str
        supports_sso: bool
        is_open_source: bool
        is_in_yc: bool
    
    json_config = JsonConfig(
        schema=ExtractSchema
    )
    
    llm_extraction_result = app.scrape_url(
        'https://firecrawl.dev',
        formats=["json"],
        json_options=json_config,
        only_main_content=False,
        timeout=120000
    )
    
    print(llm_extraction_result.json)
    ```

5. Interacting with the page with Actions
   - Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.
   - It is important to almost always use the **wait** action before/after executing other actions to give enough time for the page to load.
    ```bash
    from firecrawl import FirecrawlApp

    app = FirecrawlApp(api_key="fc-YOUR_API_KEY")
    
    # Scrape a website:
    scrape_result = app.scrape_url('firecrawl.dev', 
        formats=['markdown', 'html'], 
        actions=[
            {"type": "wait", "milliseconds": 2000},
            {"type": "click", "selector": "textarea[title=\"Search\"]"},
            {"type": "wait", "milliseconds": 2000},
            {"type": "write", "text": "firecrawl"},
            {"type": "wait", "milliseconds": 2000},
            {"type": "press", "key": "ENTER"},
            {"type": "wait", "milliseconds": 3000},
            {"type": "click", "selector": "h3"},
            {"type": "wait", "milliseconds": 3000},
            {"type": "scrape"},
            {"type": "screenshot"}
        ]
    )
    print(scrape_result)
    ```
 
