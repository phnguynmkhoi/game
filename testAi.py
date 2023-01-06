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
  # review_list = [["Game chán vãi",0],["Game hay",0],["Không ổn cho lắm",0],["Chán",0]]
  data_input = pd.DataFrame(review_list, columns = ['Text', 'Label'])

  labels_input = data_input.iloc[:, 1].values
  reviews_input = data_input.iloc[:, 0].values

  encoded_labels_input = []
  for label_input in labels_input:
    if label_input == -1:
      encoded_labels_input.append([1,0,0])
    else:
      encoded_labels_input.append([0,0,1])   
  encoded_labels_input = np.array(encoded_labels_input)
  
  reviews_processed = []
  unlabeled_processed = []

  for review in reviews_input:
    review_cool_one = ''.join([char for char in review if char not in digits])
    reviews_processed.append(review_cool_one)

  word_reviews = []
  all_words =[]
  for review in reviews_processed:
    review = ViTokenizer.tokenize(review.lower())
    word_reviews.append(review.split())

  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(word_reviews)
  sequences_input = tokenizer.texts_to_sequences(word_reviews)
  data_input = pad_sequences(sequences_input, maxlen=MAX_SEQUENCE_LENGTH)
  labels_input = encoded_labels_input

  cnn_model = keras.models.load_model(".\AI_final.h5")
  prediction = cnn_model.predict(data_input)

  #Xuat predic
  happiness=0
  reviewtemp=reviews_input
  for i in range (1,len(review_list)):
    b=reviewtemp[i].split(" ")
    for j in b:
      if j in ["chán", "Chán", "Xui", "xui", "dở", "Dở", "tệ", "Tệ", "cặc", "buồi", "lồn"]:
        print(j)
        happiness+=-1
        break
      elif j in ["Hên", "hên","tuyệt", "vời", "haha"]:
        print(j)
        happiness+=1
        break
      else:
        happiness += np.argmax(prediction[i])-1
        break
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

# responseChat("a")