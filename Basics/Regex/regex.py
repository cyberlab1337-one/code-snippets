import re

re.search()   # znajdź pierwszy pasujący fragment | returns OBJECT
re.findall()  # znajdź wszystkie | return RESULTS
re.match()    # sprawdź początek tekstu, if no match → None
re.sub()      # zamień tekst

regex_email = r"\w+@\w+.\w+"
regex_date = r"(\d{4})-(\d{2})-(\d{2})"
regex_ip = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

# \d = dowolna cyfra (0–9)
# r"" = raw string (ważne, żeby \ działał poprawnie)
# . → dowolny znak
# \w → litera lub cyfra
# \s → spacja

# POWTÓRZENIA
# + → 1 lub więcej razy
# * → 0 lub więcej razy
# .* → dowolne znaki, dowolnej długości (greedy - zachłanny) → „połknij wszystko”
# ? → zrób to w trybie „minimalnym” (non-greedy - precyzyjny) → „weź tylko tyle, ile trzeba, żeby dopasowanie się udało”
# .*? → weź jak najmniej znaków, ile potrzeba
# {n} → dokładnie n
# {n,m} → od n do m


# GRUPY
re.findall()
regex = r"\[(\d+)\]"
# bez grupy → zwraca cały match
# z grupą → zwraca tylko zawartość grupy
# (.*?) → dowolne znaki

text = "Mam 2 koty i 3 psy"

numbers = re.findall(r"\d", text)
words = re.findall(r"\w+", text)
date = re.findall(r"\[(\d{4}-\d{2}-\d{2})\]", text)
ip = re.findall(r"\[(\d+\.\d+\.\d+\.\d+)\]", text)

print(numbers)

re.search()   # znajdź pierwszy pasujący fragment | returns OBJECT
result8 = re.search(r"(\d{4})-(\d{2})-(\d{2})", date)
date = "Data: 2026-04-29"

result8.group(0)  # cały match # '2026-04-29'
result8.group(1)  # rok 
result8.group(2)  # miesiąc
result8.group(3)  # dzień


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
