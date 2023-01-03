import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from preprocessing import encode_AI
from preprocessing import sequences_AI
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer
import tensorflow as tf
import pandas as pd
import numpy as np
from string import digits
from collections import Counter
from pyvi import ViTokenizer
from gensim.models.word2vec import Word2Vec
from keras.utils.np_utils import to_categorical
import re
import matplotlib.pyplot as plt
import string
import random
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer 

EMBEDDING_DIM = 400 # HOW BIG IS EACH WORD VECTOR
MAX_VOCAB_SIZE = 10000 # HOW MANY UNIQUE WORDS TO USE
MAX_SEQUENCE_LENGTH = 300 # MAX NUMBER OF WORDS IN A COMMENT TO USE

def pre_processingdata(reviews):
  reviews_processed = []
  for review in reviews:
    review_good_one = ''.join([char for char in review if char not in digits])
    reviews_processed.append(review_good_one)
  word_reviews = []
  clean_reviews = []
  for review in reviews_processed:
    review = ViTokenizer.tokenize(review.lower())
    word_reviews.append(review)
  
  for statement in word_reviews:
    clean = []
    for w in statement.split():
      new_w = w.translate(str.maketrans('','','!#$%^&*<>?./:;"["]{\}_-+='))
      if (new_w!=''):
        clean.append(new_w)
    clean_reviews.append(clean)
  return clean_reviews

review_list = [["Lạy chúa game quá chán",0],["Lạy chúa game quá chán",0],["Lạy chúa game quá chán",0],["Lạy chúa game quá 1chán",0]]
data_input = pd.DataFrame(review_list, columns = ['product_name', 'price'])

labels_input = data_input.iloc[:, 1].values
reviews_input = data_input.iloc[:, 0].values

data_input = pre_processingdata(reviews_input)

labels_input = encode_AI(labels_input)

word_reviews_input = pre_processingdata(reviews_input)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(word_reviews_input)
sequences_input = tokenizer.texts_to_sequences(word_reviews_input)
data_input = pad_sequences(sequences_input, maxlen=MAX_SEQUENCE_LENGTH)

cnn_model = keras.models.load_model(".\AI (main)\AI_3.h5")
prediction = cnn_model.predict(data_input)

for i in range (0,5):
    print(reviews_input[i])
    print(np.argmax(prediction[i]))