from playwright.sync_api import sync_playwright
import time
import json

def fetch_influencers(keyword="perfume", max_count=2000):
    collected_data = []
    
    print(f" Initiating the browser... (Target: {max_count} people)")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Opening Wotohub, please prepare to log in...")
        page.goto("https://www.wotohub.com/login")

        print("\n" + "="*50)
        print("Please manually log in to Wotohub in the opened browser!")
        print("After successful login and seeing the homepage, please come back here and press [Enter] to continue...")
        print("="*50 + "\n")
        input("Finished logging in? Press Enter to continue the program -> ")

        def handle_response(response):
            if "dataService/home/search" in response.url and response.status == 200:
                try:
                    json_data = response.json()
                    if "data" in json_data and "list" in json_data["data"]:
                        new_items = json_data["data"]["list"]
                        collected_data.extend(new_items)
                        print(f"   Captured data packet: Added {len(new_items)} people | Total: {len(collected_data)}")
                except:
                    pass

        page.on("response", handle_response)

        print(f"Searching keyword: {keyword}...")
        page.goto("https://www.wotohub.com/workbenchSearch")
        page.wait_for_timeout(3000)

        try:
            page.fill("input[placeholder*='Search']", keyword) 
            page.press("input[placeholder*='Search']", "Enter")
        except:
            print("Automatic input failed, please manually enter the keyword in the browser and press Enter!")
            print("   (The program will automatically listen to the data, you just need to turn the page)")
        
        print("Starting automatic pagination...")
        page_num = 1
        
        while len(collected_data) < max_count:
            if len(collected_data) >= max_count:
                break
            
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)

            current_count = len(collected_data)
            
            try:
                next_btn = page.query_selector(".btn-next, .el-pagination__next") 
                if next_btn:
                    next_btn.click()
                else:
                    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            except:
                pass

            time.sleep(3)
            
            if len(collected_data) == current_count:
                print("Data did not increase, try scrolling again or manually click the next page...")
            
            page_num += 1

        print(f"Fetching completed! Total {len(collected_data)} records obtained.")
        browser.close()

    return collected_data[:max_count]
