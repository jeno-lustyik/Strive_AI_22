import torch
import torch as T
import torch.nn as nn
import torch.nn.functional as F


class NeuralNet(nn.Module):

    def __init__(self, embedding_dim, hidden_dim, vocab_size, tagset_size):
        super(NeuralNet, self).__init__()
        self.hidden_dim = hidden_dim

        self.words = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)

        self.hidden2tag = nn.Linear(hidden_dim, tagset_size)

    def forward(self, x):

        h0 = torch.zeros_like()
        embeds = self.words(x)

        lstm_out, (hidden_state, cell_state) = self.lstm(embeds)
        lstm_last = hidden_state[-1]
        out = self.hidden2tag(lstm_last)

        return out

# class NeuralNet(nn.Module):
#     def __init__(self, input_size, hidden_size, num_classes):
#         super(NeuralNet, self).__init__()
#         self.l1 = nn.Linear(input_size, hidden_size)
#         self.l2 = nn.Linear(hidden_size, hidden_size)
#         self.l3 = nn.Linear(hidden_size, num_classes)
#         self.relu = nn.ReLU()
#
#     def forward(self, x):
#         out = self.l1(x)
#         out = self.relu(out)
#         out = self.l2(out)
#         out = self.relu(out)
#         out = self.l3(out)
#         # no activation and no softmax at the end
#         return out
