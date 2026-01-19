import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def process_influencer_with_gpt(raw_data):
    try:
        influencer_summary = {
            "name": raw_data.get('nickName', 'Unknown'),
            "description": raw_data.get('description', ''),
            "stats": {
                "subscribers": raw_data.get('fanNum', 0),
                "avg_views": raw_data.get('avgViewNum', 0),
                "engagement": raw_data.get('interactiveRate', 0)
            },
            "country": raw_data.get('countryName', 'Unknown')
        }

        prompt = f"""
        You are a professional Influencer Marketing Manager for a high-end Perfume brand.
        Analyze the following influencer data:
        {json.dumps(influencer_summary)}

        Task:
        1. Extract/Confirm their Name.
        2. Calculate Engagement Rate (format as percentage).
        3. Write a SHORT, hyper-personalized outreach email (max 100 words). 
           - Mention specific details from their description or stats to prove you looked at them.
           - Tone: Professional, warm, exclusive.
        
        Output format: JSON only.
        {{
            "name": "...",
            "engagement_rate": "...",
            "email_draft": "..."
        }}
        """

        # 3. 调用 GPT-4o
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a data extraction and copywriting assistant. Output valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        
        return {
            "Name": result.get("name"),
            "Platform": "YouTube",
            "Followers": int(influencer_summary['stats']['subscribers']),
            "Engagement Rate": result.get("engagement_rate"),
            "Email Draft": result.get("email_draft"),
            "Status": "To Contact"
        }

    except Exception as e:
        print(f"❌ GPT Processing Error: {e}")
        return None
