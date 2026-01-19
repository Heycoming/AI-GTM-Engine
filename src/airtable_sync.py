import os
from pyairtable import Api
from dotenv import load_dotenv

load_dotenv()

def sync_to_airtable(influencers):
    api_key = os.getenv("AIRTABLE_API_KEY")
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("AIRTABLE_TABLE_NAME")

    if not all([api_key, base_id, table_name]):
        print("Error: .env lacks Airtable configuration")
        return

    # Connect to Airtable
    try:
        api = Api(api_key)
        table = api.table(base_id, table_name)
        print(f"Connected to Airtable table: {table_name}")
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    print(f"Preparing to sync {len(influencers)} records...")

    success_count = 0
    
    for item in influencers:
        if item.get('Status') == 'Discard':
            continue

        record = {
            "Name": item.get('nickName', item.get('name', 'Unknown')),
            "Followers": int(item.get('followerCount', 0)),
            "Engagement Rate": item.get('engagementRate', 0),
            "Region": item.get('country', 'Unknown'),
            "Profile URL": item.get('homePageUrl', ''),
        }

        try:
            table.create(record)
            print(f"Synced: {record['Name']}")
            success_count += 1
        except Exception as e:
            print(f"Sync failed [{record['Name']}]: {e}")

    print(f"Sync complete! Success: {success_count}/{len(influencers)}")
