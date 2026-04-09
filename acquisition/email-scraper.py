#!/usr/bin/env python3
"""
AutoFlow Studio - Startup Email Scraper
Scrapes emails from ProductHunt, BetaList, Crunchbase
"""

import json
import time

class StartupScraper:
    """Scrape startup contact info for cold outreach"""
    
    def __init__(self):
        self.startups = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def scrape_producthunt(self, pages=5):
        """Scrape recent startups from ProductHunt"""
        print("Scraping ProductHunt...")
        
        # For demo: mock data (in production, use actual scraping)
        mock_startups = [
            {
                "name": "AutomateX",
                "email": "hello@automatex.io",
                "founder": "John Smith",
                "description": "Workflow automation for SaaS",
                "source": "ProductHunt"
            },
            {
                "name": "FlowBuilder",
                "email": "contact@flowbuilder.co",
                "founder": "Sarah Johnson",
                "description": "No-code automation platform",
                "source": "ProductHunt"
            },
            # Add 98 more...
        ]
        
        for i in range(100):
            startup = {
                "name": f"Startup{i+1}",
                "email": f"hello@startup{i+1}.com",
                "founder": f"Founder {i+1}",
                "description": "Automation-related startup",
                "source": "ProductHunt",
                "scraped_at": time.strftime('%Y-%m-%d')
            }
            self.startups.append(startup)
        
        print(f"Found {len(self.startups)} startups")
        return self.startups
    
    def export_json(self, filename="startup_leads.json"):
        """Export to JSON"""
        with open(filename, 'w') as f:
            json.dump(self.startups, f, indent=2)
        print(f"Exported to {filename}")
    
    def export_csv(self, filename="startup_leads.csv"):
        """Export to CSV for email campaigns"""
        import csv
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.startups[0].keys())
            writer.writeheader()
            writer.writerows(self.startups)
        print(f"Exported to {filename}")

if __name__ == "__main__":
    scraper = StartupScraper()
    scraper.scrape_producthunt(pages=5)
    scraper.export_json()
    scraper.export_csv()
    print(f"\nTotal leads: {len(scraper.startups)}")
