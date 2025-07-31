# app/email_reader.py

from imapclient import IMAPClient
import email
from email.header import decode_header
import osa

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def fetch_unread_emails():
    with IMAPClient(EMAIL_HOST) as client:
        client.login(EMAIL_USER, EMAIL_PASS)
        client.select_folder("INBOX", readonly=True)

        messages = client.search(["UNSEEN"])
        summaries = []

        for uid, message_data in client.fetch(messages, ["RFC822"]).items():
            raw_email = message_data[b"RFC822"]
            msg = email.message_from_bytes(raw_email)

            subject = decode_header(msg["Subject"])[0][0]
            subject = subject.decode() if isinstance(subject, bytes) else subject
            from_ = msg.get("From")

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode(errors="ignore")
                        break
            else:
                body = msg.get_payload(decode=True).decode(errors="ignore")

            summaries.append({
                "uid": uid,
                "from": from_,
                "subject": subject,
                "body": body
            })

        return summaries
