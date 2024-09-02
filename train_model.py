from PyNomaly import loop
import numpy as np
import pickle

n = 100
data = np.append(np.random.normal(2, 1, [n, 2]), np.random.normal(8, 1, [n, 2]), axis=0)
model = loop.LocalOutlierProbability(data, n_neighbors=10)
model.fit()

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)


