from firecrawl import JsonConfig, FirecrawlApp
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("FIRECRAWL_API_KEY")

app = FirecrawlApp(api_key=api_key)

class ExtractSchema(BaseModel):
    company_mission: str
    supports_sso: bool
    is_open_source: bool
    is_in_yc: bool

json_config = JsonConfig(
    schema=ExtractSchema
)

llm_extraction_result = app.scrape_url(
    'website url',
    formats=["json"],
    json_options=json_config,
    only_main_content=False,
    timeout=120000
)

print(llm_extraction_result.json)
