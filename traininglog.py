#!/usr/bin/python3

import pandas as pd

df = pd.read_csv('Training Log - Log.csv', header=1)
df = df.drop(0)
print(df)
