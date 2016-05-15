import json
from collections import OrderedDict

'''
    Special files filled by data for getting right category.
    Categories file contains a list of topics and words with it's weights.
    Dictionary file contains a list of most common words and it's weights relative the other texts.
'''
categories = OrderedDict()
dictionary = OrderedDict()

with open("categories.json") as categories_file:
    categories = json.loads(categories_file.read(), object_pairs_hook=OrderedDict)

with open("dict.json") as dictionary_file:
    dictionary = json.loads(dictionary_file.read(), object_pairs_hook=OrderedDict)

'''
    Count weight of each needed word and mark text by one of the given category
'''
def testing(common_words):
    common_weight = sum([number for word, number in common_words])

    weight = 0
    for word, number in common_words:
        weight_from_dict = dictionary[word]
        weight += number - weight_from_dict * (common_words - 1)

    if (weight < 0):
        return "Another"

    max = 0
    for category in categories.items():
        if category["weight"] > max:
            max = category["weight"]
            name = category.item()[0]

    return name