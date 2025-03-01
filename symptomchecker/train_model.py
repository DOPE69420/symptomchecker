import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# ✅ Load Dataset
df = pd.read_csv("cleaned_dataset.csv")   # Make sure this file exists
print(df.head())  # Debugging: Check if CSV is correct

# ✅ Check CSV Columns
if "symptoms" not in df.columns or "disease" not in df.columns:
    raise ValueError("CSV file must have 'symptoms' and 'disease' columns.")

# ✅ Convert Symptoms to Features (Vectorization)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["symptoms"])  # Convert text to numbers
y = df["disease"]  # Target (Disease names)

# ✅ Train Model
model = MultinomialNB()
model.fit(X, y)

# ✅ Save Model & Vectorizer in Django Project
MODEL_DIR = "ml_models"
os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(model, os.path.join(MODEL_DIR, "disease_model.pkl"))
joblib.dump(vectorizer, os.path.join(MODEL_DIR, "vectorizer.pkl"))

print("✅ Model Trained & Saved Successfully in 'ml_models/'")
