#!/usr/bin/env python3
"""
AutoFlow Studio - Lead Scraper Demo
Scrapes business leads from Google Maps
"""

import requests
import json
import csv
from datetime import datetime

class LeadScraper:
    """Simple lead scraper for demo purposes"""
    
    def __init__(self):
        self.leads = []
    
    def scrape_google_maps(self, query, location, limit=50):
        """
        Scrape businesses from Google Maps
        Demo version - returns mock data for portfolio
        """
        print(f"🔍 Searching: {query} in {location}")
        print(f"📊 Target: {limit} leads")
        
        # Mock data for demo (in production, use actual API)
        for i in range(limit):
            lead = {
                "name": f"Business {i+1}",
                "address": f"{i+1} Main St, {location}",
                "phone": f"+33 6 {i:02d} {i:02d} {i:02d} {i:02d}",
                "website": f"https://business{i+1}.example.com",
                "category": query,
                "rating": round(4 + (i % 10) / 10, 1),
                "scraped_at": datetime.now().isoformat()
            }
            self.leads.append(lead)
            print(f"✅ Found: {lead['name']}")
        
        return self.leads
    
    def export_csv(self, filename="leads.csv"):
        """Export leads to CSV"""
        if not self.leads:
            print("❌ No leads to export")
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.leads[0].keys())
            writer.writeheader()
            writer.writerows(self.leads)
        
        print(f"💾 Exported {len(self.leads)} leads to {filename}")
        return filename

# Demo execution
if __name__ == "__main__":
    scraper = LeadScraper()
    
    # Example: Scrape restaurants in Paris
    scraper.scrape_google_maps(
        query="restaurants",
        location="Paris, France",
        limit=50
    )
    
    # Export to CSV
    scraper.export_csv("demo_leads.csv")
    
    print("\n🎉 Demo complete!")
    print(f"📊 Total leads: {len(scraper.leads)}")
