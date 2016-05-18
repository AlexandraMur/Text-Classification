'''
    Module for training classificator
'''

import math
import normalization
import db

def get_weights(common_words, category):
    weights = list()
    common_weight = sum([v for k, v in common_words])

    for key, value in common_words:
        term_frequency = value / common_weight

        number_documents_in_category, Number_documents = normalization.get_frequency_of_word(key, category)
        inverse_document_frequency = math.log2(Number_documents / number_documents_in_category)

        weights.append(('"'+key+'"', term_frequency * (1 if inverse_document_frequency == 0 else inverse_document_frequency)))

    print(weights)
    return weights



def train(common_words, category, is_new=False):
    if (is_new):
        db.create_new_category(category)

    words_and_weights = get_weights(common_words, category)
    db.set_category_data(category, words_and_weights)
