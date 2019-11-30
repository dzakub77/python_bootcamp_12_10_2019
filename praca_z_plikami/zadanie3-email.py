

with open('emails.txt') as f:
    cleaned_emails = set()
    for line in f:
        email = line.lower().strip()
        if email.count("@") == 1:
            cleaned_emails.add(email)
print(cleaned_emails)