import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

# Combine all symptom columns into a single column
df["symptoms"] = df.iloc[:, 1:].apply(lambda x: ' '.join(x.dropna()), axis=1)
 
# Keep only necessary columns
df = df[["symptoms", "Disease"]]

# Rename for consistency
df.rename(columns={"Disease": "disease"}, inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("✅ Dataset cleaned & saved as 'cleaned_dataset.csv'")
