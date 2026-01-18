import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # --- API Keys ---
    AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
    AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
    AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")
    
    # --- Wotohub Headers (Anti-Scraping) ---
    # Real headers to mimic a browser visit
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    # --- Business Logic Thresholds ---
    # Standard metrics for "Luxury/Niche" perfume brands
    VIP_THRESHOLD = {"engagement": 0.05, "followers": 50000} 
    SEED_THRESHOLD = {"engagement": 0.02, "followers": 5000}
