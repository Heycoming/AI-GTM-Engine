import pandas as pd
from .config import Config

class DataProcessor:
    def process(self, data_list: list) -> pd.DataFrame:
        """
        Enriches raw data with 'Status' and 'Email Draft'.
        """
        df = pd.DataFrame(data_list)
        
        # Apply Logic
        df['Status'] = df.apply(self._classify_tier, axis=1)
        df['Email Draft'] = df.apply(self._generate_email, axis=1)
        
        # Rename columns to match Airtable Schema exactly
        df = df.rename(columns={
            "name": "Influencer Name",
            "followers": "Followers",
            "engagement_rate": "Engagement Rate",
            "region": "Region",
            "profile_link": "Profile URL"
        })
        
        return df

    def _classify_tier(self, row):
        """
        Segmentation Strategy:
        - VIP: High Engagement (>5%) + High Reach (>50k) -> Full Bottle
        - Seed: Good Engagement (>2%) -> Sample
        """
        eng = row.get('engagement_rate', 0)
        followers = row.get('followers', 0)

        if eng >= Config.VIP_THRESHOLD['engagement'] and followers >= Config.VIP_THRESHOLD['followers']:
            return "VIP_Full_Bottle"
        elif eng >= Config.SEED_THRESHOLD['engagement']:
            return "Seed_Sample"
        else:
            return "Discard"

    def _generate_email(self, row):
        """Generates a Professional outreach email based on tier."""
        name = row['name']
        
        if row['Status'] == "VIP_Full_Bottle":
            return (
                f"Subject: Exclusive Partnership Opportunity: [Brand] x {name}\n\n"
                f"Dear {name},\n\n"
                "I hope this email finds you well. We have been following your content regarding luxury fragrances "
                "and admire your sophisticated analysis.\n\n"
                "We would be honored to send you our full-size signature collection for your review. "
                "Please let us know if you are interested in a potential collaboration.\n\n"
                "Best,\n[Your Name]"
            )
        elif row['Status'] == "Seed_Sample":
            return (
                f"Subject: Discovery Set for {name}\n\n"
                f"Dear {name},\n\n"
                "We loved your recent video! We believe our new scent profile aligns perfectly with your taste. "
                "We'd love to send you a complimentary discovery set—no strings attached.\n\n"
                "Best,\n[Your Name]"
            )
        return "N/A"
