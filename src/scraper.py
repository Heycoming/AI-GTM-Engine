import requests
from bs4 import BeautifulSoup
import re
from .config import Config

class WotoScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(Config.HEADERS)

    def fetch_profile(self, html_content: str = None) -> dict:
        """
        Parses influencer data. 
        Args:
            html_content: Raw HTML string. In production, this would be fetched via requests.get().
        """
        if not html_content:
            # Fallback for demo if no HTML provided (simulating a fetch)
            return {}

        soup = BeautifulSoup(html_content, 'html.parser')
        data = {}

        try:
            # 1. Basic Info
            # Selector based on provided HTML: .blo_name_text
            name_tag = soup.find("span", class_="blo_name_text")
            data["name"] = name_tag.text.strip() if name_tag else "Unknown"

            # Extract Channel ID to build a URL
            id_tag = soup.find("span", class_="channel_id")
            channel_id = id_tag.text.replace("（频道ID：", "").replace("）", "") if id_tag else ""
            data["profile_link"] = f"https://www.youtube.com/@{channel_id}"

            # 2. Region (Next to the flag image)
            # Finding the span that contains the region text (e.g., "巴西")
            region_img = soup.find("div", class_="blo_name_box").find("img")
            if region_img:
                data["region"] = region_img.parent.find_next_sibling("span").text.strip()
            else:
                data["region"] = "Global"

            # 3. Metrics (Fans, Views, Engagement)
            # The HTML uses 'fans_box' for all three metrics. We iterate to find them.
            stats_boxes = soup.find_all("div", class_="fans_box")
            
            for box in stats_boxes:
                label = box.find("span", class_="fans_text").text.strip()
                value_str = box.find("span").text.strip() # The number is in the first span
                
                if "粉丝数" in label:
                    data["followers"] = self._parse_metric(value_str)
                elif "平均观看量" in label:
                    data["avg_views"] = self._parse_metric(value_str)
                elif "平均互动率" in label:
                    data["engagement_rate"] = self._parse_percentage(value_str)

        except Exception as e:
            print(f"⚠️ Parsing Error: {e}")
            return None

        return data

    def _parse_metric(self, value: str) -> int:
        """Handles '10.10万' (Chinese notation) or '1.5M' conversions."""
        value = value.replace(",", "")
        if "万" in value:
            return int(float(value.replace("万", "")) * 10000)
        return int(float(value))

    def _parse_percentage(self, value: str) -> float:
        """Converts '14.41%' to 0.1441"""
        return float(value.replace("%", "")) / 100
