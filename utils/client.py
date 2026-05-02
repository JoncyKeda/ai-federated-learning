import torch
import numpy as np
from model.model import SimpleModel

def train_clients(num_clients):
    client_models = []

    for _ in range(num_clients):
        model = SimpleModel()

        # Dummy data
        x = torch.rand(10, 2)
        y = torch.rand(10, 1)

        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        loss_fn = torch.nn.MSELoss()

        for _ in range(5):
            pred = model(x)
            loss = loss_fn(pred, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        client_models.append(model.state_dict())

    return client_models
