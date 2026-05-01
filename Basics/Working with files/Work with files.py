from pathlib import Path
from collections import Counter
import string

BASE_DIR = Path(__file__).parent
path_to_file = BASE_DIR / "text.txt"

# count lines

with open(path_to_file, "r", encoding = "utf-8") as file:
    count = sum(len(line.split() for line in file if line.strip()))

with open(path_to_file,"r",encoding="utf-8") as file:
    count = sum(1 for line in file if line.strip())

# count words

words = []
word_count = {}

with open(path_to_file,"r",encoding="utf-8") as file:
    word_count = sum(len(line.split()) for line in file)

with open(path_to_file, "r", encoding = "utf-8") as file:
    for line in file:
        for word in line.lower().split():
            clean = word.strip(string.punctuation)
            if clean:
                words.append(clean)
    
    counter = Counter(words)
    most_common_word, count = counter.most_common(1)[0]

print("Amount of lines:", count)
print("Amount of words:", word_count)

with open (path_to_file, "r", encoding = "utf-8") as file:
    for line in file:
        for word in line.lower().strip():
            word_count[word] = word_count.get(word,0) + 1

most_word = max(word_count, key=word_count.get)
            