from pyairtable import Table
from .config import Config

class AirtableSync:
    def __init__(self):
        if not Config.AIRTABLE_API_KEY:
            raise ValueError("❌ Airtable API Key is missing in .env")
            
        self.table = Table(
            Config.AIRTABLE_API_KEY, 
            Config.AIRTABLE_BASE_ID, 
            Config.AIRTABLE_TABLE_NAME
        )

    def sync_records(self, df):
        """
        Iterates through DataFrame and pushes to Airtable.
        """
        print(f"🚀 Syncing {len(df)} records to Airtable...")
        
        for _, row in df.iterrows():
            if row['Status'] == "Discard":
                continue # Skip low-quality leads
            
            record = {
                "Influencer Name": row['Influencer Name'],
                "Followers": int(row['Followers']),
                "Engagement Rate": row['Engagement Rate'], # Airtable expects 0.14 for 14%
                "Region": row['Region'],
                "Status": row['Status'],
                "Email Draft": row['Email Draft'],
                "Profile URL": row.get('Profile URL', '')
            }
            
            try:
                self.table.create(record)
                print(f"✅ Synced: {row['Influencer Name']} ({row['Status']})")
            except Exception as e:
                print(f"❌ Error syncing {row['Influencer Name']}: {e}")
