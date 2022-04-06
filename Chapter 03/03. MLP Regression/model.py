import torch
import torch.nn.functional as F
from torch import nn
from torchsummary import summary


# YOUR CODE HERE

class Network(nn.Module):
    def __init__(self, input):
        super(Network, self).__init__()
        self.input_layer = nn.Linear(input, 32)
        self.hidden1 = nn.Linear(32, 16)
        self.hidden2 = nn.Linear(16, 8)
        self.output = nn.Linear(8, 1)

    def forward(self, x):
        first_layer = self.input_layer(x)
        act1 = F.relu(first_layer)
        second_layer = self.hidden1(act1)
        act2 = F.relu(second_layer)
        third_layer = self.hidden2(act2)
        act3 = F.relu(third_layer)
        output = self.output(act3)
        x = F.relu(output)
        return x
