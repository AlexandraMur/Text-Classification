'''
    Module modifying the text data for ease of usage
'''

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
import string
import db

'''
    Returns frequency number of normalized word in text
'''
def get_word_frequency(word, text):
    filtered_text = deleting_stop_words_and_punctuating(text)
    all_words = nltk.FreqDist(filtered_text)
    return all_words.get(word)


'''
    Returns n - number of corpus texts using word and N - number from all text using this word
'''
def get_frequency_of_word_among_all(word, category):
    state1, all_files = db.get_file_names()
    state2, category_files = db.get_file_names_in_category(category)

    if state1 & state2 is False:
        return

    N = 0
    n = 0
    for file_name, file_category in all_files:
        with open(file_name, encoding='utf-8') as file:
            text = file.read()

        word_frequency = get_word_frequency(word, text)
        if word_frequency is not None and word_frequency > 0:
            N += 1
            if category in file_category:
                n += 1
    return n, N


'''
    Count most common words.
    Returns a list of a tuple of the most a twenty common words and it's number.
'''
def detect_most_common_words(text):
    all_words = nltk.FreqDist(text)

    return all_words.most_common(20)


'''
    Tokenize text and normalize each word to it's normal form for analysis
    Returns a list of normalized words
'''
def deleting_stop_words_and_punctuating(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    word_tokenize_text = word_tokenize(text)
    words = [ps.stem(lemmatizer.lemmatize(w)) for w in word_tokenize_text]
    return [w.lower() for w in words if not (w in stop_words or w in string.punctuation or w in "''" or w in '``' or w in "the" or w in 'in' or w in "'s")]


'''
    Common function for text normalizing: tagging, deleting stopwords and punctuation signs
    Returns a list of a tuple of the most common words and it's number.
'''
def normalize_text(name_of_file):
    with open(name_of_file, encoding='utf-8') as file:
        corpora = file.read()

    filtered_text = deleting_stop_words_and_punctuating(corpora)
    return detect_most_common_words(filtered_text)

