import torch

reloaded = torch.load('best_model.pth.tar', map_location='cpu')
torch.save(reloaded, 'cpu_model/best_model.pth.tar')