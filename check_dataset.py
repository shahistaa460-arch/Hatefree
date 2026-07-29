import pandas as pd

print("HINGLISH DATASET")
df1 = pd.read_csv("data/hinglish/train.txt", sep="\t")
print(df1.head())
print(df1.columns)

print("\n=========================\n")

print("MANGLISH DATASET")
df2 = pd.read_excel("data/manglish.xlsx")
print(df2.head())
print(df2.columns)