#!/usr/bin/env python3
"""
AutoFlow Studio - Cold Email Bot Demo
Automated email outreach with personalization
"""

import time
from datetime import datetime
import json

class EmailBot:
    """Automated cold email outreach bot"""
    
    def __init__(self, sender_email, sender_name):
        self.sender_email = sender_email
        self.sender_name = sender_name
        self.sent_emails = []
    
    def personalize_email(self, template, lead):
        """Personalize email template with lead data"""
        email = template
        for key, value in lead.items():
            placeholder = f"{{{key}}}"
            email = email.replace(placeholder, str(value))
        return email
    
    def send_email(self, to_email, to_name, subject, body):
        """
        Send personalized email
        Demo version - simulates sending
        """
        email_data = {
            "from": f"{self.sender_name} <{self.sender_email}>",
            "to": f"{to_name} <{to_email}>",
            "subject": subject,
            "body": body,
            "sent_at": datetime.now().isoformat(),
            "status": "sent"
        }
        
        self.sent_emails.append(email_data)
        print(f"✉️  Sent to {to_name} ({to_email})")
        return email_data
    
    def send_campaign(self, leads, template, subject_template, delay=2):
        """
        Send email campaign to multiple leads
        Includes smart delays to avoid spam filters
        """
        print(f"🚀 Starting campaign: {len(leads)} recipients")
        
        for i, lead in enumerate(leads):
            # Personalize subject and body
            subject = self.personalize_email(subject_template, lead)
            body = self.personalize_email(template, lead)
            
            # Send email
            self.send_email(
                to_email=lead['email'],
                to_name=lead['name'],
                subject=subject,
                body=body
            )
            
            # Smart delay (simulate)
            if i < len(leads) - 1:
                print(f"⏳ Waiting {delay}s before next email...")
                time.sleep(0.1)  # Fast demo
        
        print(f"\n🎉 Campaign complete!")
        print(f"📊 Emails sent: {len(self.sent_emails)}")
        return self.sent_emails
    
    def export_report(self, filename="campaign_report.json"):
        """Export campaign report"""
        report = {
            "sender": self.sender_email,
            "total_sent": len(self.sent_emails),
            "emails": self.sent_emails,
            "generated_at": datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Report saved to {filename}")
        return filename

# Demo execution
if __name__ == "__main__":
    # Setup bot
    bot = EmailBot(
        sender_email="hello@autoflowstudio.com",
        sender_name="AutoFlow Studio"
    )
    
    # Demo leads
    demo_leads = [
        {"name": "John Doe", "email": "john@startup.com", "company": "Startup Inc"},
        {"name": "Jane Smith", "email": "jane@tech.co", "company": "Tech Co"},
        {"name": "Mike Johnson", "email": "mike@agency.io", "company": "Agency IO"}
    ]
    
    # Email template
    template = """Hi {name},

I noticed {company} could benefit from automation.

We help companies like yours automate repetitive tasks in 24h.

Interested in a quick 15min call?

Best,
AutoFlow Studio"""
    
    subject = "Quick question about {company}'s workflow"
    
    # Send campaign
    bot.send_campaign(demo_leads, template, subject)
    
    # Export report
    bot.export_report()
