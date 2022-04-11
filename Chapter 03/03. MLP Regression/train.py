# import the needed libraries
import time

import data_handler as dh  # yes, you can import your code. Cool!
import torch
import torch.optim as optim
import torch.nn as nn

import matplotlib.pyplot as plt
import numpy as np

from model import Network  # import your model here

# Remember to validate your model: with torch.no_grad() ...... model.eval .........model.train

model = Network(8)

pth = 'data/turkish_stocks.csv'

x_train, x_test, y_train, y_test = dh.load_data(pth)

optimizer = torch.optim.SGD(model.parameters(), lr=0.003)
criterion = torch.nn.MSELoss()

epochs = 10

start_time = time.time()

train = []
test = []

for epoch in range(epochs):
    x_train_batch, x_test_batch, y_train_batch, y_test_batch = dh.to_batches(x_train, x_test, y_train, y_test, 7)
    running_loss = 0
    running_loss_test = 0

    for n in range(x_train_batch.shape[0]):
        optimizer.zero_grad()
        pred = model.forward(x_train_batch[n])
        loss = criterion(pred, y_train_batch[n])

        loss.backward()
        optimizer.step()

        with torch.no_grad():
            test_pred = model.forward(x_test_batch)
            test_loss = criterion(test_pred, y_test_batch)

        running_loss += loss.item()
        running_loss_test += test_loss.item()
    train.append(running_loss/len(x_train_batch))
    test.append(running_loss_test/len(x_test_batch))
    print(f'{epoch + 1}/ {epochs}')

train_time = time.time() - start_time
print(f'Training time: {train_time}')

plt.plot(train, label='train Loss')
plt.plot(test, label='test Loss')

plt.legend()
plt.show()
