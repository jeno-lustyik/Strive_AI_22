import numpy as np
import numpy.random as rnd
import itertools
import os
import sys

import pandas as pd
import scipy.misc
import random

import torch
from sklearn.preprocessing import StandardScaler

import torch as T
from torch import nn
import torch.nn.functional as F
from torch.optim import Adam, SGD
from torchsummary import summary
from torch.autograd import Variable

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('data_akbilgic.csv')


class Recurrent_Net(nn.Module):

    def __init__(self, in_size, hid_size, n_layers, batch_size, seq_length):
        super(Recurrent_Net, self).__init__()
        self.batch_size = batch_size
        self.n_layers = n_layers
        self.hidden_size = hid_size

        self.rnn = nn.RNN(in_size, hid_size, n_layers, batch_first=True)
        self.fc = nn.Linear(hid_size, seq_length)

    def forward(self, x):
        h_0 = T.zeros((self.n_layers, self.batch_size, self.hidden_size))

        _, h_n = self.rnn(x, h_0)
        last_hidden = h_n[-1]
        out = F.relu(self.fc(last_hidden))

        return out


def train_test_split(df):
    df.drop('date', axis=1, inplace=True)
    df_train = df[0:int(df.shape[0] * 0.8)]
    df_test = df[int(df.shape[0] * 0.8):]

    return df_train, df_test


def next_stock_batch(batch_size, n_steps, df_base):
    t_min = 0
    t_max = df_base.shape[0]

    feats = df_base.iloc[:, -8:].values
    random_seeds = np.random.randint(0, len(df_base) - n_steps - 1, batch_size)

    x = []
    y = []
    for i in random_seeds:
        sequence = df_base.iloc[i:i + n_steps, -8:]
        target = df_base.iloc[i + 1:i + n_steps + 1, -1]

        x.append(sequence), y.append(target)

    return np.array(x), np.array(y)


df_train, df_test = train_test_split(df)

iters = 5

n_layers = 100
in_size = 8
hid_size = 15
batch_size = 32
seq_len = 20

model = Recurrent_Net(in_size, hid_size, n_layers, batch_size, seq_len)
criterion = nn.MSELoss()
optim = torch.optim.SGD(model.parameters(), lr=0.003)

train = []
test = []

for i in range(iters):
    running_train_loss = 0

    # Train X & Y
    train_x, train_y = next_stock_batch(batch_size, seq_len, df_train)

    train_x, train_y = torch.tensor(train_x).float(), torch.tensor(train_y).type(torch.float32)

    optim.zero_grad()

    preds = model.forward(train_x)

    train_loss = criterion(preds, train_y)
    train_loss.backward()
    optim.step()

    running_train_loss += train_loss.item()

    avg_train_loss = running_train_loss / batch_size
    train.append(avg_train_loss)

plt.plot(train, label='Train Loss')
plt.show()
