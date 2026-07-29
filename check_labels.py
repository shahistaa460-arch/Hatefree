import pandas as pd

df = pd.read_csv("data/hinglish/train.txt", sep="\t")

for label in sorted(df["label"].unique()):
    print(f"\n===== LABEL {label} =====")
    samples = df[df["label"] == label]["text"].head(10)
    for i, text in enumerate(samples, 1):
        print(f"{i}. {text}")