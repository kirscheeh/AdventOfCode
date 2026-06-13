import re

with open("inputs/2015/day19.txt") as f:
    rules, word = f.read().split("\n\n")
    rules = rules.splitlines()

replacements = set()
for rule in rules:
    pattern, replacement = rule.split(" => ")
    for match in re.finditer(pattern, word):
        new_word = word[:match.start()] + replacement + word[match.end():]
        replacements.add(new_word)

print(len(replacements))