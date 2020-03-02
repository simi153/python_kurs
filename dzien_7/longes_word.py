import string


def clean(text):
    znaki = string.ascii_lowercase + "ąćęłóńśźż- "
    uniq_text = set(text)
    for znak in uniq_text:
        if znak not in znaki:
            text = text.replace(znak, "")
    return text


with open("pliki/dane/pan-tadeusz.txt", encoding="utf8") as f:
    text = f.read().lower()
    for el in "\n\\/:":
        text = text.replace(el, " ")
    text = clean(text)
    text = set(text.split())
    dlugosci = {slowo: len(slowo) for slowo in text}
    print(sorted(dlugosci.items(), key=lambda x:x[1], reverse=True))