import re

re.search()   # znajdź pierwszy pasujący fragment
re.findall()  # znajdź wszystkie
re.match()    # sprawdź początek tekstu
re.sub()      # zamień tekst

# \d = dowolna cyfra (0–9)
# r"" = raw string (ważne, żeby \ działał poprawnie)
# . → dowolny znak
# \w → litera lub cyfra
# \s → spacja

text = "Mam 2 koty i 3 psy"

numbers = re.findall(r"\d", text)
words = re.findall(r"\w+", text)

print(numbers)

# POWTÓRZENIA
# + → 1 lub więcej
# * → 0 lub więcej
# {n} → dokładnie n
# {n,m} → od n do m

emails = "Kontakt: test@mail.com, Kontakt2: test2@gmail.com"
email_list = re.findall(r"\w+@\w+\.\w+", text)

# O: ['test@mail.com', 'test2@gmail.com']

# sprawdź czy matchuje
if re.match(r"\d+", "123abc"):
    print("Zaczyna się od liczby")
else:
    print("Nie zaczyna się od liczby")

# GRUPOWANIE
date = "Data: 2026-04-28"

match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date)
print(match.groups())

# O: ('2026', '04', '28')

# ZMIANA TEKSTU
poem = "Mam 2 koty"
new_poem = re.sub(r"\d+", "X", poem)

print(new_poem)

# O: Mam X koty

# result[0] → cały match
# result[1] → pierwsza grupa

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)

print(result)
# O: <re.Match object; span=(39, 46), match='[12345]'>
print(result[1])
# O: 12345
print(result[0])
# O: [12345]
