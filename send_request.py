
import numpy as np
import requests

n = 20
n2 = 5 # to generate anomalies
data = np.append(np.random.normal(2, 1, [n, 2]), np.random.normal(12, 4, [n2, 2]), axis=0)
shuffled = np.random.shuffle(data)

res = requests.post('http://localhost:5000/v2/classify', json={'data': data.tolist()})
if res.status_code != 200:
    print('Error:', res.status_code)
else:
    print(res.json())

