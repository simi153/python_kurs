def by_name(item):
    return int(item[0].split("-")[1])


emaile = {}

with open("dane/emails.txt") as data, open("dane/cleaned_emails.txt", "w") as emails:
    for email in data:
        if len(email.split("@")) == 2:
            login, adress = email.strip().lower().split("@")
            emaile[login] = adress
    for login, adress in sorted(emaile.items(), key=by_name):
        emails.write(f"{login}@{adress}\n")

with open("dane/cleaned_emails.txt") as ce:
    for email in ce:
        print(email[:-1])
