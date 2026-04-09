#!/usr/bin/env python3
"""
AutoFlow Studio - Social Media Scheduler Demo
Auto-post to Twitter/X and LinkedIn
"""

from datetime import datetime, timedelta
import json

class SocialScheduler:
    """Automated social media posting scheduler"""
    
    def __init__(self):
        self.scheduled_posts = []
        self.posted = []
    
    def schedule_post(self, platform, content, post_time=None):
        """Schedule a post for specific time"""
        if post_time is None:
            post_time = datetime.now()
        
        post = {
            "id": len(self.scheduled_posts) + 1,
            "platform": platform,
            "content": content,
            "scheduled_for": post_time.isoformat(),
            "status": "scheduled"
        }
        
        self.scheduled_posts.append(post)
        print(f"📅 Scheduled: {platform} post at {post_time.strftime('%Y-%m-%d %H:%M')}")
        return post
    
    def schedule_series(self, posts, start_time=None, interval_hours=4):
        """Schedule multiple posts with intervals"""
        if start_time is None:
            start_time = datetime.now()
        
        print(f"🚀 Scheduling {len(posts)} posts...")
        
        for i, post_data in enumerate(posts):
            post_time = start_time + timedelta(hours=i * interval_hours)
            self.schedule_post(
                platform=post_data['platform'],
                content=post_data['content'],
                post_time=post_time
            )
        
        print(f"✅ {len(posts)} posts scheduled!")
        return self.scheduled_posts
    
    def post_now(self, post_id):
        """Post immediately (simulate)"""
        post = next((p for p in self.scheduled_posts if p['id'] == post_id), None)
        
        if not post:
            print(f"❌ Post {post_id} not found")
            return
        
        post['status'] = 'posted'
        post['posted_at'] = datetime.now().isoformat()
        self.posted.append(post)
        
        print(f"✅ Posted to {post['platform']}: {post['content'][:50]}...")
        return post
    
    def export_schedule(self, filename="schedule.json"):
        """Export posting schedule"""
        schedule = {
            "total_scheduled": len(self.scheduled_posts),
            "total_posted": len(self.posted),
            "posts": self.scheduled_posts,
            "generated_at": datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(schedule, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Schedule saved to {filename}")
        return filename

# Demo execution
if __name__ == "__main__":
    scheduler = SocialScheduler()
    
    # Demo posts
    demo_posts = [
        {
            "platform": "Twitter",
            "content": "🚀 Automation tip: Use webhooks to trigger workflows automatically. Save 10+ hours/week!"
        },
        {
            "platform": "LinkedIn",
            "content": "Most startups waste 40% of their time on manual tasks. Here's how we helped 50+ companies automate their workflows 👇"
        },
        {
            "platform": "Twitter",
            "content": "💡 Pro tip: Automate your lead generation. We scrape 1000+ qualified leads in under 1 hour."
        },
        {
            "platform": "LinkedIn",
            "content": "3 automation hacks that saved our clients $50k+ last month. Thread 🧵"
        }
    ]
    
    # Schedule series (every 4 hours starting now)
    scheduler.schedule_series(demo_posts, interval_hours=4)
    
    # Simulate posting first one
    scheduler.post_now(1)
    
    # Export schedule
    scheduler.export_schedule()
    
    print(f"\n🎉 Demo complete!")
    print(f"📊 Scheduled: {len(scheduler.scheduled_posts)} posts")
    print(f"✅ Posted: {len(scheduler.posted)} posts")
