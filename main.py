import os
from src.scraper import fetch_influencers
from src.processor import process_influencer_with_gpt
from src.airtable_sync import sync_to_airtable
from dotenv import load_dotenv

load_dotenv()

def main():
    print("🤖 Starting AI-Driven GTM Engine (GPT-4o Powered)...")

    target_limit = 5 
    print(f"📡 Connecting to Wotohub to fetch {target_limit} influencers...")
    
    raw_list = fetch_influencers(keyword="perfume", max_count=target_limit)
    
    if not raw_list:
        print("❌ No data found. Check your Cookie or Network.")
        return

    print(f"📦 Successfully scraped {len(raw_list)} raw records.")

    processed_records = []
    print("🧠 Analyzing with GPT-4o...")
    
    for raw_item in raw_list:
        record = process_influencer_with_gpt(raw_item)
        if record:
            print(f"   ✨ Processed: {record['Name']}")
            processed_records.append(record)
    
    if processed_records:
        print(f"🚀 Syncing {len(processed_records)} records to Airtable...")
        sync_to_airtable(processed_records)
        print("✅ Workflow Complete!")
    else:
        print("⚠️ No records processed successfully.")

if __name__ == "__main__":
    main()
