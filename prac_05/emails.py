"""
emails.py
Estimate: 40 minutes
Actual:  minutes

"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)

def get_name_from_email(email):
    """get username from email address."""
    username = email.split('@')[0]
    name_parts = username.replace('.', ' ').split()
    name = ' '.join(name_parts).title()
    return name

main()