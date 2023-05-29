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

with open(input("Word list: ./input/"), "r") as f:
    pass

inflections = getAllInflections('watch')