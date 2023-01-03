import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from preprocessing import pre_processingdata
from preprocessing import encode_AI
from preprocessing import sequences_AI
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer

EMBEDDING_DIM = 400 # HOW BIG IS EACH WORD VECTOR
MAX_VOCAB_SIZE = 10000 # HOW MANY UNIQUE WORDS TO USE
MAX_SEQUENCE_LENGTH = 300 # MAX NUMBER OF WORDS IN A COMMENT TO USE

review_list = [['Game như con cặc',0],['tệ',0],['Hay',0],['Vui hợp lý luôn',0],['ổn áp',0]]
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

cnn_model = keras.models.load_model("AI.h5")
prediction = cnn_model.predict(data_input)

for i in range (0,4):
    print(reviews_input[i])
    print(np.argmax(prediction[i]))