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
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation not in ["", "y"]:
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Get name from email address"""
    username = email.split('@')[0]
    name_parts = username.replace('.', ' ').split()
    name = ' '.join(name_parts).title()
    return name


main()
