import re

text = "User john.doe_92@example-domain.com logged in at [2026-04-29] 09:45:33 from IP [192.168.0.101]."

# EX1 - find all numbers
result = re.findall(r"\d+", text)

# EX2 - find all words, without special signs
result2 = re.findall(r"[a-zA-Z0-9@._-]+", text)

# EX3 - Find words that start with a capital letter
result3 = re.findall(r"[A-Z][a-z]+|[A-Z]+", text)

# EX4 - Take the numbers out of parentheses (groups)
result4 = re.findall(r"\[(.*?)\]", text)

# EX4B - Check if the text starts with a number
def check_sentence(text):
    if re.match(r"\d+", text):
        return "Starts with numbers"
    else:
        return "Doesn't start with numbers"

# EX5 - Check if the text starts with a number
result5 = re.sub(r"\d+", "X", text)

# EX6 - Find an email address (simple)
emails = "Kontakt: test@mail.com oraz admin@test.org"
result6 = re.findall(r"\w+@\w+.\w+", emails)

# EX7 - Select a date
date = "Data: 2026-04-29"
result7 = re.findall(r"(\d{4})-(\d{2})-(\d{2})", date)
full_date = result7[0]
year, month, day = result7[0]

# return object
result8 = re.search(r"(\d{4})-(\d{2})-(\d{2})", date)

# EX8 - Find an IP address (basics)
result9 = re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", text)

# EX9 - Mini-log (Extract: Level (ERROR), Date and IP)
log = "ERROR 2026-04-29 192.168.1.1 Connection failed"
result10 = re.findall(r"(^ERROR)\s+(\d{4}-\d{2}-\d{2})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+", log)


# print(check_sentence(text))
print(result10)
