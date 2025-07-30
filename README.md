# EmailParserAI

Connect to your inbox, auto-summarize unread emails, and classify them with GPT-4.

## Features
- Connect via IMAP
- GPT-powered summarization and categorization
- SQLite log of all parsed emails
- FastAPI interface

## Setup
1. Add `.env` with email credentials and OpenAI key
2. Install: `pip install -r requirements.txt`
3. Run: `uvicorn app.main:app --reload`
