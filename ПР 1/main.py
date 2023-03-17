import numpy as np
import matplotlib.pyplot as plt

random_matrix = np.random.randint(100, size=(50, 50))
ax = plt.subplot()
i = 0

while i < random_matrix.size:
    plt.bar(random_matrix.take())