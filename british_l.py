# To find verbs that use either an -l- or -ll-, and prioritize -ll-
# E.g. leveled and levelled -> levelled

# Linux

# .*[aeiou]ling\n – Gerund or Present Participle

# .*[aeiou]led\n – Simple Past tense
# Windows

# .*[aeiou]ling\r\n – Gerund or Present Participle

# .*[aeiou]led\r\n – Simple Past tense

import re

GERUND_RULE = r"(?:.*[aeiou]ling\n)"
GERUND_REPLACE = r"lling\n"
PAST_TENSE_RULE = r"(?:.*[aeiou]led\n)"

input_file = f"./input/{input('Input file: ./input/')}"

word_file = ""

with open(input_file, "r", encoding="utf8") as f:
    word_file = f.read()

# print(word_file)

gerund_matches = re.findall(GERUND_RULE, word_file)

print(gerund_matches)