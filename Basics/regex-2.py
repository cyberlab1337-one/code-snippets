# grep to polecenie w systemach Unix/Linux, które
# wyszukuje linie pasujące do wzorca (regex) w plikach lub strumieniu tekstu

import re

# ANCHOR CHARACTERS
# ^   → początek linii / stringa
# $   → koniec linii / stringa

# r"^Hello" - Anchor (poza nawiasami)
# r"[^a-z]" - Negacja (wewnątrz nawiasów)

text = "Hello world"

print(re.search(r"^Hello", text))  # pasuje (początek)
print(re.search(r"world$", text))  # pasuje (koniec)


def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

# CHARACTER CLASSES
# [a-z]      → jedna mała litera
# [a-z]+     → słowo z małych liter
# [a-zA-Z]   → jedna litera (mała lub duża)
# [a-zA-Z]+  → słowo (litery)
# [^a-zA-Z] → jeden znak spoza tego zakresu (negacja)

# QUALIFIERS
# ile razy coś ma się powtórzyć. Bez nich regex działa na pojedynczych znakach.
# +      → jeden lub więcej
# *      → zero lub więcej
# ?      → zero lub jeden
# {n}    → dokładnie n razy
# {n,}   → co najmniej n razy
# {n,m}  → od n do m razy

# WILDCARDS
# .      → dowolny znak (oprócz newline)
# \d     → cyfra (0–9)
# \D     → nie-cyfra
# \w     → znak słowa (litera, cyfra, _)
# \W     → nie-znak słowa
# \s     → biały znak (spacja, tab, newline)
# \S     → nie-biały znak
# ( ... )→ grupa

re.search(r"(.*[aA]){2,}", text)
# jedna litera: a lub A
# co najmniej dwa razy

print(re.search(r"p?each", "To each their own")) # p? → p is optional
# O: <_sre.SRE_Match object; span=(3, 7), match='each'>
print(re.search(r"p?each", "I like peaches"))
# O: <_sre.SRE_Match object; span=(7, 12), match='peach'>

text = "Hello 123 world"
print(re.findall(r"[a-zA-Z]", text))
# O: ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

print(re.findall(r"[a-zA-Z]+", text))
# O: ['Hello', 'world']

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# O: <_sre.SRE_Match object; span=(4, 5), match=' '>

print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
# O: <_sre.SRE_Match object; span=(30, 31), match='.'>

print(re.search(r"cat|dog", "I like cats."))
# O: <_sre.SRE_Match object; span=(7, 10), match='cat'>

print(re.search(r"Py.*n", "Python Programming"))
# O: <_sre.SRE_Match object; span=(0, 17), match='Python Programmin'>

print(re.search(r"Py[a-z]*n", "Python Programming"))
# O: <_sre.SRE_Match object; span=(0, 6), match='Python'>
print(re.search(r"Py[a-z]*n", "Pyn"))
# O: <_sre.SRE_Match object; span=(0, 3), match='Pyn'>

# one or more

print(re.search(r"o+l+", "goldfish"))
# O: <_sre.SRE_Match object; span=(1, 3), match='ol'>
print(re.search(r"o+l+", "woolly"))
# O: <_sre.SRE_Match object; span=(1, 5), match='ooll'>
print(re.search(r"o+l+", "boil"))
# O: None