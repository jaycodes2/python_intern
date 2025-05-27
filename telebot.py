import pandas as pd
import os
import json
import re
import requests
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID") 
if not BOT_TOKEN:
    print("Error: BOT_TOKEN not set in environment.")
    exit()

# Read CSV
df = pd.read_csv("cleaned_output.csv")

df['linkedin_missing_or_incomplete'] = df['What is your LinkedIn profile?'].isna() | df['What is your LinkedIn profile?'].str.strip().eq('')

def generate_message(row):
    first_name = row.get('first_name', 'there')
    job_title = row.get('Job Title', '').strip() or "professional"
    joined = row.get('has_joined_event', False)
    linkedin = not row['linkedin_missing_or_incomplete']

    if joined:
        msg = f"Hey {first_name}, thanks for joining our session! As a {job_title}, we think you’ll love our upcoming AI workflow tools. Want early access?"
    else:
        msg = f"Hi {first_name}, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as a {job_title}."

    if not linkedin:
        msg += " P.S. We’d love to connect with you on LinkedIn if you’re open to it!"

    return msg

df['message'] = df.apply(generate_message, axis=1)

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f"✅ Message sent to chat_id {chat_id}")
    else:
        print(f"❌ Failed to send message to chat_id {chat_id}: {response.text}")


target_chat_id = CHAT_ID

for _, row in df.iterrows():
    send_telegram_message(target_chat_id, row['message'])
