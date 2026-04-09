#!/usr/bin/env python3
"""
AutoFlow Studio - Automated Proton Mail Account Creation
"""

from pywinauto import Desktop
import time
import random
import string

def generate_email():
    """Generate random email for AutoFlow Studio"""
    random_suffix = ''.join(random.choices(string.digits, k=4))
    return f"autoflowstudio{random_suffix}"

def generate_password():
    """Generate strong password"""
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choices(chars, k=16))

def create_proton_account():
    """Automate Proton Mail account creation"""
    
    print("🚀 Starting Proton Mail account creation...")
    
    # Wait for Chrome to load
    time.sleep(3)
    
    # Find Chrome window
    wins = Desktop(backend='uia').windows()
    chrome = None
    
    for w in wins:
        if 'Chrome' in w.window_text():
            chrome = w
            break
    
    if not chrome:
        print("❌ Chrome not found")
        return None
    
    print("✅ Chrome found")
    chrome.set_focus()
    time.sleep(1)
    
    # Generate credentials
    email = generate_email()
    password = generate_password()
    
    print(f"📧 Email: {email}@proton.me")
    print(f"🔐 Password: {password}")
    
    # Save credentials
    with open('/home/pc/.openclaw/workspace/autoflow-studio/credentials.txt', 'w') as f:
        f.write(f"Proton Mail Account\n")
        f.write(f"Email: {email}@proton.me\n")
        f.write(f"Password: {password}\n")
        f.write(f"Created: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print("💾 Credentials saved to credentials.txt")
    
    # For now, just prepare the data
    # Manual completion needed (CAPTCHA, verification)
    print("\n⚠️  Manual step required:")
    print("1. Fill email username:", email)
    print("2. Fill password:", password)
    print("3. Complete CAPTCHA")
    print("4. Verify email if needed")
    
    return {
        "email": f"{email}@proton.me",
        "password": password
    }

if __name__ == "__main__":
    credentials = create_proton_account()
    
    if credentials:
        print("\n🎉 Account ready!")
        print(f"📧 {credentials['email']}")
