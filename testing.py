'''
    Module for testing trained classificator.
    Marks text one by one of category from database using classificator algorithm
'''

import db

def count_weight(common_words, words_from_category):
    sum_w = 0
    sum_c = 0
    for word_w, weight_w in common_words:
        for word_c, weight_c in words_from_category:
            if word_w in word_c:
                sum_w += weight_w
                sum_c += weight_c
                break

    return sum_w, sum_c

def classify(common_words):
    state, categories = db.get_all_categories_names()

    if state is False:
        print("Some Errors")
        return

    F = list()
    for k, category in categories:
        state, data = db.get_category_data(category)

        if state is False:
            print("Some Errors")
            return

        sum_w, sum_c = count_weight(common_words, data)
        if sum_w * sum_c != 0:
            F.append((category, sum_w - sum_c))

    category = ''
    min = 1000

    if len(F) == 0:
        print("The category is 'another'")
        return

    for category_f, weight in F:
        if weight < min:
            category = category_f

    print("The category is ", category)