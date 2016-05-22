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

        number_documents_in_category, Number_documents = normalization.get_frequency_of_word_among_all(key, category)
        inverse_document_frequency = math.log2((Number_documents / number_documents_in_category if number_documents_in_category != 0 else 1) if Number_documents/number_documents_in_category != 0 else 1)

        weights.append(('"'+key+'"', term_frequency * (1 if inverse_document_frequency == 0 else inverse_document_frequency)))

    print(weights)
    return weights

def compare_weight(weights, category):
    state, weights_from_db = db.get_category_data(category)

    if state is False:
        return

    weights_from_db = dict(weights_from_db)
    weights_ = dict(weights.copy())

    for key, value in weights:
        key_ = key.split('"')[1]
        try:
            value_from_db = weights_from_db[key_]
            if value_from_db != value:
                weights_[key] = (value + value_from_db) / 2
        except Exception:
            continue

    return list(weights_.items())

def train(common_words, category, is_new=False):
    if (is_new):
        db.create_new_category(category)

    words_and_weights = get_weights(common_words, category)
    words_and_weights = compare_weight(words_and_weights, category)
    db.set_category_data(category, words_and_weights)
