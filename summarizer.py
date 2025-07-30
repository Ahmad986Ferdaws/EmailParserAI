# app/summarizer.py

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_email(subject: str, body: str):
    prompt = f"""
You are an AI email assistant. Summarize the following email and assign a category 
(e.g., Work, Billing, Social, Spam, Reminder, Notification).

Subject: {subject}

Body:
{body[:2000]}

Return a JSON with fields: summary, category
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
