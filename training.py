import json
from collections import OrderedDict

'''
    Special files need for training system.
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
    Train function. Fills categories and dictionary files
'''
def train(common_words, category, is_new=False):
    category_json = categories[category]
    if is_new is True:
        for word, number in common_words:
            print(word, number)
            category_json[word] = number

        categories[category] = json.dumps(category_json)

        with open("categories.json", 'w') as categories_file:
            json.dump(categories, categories_file)
    else:
        # common_weight = sum([number for word, number in common_words])
        for word, number in common_words:
            if word in categories[category]['words'].items():
                categories[category]['words'].items()[word] = (categories[category]['words'].items() + number)/2
            else:
                categories[category]['words'].items()[word] = number