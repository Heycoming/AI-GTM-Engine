# Influencer GTM Automation Pipeline

**End-to-End Instagram Talent Discovery & Outreach System**

This repository houses a specialized **Go-To-Market (GTM) engine** designed to automate the labor-intensive process of influencer marketing. Developed to support brand product launches, this pipeline replaces manual scouting with a programmatic approach to discover, classify, and engage high-potential Instagram creators.

## Project Background

In the context of scaling a brand's product promotion, manual influencer sourcing is often the primary bottleneck. Marketing teams spend countless hours manually searching platforms, verifying engagement metrics, copying data to spreadsheets, and drafting individual outreach emails.

**The Solution:**
I engineered this automated pipeline to transform a fragmented manual workflow into a streamlined system. By inputting target keywords (e.g., "skincare," "tech setup"), the system autonomously:
1.  **Scouts** thousands of profiles via Wotohub.
2.  **Qualifies** leads based on engagement rates and follower counts.
3.  **Organizes** data into a structured CRM (Airtable).
4.  **Prepares** personalized email drafts, readying the campaign for immediate execution.

## Key Features

*   **Automated Discovery:** Implements a custom **Playwright** engine to navigate Wotohub, handling authentication, pagination, and dynamic content rendering to extract high-value influencer metrics.
*   **Smart Filtration & Classification:** Uses **Pandas** to process raw data, filtering out low-quality leads (e.g., bot accounts, low engagement) and categorizing influencers by region and niche.
*   **Outreach Readiness:** Automatically generates personalized email drafts and outreach metadata for each qualified lead, significantly reducing the time-to-contact for marketing teams.
*   **CRM Synchronization:** Synchronizes processed data with **Airtable** via API. The system employs an idempotent design to prevent duplicate records, serving as a "Single Source of Truth" for the GTM team.
*   **Stealth Extraction:** Utilizes advanced network interception techniques to capture raw JSON payloads, bypassing complex frontend anti-bot protections.

## Technical Architecture

### Core Runtime
*   **Python 3.10+**: Primary backend logic.
*   **ETL Design Pattern**: Strict separation of concerns between Extraction (Scraper), Transformation (Processor), and Loading (Airtable Sync).

### Extraction Layer
*   **Playwright**: Enterprise-grade browser automation used for rendering JavaScript-heavy interfaces.
*   **Network Interception**: Direct capture of XHR/Fetch responses to retrieve clean data structures rather than parsing unstable HTML DOM elements.

### Data Processing Layer
*   **Pandas**: High-performance data manipulation.
*   **Metric Normalization**: Custom logic to standardize numerical formats and calculate engagement ratios to score lead quality.

### Integration Layer
*   **PyAirtable**: Robust client for the Airtable REST API.
*   **Environment Security**: Strict handling of API keys and secrets via environment variables.

## Project Structure

```text
AI-GTM-ENGINE/
├── src/                     # Source Code Package
│   ├── __init__.py          # Package initialization
│   ├── scraper.py           # Playwright extraction logic (Wotohub)
│   ├── processor.py         # Data cleaning, filtering & email drafting
│   ├── airtable_sync.py     # Airtable API integration
│   └── config.py            # Configuration loader
├── main.py                  # Application entry point
├── .env.example             # Template for environment variables
├── .gitignore               # Git exclusion rules
├── requirements.txt         # Python dependencies
└── README.md                # Documentation
```

## Quick Start

### Prerequisites
*   Python 3.9 or higher
*   Airtable Account (Personal Access Token required)

### Installation

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd AI-GTM-ENGINE
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Install Browser Binaries**
    Playwright requires specific browser binaries to function.
    ```bash
    playwright install
    ```

4.  **Configuration**
    Refer to the `.env.example` file. Create a `.env` file in the root directory and populate it with your credentials:
    ```bash
    cp .env.example .env
    # Edit .env with your Airtable API Key, Base ID, and Table Name
    ```

## Usage

To initiate the pipeline, execute the main entry script. The system operates in a semi-automated mode to ensure secure authentication.

```bash
python main.py
```

**Operational Workflow:**

1.  **Authentication:** A browser instance launches automatically. Log in to the target platform manually to establish a secure session.
2.  **Handshake:** Once the login is successful, press `Enter` in the terminal. This signal triggers the automation engine to take over.
3.  **Extraction:** The engine navigates to the search module, executes queries based on brand requirements, and intercepts data streams.
4.  **Transformation & Load:** Data is processed, email drafts are generated, and the final dataset is pushed to Airtable.

## License

MIT License

> **Note:** This project serves as a technical portfolio demonstrating the automation and backend architecture designed during my **Data Operations & Database Internship**. The code has been sanitized for educational purposes and contains **no proprietary business data, sensitive internal information, or live credentials**.