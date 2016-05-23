import normalization
import training
import testing
import time


start = time.time()
common_words = normalization.normalize_text("test/sport.txt")

print("text normalize")



''' for training
training.train(common_words, "mathematics")
print(time.time() - start)

'''

''' for testing '''

testing.classify(common_words)
print(time.time() - start)