import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "age": [20, 25, 30, 35, 40],
    "income": [300, 350, 500, 650, 800]
})

plt.scatter(df["age"], df["income"])
plt.show()