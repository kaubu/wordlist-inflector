# Penn-Treebank tags:
# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

from lemminflect import getAllInflections

# >>> getAllInflections('watch')
# {
#     'NNS': ('watches', 'watch'),
#     'NN': ('watch', ),
#     'VBD': ('watched', ),
#     'VBG': ('watching', ),
#     'VBZ': ('watches', ),
#     'VB': ('watch', ),
#     'VBP': ('watch', )
# }
# type = <class 'dict'>

words = []
inflected_words = [] # Words + Inflections

# Put all words in a list
with open(
        f"./input/{input('Word list: ./input/')}", "r", encoding="utf8"
    ) as f:
    for line in f:
        words.append(line.strip())

output_name = f"./output/{input('Output file name: ./output/')}"

# Go through words, inflect them, and add to new list
for word in words:
    inflections = getAllInflections(word)
    # Check if dictionary exists (i.e., not empty)
    if not inflections:
        continue
    # print(f"debug inflections: {inflections}")

    # Iterate in key, value pairs
    for tag, new_words in inflections.items():
        # new_words = tuple ('ACTED',)
        
        for new_word in new_words:
            inflected_words.append(new_word)

# Get rid of duplicates
inflected_words = list(set(inflected_words))

with open(output_name, "w", encoding="utf8") as f:
    for word in inflected_words:
        f.write(f"{word}\n")