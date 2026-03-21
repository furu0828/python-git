import pandas as pd

df = pd.DataFrame({
    "age": [20, 25, 30, 35, 40],
    "income": [300, 350, 500, 650, 800]
})

df["study_time"] = [1, 2, 2, 3, 5]
print(df.corr())