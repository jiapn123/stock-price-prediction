from tensorflow.keras import Sequential 
from tensorflow.keras.layers import Dense, LSTM, Dropout
import numpy as np
import matplotlib.pyplot as plt
import Analyzer

mk = Analyzer.MarketDB()

raw_df = mk.get_daily_price("005930","2021-01-15","2024-01-15")
# print(raw_df)

window_size = 10 # 10 rows/ days 
data_size = 5   # 5 columns / open price...

def MinMaxScaler(data):
    numerator = data - np.min(data, 0)
    denominator = np.max(data,0) - np.min(data,0)
    return numerator / (denominator  + 1e-7)

dfx = raw_df[["open","high","low","volume","close"]]
dfx = MinMaxScaler(dfx)
dfy = dfx[["close"]]

x=dfx.values.tolist()
y=dfy.values.tolist()

data_x = []
data_y = []

for i in range(len(y)-window_size):
    _x = x[i:i+window_size]
    _y = y[i+window_size] 
    data_x.append(_x)
    data_y.append(_y)
    # print(_x,"->",_y)
    
# print(len(data_x))

train_size = int(len(data_y)*0.7)
train_x = np.array(data_x[0:train_size])
train_y = np.array(data_y[0:train_size])

test_size = len(data_y)-train_size
test_x = np.array(data_x[train_size:len(data_x)])
test_y = np.array(data_y[train_size:len(data_y)])

model = Sequential()
model.add(LSTM(units=10, activation = "relu", return_sequences = True, input_shape = (window_size,data_size)))
model.add(Dropout(0.1))
model.add(LSTM(units=10, activation="relu"))
model.add(Dropout(0.1))
model.add(Dense(units=1))
model.summary()

model.compile(optimizer = "adam",loss = "mean_squared_error")
history =model.fit(train_x,train_y,epochs=60,batch_size=30)

pred_y = model.predict(test_x)
print(pred_y)


print("Tomorrow's SEC price :", raw_df.close[-1], pred_y[-1], dfy.close[-1])
print("Tomorrow's SEC price :", raw_df.close[-1] / dfy.close[-1] * pred_y[-1], 'KRW')