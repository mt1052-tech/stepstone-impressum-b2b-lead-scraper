"""
StepStone.de B2B Hiring-Lead Scraper & Impressum-Extraktor (Geschäftsführer, E-Mail, Telefon) — Open-Source Lite Demo
Full real-time DACH data terminal & instant CSV/Excel export (no coding required):
-> https://valora-data-intelligence.web.app/?vertical=recruiting&utm_source=github&utm_campaign=stepstone-impressum-b2b-lead-scraper
"""
import json
from scrapling.fetchers import Fetcher

def run_demo():
    print("Loading sample DACH intelligence stream for: recruiting...")
    print("For full 24/7 enriched feeds (including Impressum CEO, Email & Phone), visit:")
    print("👉 https://valora-data-intelligence.web.app/?vertical=recruiting&utm_source=github&utm_campaign=stepstone-impressum-b2b-lead-scraper")
    with open("sample_preview.json", encoding="utf-8") as f:
        sample = json.load(f)
    for idx, row in enumerate(sample, 1):
        print(f"[{idx}] {row.get('title')} | {row.get('seller_name')} | {row.get('price_formatted')}")

if __name__ == "__main__":
    run_demo()
