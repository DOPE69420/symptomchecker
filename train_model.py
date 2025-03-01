import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# ✅ Load Dataset
df = pd.read_csv("dataset.csv")  # Ensure this file exists
print(df.head())  # Debugging: Check if CSV is correct

# ✅ Combine Symptoms into a Single Column
df["symptoms_combined"] = df.iloc[:, 1:].astype(str).agg(" ".join, axis=1)

# ✅ Convert Symptoms to Features (Vectorization)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["symptoms_combined"])  # Convert text to numbers
y = df.iloc[:, 0]  # First column is Disease

# ✅ Train Model
model = MultinomialNB()
model.fit(X, y)

# ✅ Save Model & Vectorizer in Django Project
MODEL_DIR = "ml_models"
os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(model, os.path.join(MODEL_DIR, "disease_model.pkl"))
joblib.dump(vectorizer, os.path.join(MODEL_DIR, "vectorizer.pkl"))

print("✅ Model Trained & Saved Successfully in 'ml_models/'")
