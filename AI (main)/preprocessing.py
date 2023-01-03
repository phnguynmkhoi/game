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

EMBEDDING_DIM = 400 # HOW BIG IS EACH WORD VECTOR
MAX_VOCAB_SIZE = 10000 # HOW MANY UNIQUE WORDS TO USE
MAX_SEQUENCE_LENGTH = 300 # MAX NUMBER OF WORDS IN A COMMENT TO USE

def encode_AI(labels_input,):
    encoded_labels_input = []
    for label_input in labels_input:
        if label_input == -1:
            encoded_labels_input.append([1,0,0])
        else:
            encoded_labels_input.append([0,0,1])   
    encoded_labels_input = np.array(encoded_labels_input)
    return encoded_labels_input

def sequences_AI(reviews_input):
    word_reviews_input = pre_processingdata(reviews_input)
    sequences_input = Tokenizer.texts_to_sequences(word_reviews_input)
    data_input = pad_sequences(sequences_input, maxlen=MAX_SEQUENCE_LENGTH)
    return data_input