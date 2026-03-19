import numpy as np

data = np.array([10, 20, 30, 40])
print(np.mean(data))
print(np.var(data))
print(np.std(data))

print(np.max(data))
print(np.min(data))

data2 = data * 2
print(np.mean(data2))