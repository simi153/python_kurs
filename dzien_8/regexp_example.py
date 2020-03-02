import re

poczt_pattern = re.compile("\d\d-\d\d\d")
email_pattern = re.compile("[\w-]+@\w+(?:\.\w+)+")
data_pattern = re.compile("\d{2} \w{3} \d{4}")
def pattern(template):
    return re.compile(template)


with open("../dzien_7/pliki/dane/input.txt", encoding="utf8") as text:
    kody_pocztowe = poczt_pattern.findall(text.read())
with open("../dzien_7/pliki/dane/input.txt", encoding="utf8") as text:
    emaile = email_pattern.findall(text.read())
with open("../dzien_7/pliki/dane/input.txt", encoding="utf8") as text:
    daty = data_pattern.findall(text.read())

print("Kody pocztowe")
print(kody_pocztowe)
print("Emaile:")
print(emaile)
print("Daty:")
print(daty)
