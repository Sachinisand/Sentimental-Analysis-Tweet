import pandas as pd

train_df = pd.read_csv("data/raw/twitter_training.csv")
val_df   = pd.read_csv("data/raw/twitter_validation.csv")

print("Training data shape:", train_df.shape)
print("Validation data shape:", val_df.shape)

print(train_df.head())
