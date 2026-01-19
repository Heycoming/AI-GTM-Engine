# AI GTM Engine

**Automated Talent Intelligence & ETL Pipeline**

The AI GTM Engine is a specialized automation system designed to streamline the discovery and management of influencer talent. By orchestrating a seamless ETL (Extract, Transform, Load) workflow, this tool converts unstructured data from **Wotohub** into actionable insights within **Airtable**, serving as a foundational component for data-driven Go-To-Market (GTM) strategies.

This project demonstrates a systems-oriented approach to solving manual data bottlenecks, leveraging browser automation and API integrations to build a scalable Talent Intelligence database.

## Key Features

*   **Wotohub Automation:** Implements a custom **Playwright** engine to navigate Wotohub, handling authentication, pagination, and dynamic content rendering to extract high-value influencer metrics.
*   **Stealth Extraction:** Utilizes advanced network interception techniques to capture raw JSON payloads directly from the source, bypassing complex frontend anti-bot protections and signature verifications.
*   **Data Engineering:** Features a robust processing layer using **Pandas** to clean, normalize, and score leads based on engagement rates and follower counts, ensuring only quality data enters the CRM.
*   **CRM Integration:** Synchronizes processed data with **Airtable** via API. The system employs an idempotent design to prevent duplicate records while updating existing profiles with fresh metrics.
*   **Modular Backend Architecture:** Built with a decoupled design pattern (Extraction, Processing, Loading), allowing for easy integration of additional data sources or AI enrichment modules (e.g., GPT-4 analysis).

## Technical Architecture

### Core Runtime
*   **Python 3.10+**: Primary backend logic.
*   **ETL Design Pattern**: Strict separation of concerns between the Scraper (Extract), Processor (Transform), and Syncer (Load).

### Extraction Layer
*   **Playwright**: Enterprise-grade browser automation used for rendering JavaScript-heavy interfaces on Wotohub.
*   **Network Interception**: Direct capture of XHR/Fetch responses to retrieve clean data structures rather than parsing unstable HTML DOM elements.

### Data Processing Layer
*   **Pandas**: High-performance data manipulation.
*   **Normalization Logic**: Custom algorithms to standardize numerical formats (e.g., converting "10k" to 10000) and calculate engagement ratios.

### Integration Layer
*   **PyAirtable**: Robust client for the Airtable REST API.
*   **Environment Security**: Strict handling of API keys and secrets via environment variables.

## Project Structure

```text
AI-GTM-ENGINE/
├── src/                     # Source Code Package
│   ├── __init__.py          # Package initialization
│   ├── scraper.py           # Playwright extraction logic (Wotohub)
│   ├── processor.py         # Data transformation & cleaning
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
    Refer to the `.env.example` file for the required configuration keys. Create a `.env` file in the root directory and populate it with your credentials:
    ```bash
    cp .env.example .env
    # Edit .env with your Airtable API Key, Base ID, and Table Name
    ```

## Usage

To initiate the pipeline, execute the main entry script. The system operates in a semi-automated mode to ensure secure authentication with Wotohub.

```bash
python main.py
```

**Operational Workflow:**

1.  **Authentication:** A browser instance launches automatically. Log in to Wotohub manually to establish a secure session.
2.  **Handshake:** Once the login is successful, press `Enter` in the terminal. This signal triggers the automation engine to take over.
3.  **Extraction:** The engine navigates to the search module, executes queries, and intercepts data streams.
4.  **Transformation & Load:** Data is processed in memory and immediately synchronized to the defined Airtable base.

## License

MIT License