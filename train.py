# We set the seed value with a constant number to get consistent #results every time our neural network is trained.
# This is because when we create a model in Keras, it is assigned #random weights every time. Due to this, we might receive different #results every time we train our model.
# However this won't be a general issue, our training set is small, #so we take this precaution
import numpy as np
import keras
import random
from keras.models import Sequential
from keras.layers import Dense, Activation

from ai_support import simulate_ball

vel = 7
test_X = []
test_Y = []
train_X = []
train_Y = []
final_X = []
final_Y = []
for i in range(10000):
    # all these are scaled between 0 and 1
    vel_x = random.uniform(.01, .99)
    vel_y = ((vel ** 2 - (vel_x * vel) ** 2) ** .5) * (-1 if random.uniform(0, 1) > .5 else 1) / vel
    x = random.uniform(0, 1 - 1 / 25)  # the 1/25 is the % width of the ball
    y = random.uniform(0, 1 - (1 / 25))
    train_X.append([vel_x, vel_y, x, y])
    train_Y.append([simulate_ball(vel_x * vel, vel_y * vel, vel, x * 500, y * 500) / 500])
    print(train_X[-1], train_Y[-1])

for i in range(1000):
    # all these are scaled between 0 and 1
    vel_x = random.uniform(0, .99)
    vel_y = ((vel ** 2 - (vel_x * vel) ** 2) ** .5) * (-1 if random.uniform(0, 1) > .5 else 1) / vel
    x = random.uniform(0, 1 - 1 / 25)  # the 1/25 is the % width of the ball
    y = random.uniform(0, 1 - (1 / 25))
    test_X.append([vel_x, vel_y, x, y])
    test_Y.append([simulate_ball(vel_x * vel, vel_y * vel, vel, x * 500, y * 500) / 500])

for i in range(1000):
    # all these are scaled between 0 and 1
    vel_x = random.uniform(0, .99)
    vel_y = ((vel ** 2 - (vel_x * vel) ** 2) ** .5) * (-1 if random.uniform(0, 1) > .5 else 1) / vel
    x = random.uniform(0, 1 - 1 / 25)  # the 1/25 is the % width of the ball
    y = random.uniform(0, 1 - (1 / 25))
    final_X.append([vel_x, vel_y, x, y])
    final_Y.append([simulate_ball(vel_x * vel, vel_y * vel, vel, x * 500, y * 500) / 500])

test_X = np.array(test_X)
test_Y = np.array(test_Y)
train_X = np.array(train_X)
train_Y = np.array(train_Y)
final_X = np.array(final_X)
final_Y = np.array(final_Y)

# as first layer in a sequential model:
model = Sequential()
model.add(Dense(20, activation='sigmoid', input_dim=4))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

keras.layers.Dropout(.5, noise_shape=None, seed=None)

model.compile(loss='mean_absolute_error', optimizer=keras.optimizers.SGD(lr=.01, momentum=.9, nesterov=False),
              metrics=['accuracy'])
keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=20, verbose=0, mode='auto', baseline=None,
                              restore_best_weights=True)
model.fit(train_X, train_Y, epochs=70000, batch_size=5000, validation_data=(test_X, test_Y), shuffle=True)

error = 0
predicted = model.predict(final_X)

for i, x, z in zip(final_X, final_Y, predicted):
    dif = abs(x[0] - z[0])
    error = error + dif

print('validation error ', error / len(predicted), len(predicted))

model.save('pong_ai_2.h5')
