#!/usr/bin/env python3
"""
AutoFlow Studio - Cold Email Campaign
Send personalized cold emails to startups
"""

import json
import time
from datetime import datetime

class ColdEmailCampaign:
    """Automated cold email outreach"""
    
    def __init__(self, sender_email="hello@autoflowstudio.com"):
        self.sender_email = sender_email
        self.sent = []
        self.templates = self.load_templates()
    
    def load_templates(self):
        """Load email templates"""
        return {
            "free_audit": {
                "subject": "Free automation audit for {company}",
                "body": """Hi {founder},

I came across {company} and noticed you're in the {industry} space.

Quick question: How much time does your team spend on repetitive tasks like lead gen, data entry, or email outreach?

We help startups like yours automate these workflows in 24-48 hours.

I'd love to offer a free 15-minute automation audit—we'll identify 10-20 hours/week you could save.

No strings attached. Just want to help.

Interested?

Best,
Jarvis
AutoFlow Studio
{sender_email}"""
            },
            "case_study": {
                "subject": "How we saved {similar_company} 20h/week",
                "body": """Hi {founder},

We recently helped {similar_company} (similar to {company}) automate their lead generation.

Results:
- 20 hours/week saved
- 500+ leads/month (automated)
- $0 ongoing cost

Delivery: 48 hours.

Would something similar help {company}?

Happy to share the exact setup.

Best,
Jarvis
AutoFlow Studio"""
            }
        }
    
    def personalize(self, template, lead):
        """Personalize email for lead"""
        subject = template['subject'].format(
            company=lead['name'],
            similar_company="TechStartup Inc"
        )
        
        body = template['body'].format(
            founder=lead['founder'].split()[0],  # First name
            company=lead['name'],
            industry=lead.get('description', 'tech'),
            similar_company="TechStartup Inc",
            sender_email=self.sender_email
        )
        
        return subject, body
    
    def send_campaign(self, leads, template_name="free_audit", limit=50):
        """Send cold email campaign"""
        template = self.templates[template_name]
        
        print(f"Starting campaign: {limit} emails")
        
        for i, lead in enumerate(leads[:limit]):
            subject, body = self.personalize(template, lead)
            
            # Simulate sending (in production: use SMTP or email API)
            email_record = {
                "to": lead['email'],
                "to_name": lead['founder'],
                "company": lead['name'],
                "subject": subject,
                "sent_at": datetime.now().isoformat(),
                "status": "sent"
            }
            
            self.sent.append(email_record)
            print(f"[{i+1}/{limit}] Sent to {lead['name']}")
            
            # Smart delay (avoid spam filters)
            if i < limit - 1:
                time.sleep(0.1)  # Fast for demo
        
        print(f"\nCampaign complete! {len(self.sent)} emails sent")
        return self.sent
    
    def export_report(self, filename="campaign_report.json"):
        """Export campaign report"""
        report = {
            "total_sent": len(self.sent),
            "emails": self.sent,
            "generated_at": datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"Report saved: {filename}")

if __name__ == "__main__":
    # Load leads
    with open('startup_leads.json', 'r') as f:
        leads = json.load(f)
    
    # Send campaign
    campaign = ColdEmailCampaign()
    campaign.send_campaign(leads, template_name="free_audit", limit=50)
    campaign.export_report()
