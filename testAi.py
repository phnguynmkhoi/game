import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import pandas as pd
import numpy as np
from string import digits
from pyvi import ViTokenizer
from keras.preprocessing.text import Tokenizer

EMBEDDING_DIM = 400 # HOW BIG IS EACH WORD VECTOR
MAX_VOCAB_SIZE = 10000 # HOW MANY UNIQUE WORDS TO USE
MAX_SEQUENCE_LENGTH = 300 # MAX NUMBER OF WORDS IN A COMMENT TO USE

def responseChat(review_list):
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
  #sua review_list
  # review_list = [["Game hay vai",0],["Game hay",0],["Không ổn cho lắm",0],["Chán",0]]
  # print(type(review_list))
  data_input = pd.DataFrame(review_list, columns = ['Text', 'Label'])

  labels_input = data_input.iloc[:, 1].values
  reviews_input = data_input.iloc[:, 0].values

  data_input = pre_processingdata(reviews_input)

  encoded_labels_input = []
  for label_input in labels_input:
    if label_input == -1:
      encoded_labels_input.append([1,0,0])
    else:
      encoded_labels_input.append([0,0,1])   
  encoded_labels_input = np.array(encoded_labels_input)
  labels_input = encoded_labels_input

  word_reviews_input = pre_processingdata(reviews_input)
  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(word_reviews_input)
  sequences_input = tokenizer.texts_to_sequences(word_reviews_input)
  data_input = pad_sequences(sequences_input, maxlen=MAX_SEQUENCE_LENGTH)

  cnn_model = keras.models.load_model(".\AI_final.h5")
  prediction = cnn_model.predict(data_input)

  #Xuat predic
  happiness=0
  for i in range (1,len(review_list)):
    print(reviews_input[i])
    print(np.argmax(prediction[i]))
    happiness += np.argmax(prediction[i])-1
  if len(review_list) > 1:
    happiness=happiness/(len(review_list)-1)
    if -0.2<happiness<0.2:
      return 0
    elif happiness>=0.1:
      return 1
    else :
      return -1
  else:
    return 0

