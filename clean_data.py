import pandas as pd
df = pd.read_csv('data.csv')

df = df.drop_duplicates(subset=['email'], keep='first')
df['has_joined_event'] = df['has_joined_event'].str.strip().str.lower().map({
    'yes': True,
    'no': False
})


linkedin_col = 'What is your LinkedIn profile?'

def is_valid_linkedin(link):
    if pd.isna(link):
        return False
    s = str(link).strip().lower()
    return s.startswith('http') and 'linkedin.com' in s

df['linkedin_missing_or_incomplete'] = ~df[linkedin_col].apply(is_valid_linkedin)

df['job_title_missing'] = df['Job Title'].apply(lambda x: pd.isna(x) or str(x).strip() == '')

df.to_csv('cleaned_output.csv', index=False)
