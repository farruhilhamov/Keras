import os 
import numpy as np
import re
from numpy.core.defchararray import count
from numpy.core.fromnumeric import size
from tensorflow.keras.preprocessing import sequence
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.layers import Dense, SimpleRNN, Input, Embedding, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences


with open('train_data_true' ,'r',encoding='utf-8') as f:
    texts_true = f.readlines()
    texts_true[0] = texts_true[0].replace('\ufeff','') #убираем первый невидимый символ

with open('train_data_false' ,'r',encoding='utf-8') as f:
    texts_false = f.readlines()
    texts_false[0] = texts_true[0].replace('\ufeff','') #убираем первый невидимый символ

texts = texts_true + texts_false
count_true = len(texts_true)
count_false = len(texts_false)
total_lines = count_true+count_false

print(count_true,count_false,total_lines)


maxWordsCount = 1000
tokenizer = Tokenizer(num_words=maxWordsCount,filters='!–"—#$%&amp;()*+,-./:;<=>?@[\\]^_`{|}~\t\n\r«»',lower=True,split=' ',char_level=False)
tokenizer.fit_on_texts(texts)

dist = list(tokenizer.word_counts.items())
print(dist[:10])
print(texts[0][:100])

max_text_len = 10
data = tokenizer.texts_to_sequences(texts)
data_pad = pad_sequences(data, maxlen=max_text_len)
print(data_pad)

print( list(tokenizer.word_index.items()) )


X = data_pad
Y = np.array([[1, 0]]*count_true + [[0, 1]]*count_false)
print(X.shape, Y.shape)

indeces = np.random.choice(X.shape[0],size=X.shape[0],replace=False)
X = X[indeces]
Y = Y[indeces]

model = Sequential()
model.add(Embedding(maxWordsCount, 128, input_length=max_text_len))
model.add(LSTM(128,return_sequences=True))
model.add(LSTM(64))
model.add(Dense(2,activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', metrics=['accuracy'],optimizer=Adam(0.0001))

history = model.fit(X, Y, batch_size=32, epochs=50)

reverse_world_map = dict(map(reversed,tokenizer.word_index.items()))

def sequence_to_text(list_of_indices):
    words = [reverse_world_map.get(letter) for letter in list_of_indices]
    return words 

t = 'Не доверяй никому'.lower()
data = tokenizer.texts_to_sequences([t])
data_pad = pad_sequences(data,maxlen=max_text_len)
print(sequence_to_text(data[0]))

res = model.predict(data_pad)
if res[0][0] >= res[0][1]:
    rslt = 'Positive'
else: 
    rslt = 'Negative'
print(res,rslt,np.argmax(res),sep='\n')