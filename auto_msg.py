import pandas as pd
import os
import json
import re

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

df[['email', 'message']].to_csv("custom_messages.csv", index=False)

def sanitize_filename(email):
    filename = email.replace('@', '_at_').replace('.', '_')
    return re.sub(r'[\\/*?:"<>|]', '', filename)

os.makedirs("user_messages_txt", exist_ok=True)
os.makedirs("user_messages_json", exist_ok=True)

for _, row in df.iterrows():
    filename_base = sanitize_filename(row['email'])
    
    with open(f'user_messages_txt/{filename_base}.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(row['message'])
    
    with open(f'user_messages_json/{filename_base}.json', 'w', encoding='utf-8') as json_file:
        json.dump({"email": row['email'], "message": row['message']}, json_file, indent=2)


