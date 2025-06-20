"""
emails.py
Estimate: 40 minutes
Actual:  minutes
"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)

def extract_name_from_email(email):
    """Get username from email address."""
    username = email.split('@')[0]
    name_parts = username.replace('.', ' ').split()
    name = ' '.join(name_parts).title()
    return name

main()