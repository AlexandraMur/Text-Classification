import normalization
import training
import testing
import time


start = time.time()
common_words = normalization.normalize_text("train/maths3.txt")

training.train(common_words, "mathematics")
print(time.time() - start)

