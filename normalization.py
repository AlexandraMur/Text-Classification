from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
import string

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
    return [w.lower() for w in words if not (w in stop_words or w in string.punctuation)]


'''
    Common function for text normalizing: tagging, deleting stopwords and punctuation signs
    Returns a list of a tuple of the most common words and it's number.
'''
def normalize_text(name_of_file):
    with open(name_of_file, encoding='utf-8') as file:
        corpora = file.read()

    filtered_text = deleting_stop_words_and_punctuating(corpora)
    return detect_most_common_words(filtered_text)
