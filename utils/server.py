import torch

def aggregate_models(client_models):
    global_model = {}

    for key in client_models[0].keys():
        global_model[key] = sum([client[key] for client in client_models]) / len(client_models)

    return global_model
