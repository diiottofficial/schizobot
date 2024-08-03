import os
import json
import string

word_map : dict = {}

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

with open("all_lines.txt", "r", encoding="utf-8") as all_lines:
    for line in all_lines:
        line_list = []
        for (x1, x2) in pairwise(line.split()):
            x1 = x1.translate(str.maketrans('', '', string.punctuation)).lower()
            if x1 in word_map.keys():
                word_map[x1].append(x2)
            else:
                word_map[x1] = [x2]


with open("markovdict", "w") as out:
    json.dump(word_map, out, indent=1)