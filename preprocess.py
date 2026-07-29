import pandas as pd

# ----------------------------
# Load Hinglish Dataset
# ----------------------------
hinglish = pd.read_csv("data/hinglish/train.txt", sep="\t")

# Keep only required columns
hinglish = hinglish[["text", "label"]]

# Convert labels:
# 0 = Non-Hate
# 1 = Hate
# 2 = Hate

hinglish["label"] = hinglish["label"].replace({
    0: 1,
    1: 1,
    2: 0
})

# ----------------------------
# Load Manglish Dataset
# ----------------------------
manglish = pd.read_excel("data/manglish.xlsx")

# Rename comment -> text
manglish = manglish.rename(columns={"comment": "text"})

# Keep only required columns
manglish = manglish[["text", "label"]]

# ----------------------------
# Merge datasets
# ----------------------------
dataset = pd.concat([hinglish, manglish], ignore_index=True)

# Remove duplicates
dataset.drop_duplicates(inplace=True)

# Remove empty rows
dataset.dropna(inplace=True)

# Shuffle dataset
dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)

# Save final dataset
dataset.to_csv("data/final_dataset.csv", index=False)

print("Dataset Created Successfully!")
print(dataset.head())

print("\nDataset Shape:")
print(dataset.shape)

print("\nLabel Distribution:")
print(dataset["label"].value_counts())