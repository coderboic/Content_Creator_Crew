import os
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from scrapingbee import ScrapingBeeClient
from dotenv import load_dotenv

load_dotenv()


class ScrapingBeeToolInput(BaseModel):
    """Input schema for ScrapingBeeTool."""
    url: str = Field(..., description="The URL to scrape data from.")


class ScrapingBeeTool(BaseTool):
    name: str = "Web Scraper"
    description: str = (
        "Useful for scraping web content from URLs. Returns the HTML content of the target URL."
    )
    args_schema: Type[BaseModel] = ScrapingBeeToolInput

    def _run(self, url: str) -> str:
        """Execute web scraping using ScrapingBee API."""
        client = ScrapingBeeClient(api_key=os.getenv('SCRAPING_BEE'))

        try:
            response = client.get(url)
            return f"Status: {response.status_code}\n\nContent:\n{response.content[:5000]}"
        except Exception as e:
            return f"Error scraping URL: {str(e)}"
