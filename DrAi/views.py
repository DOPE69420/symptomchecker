from django.http import JsonResponse
import pandas as pd
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import joblib
import os   






@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello from Django API!"})

def index(request):
    return render(request, 'index.html')

try:
    dataset = pd.read_csv("dataset.csv")
    dataset.fillna("", inplace=True)  # Empty values ko "" se replace kar raha hoon
except Exception as e:
    print("Error loading dataset:", e)

def normalize_symptom(symptom):
    """Normalize a symptom by replacing underscores with spaces and converting to lowercase."""
    if not isinstance(symptom, str):
        return ""
    return symptom.strip().lower().replace("_", " ")

@csrf_exempt
def get_diseases(request):
    if request.method == "GET":
        return JsonResponse({"message": "GET Request Successful!"})

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            symptoms = data.get("symptoms", [])

            if not symptoms:
                return JsonResponse({"error": "No symptoms provided"}, status=400)

            # Normalize user-input symptoms (replace spaces with underscores to match dataset)
            user_symptoms = set([normalize_symptom(symptom).replace(" ", "_") for symptom in symptoms])

            matched_diseases = []
            for _, row in dataset.iterrows():
                # Normalize dataset symptoms (replace underscores with spaces for comparison)
                disease_symptoms = set(
                    normalize_symptom(str(symptom)).replace("_", " ") 
                    for symptom in row[1:].values 
                    if str(symptom).strip()
                )

                # Convert user symptoms back to spaces for comparison
                user_symptoms_for_comparison = set(
                    normalize_symptom(s).replace("_", " ") 
                    for s in user_symptoms
                )

                if user_symptoms_for_comparison.issubset(disease_symptoms):
                    matched_diseases.append(row["Disease"])

            if matched_diseases:
                return JsonResponse({
                    "message": "Disease Found!",
                    "possible_diseases": list(set(matched_diseases))
                })
            else:
                return JsonResponse({"message": "No matching disease found."})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

# from django.http import JsonResponse
# import json

# def predict_disease(request):
#     if request.method == "POST":
#         try:
#             # Check if JSON is received
#             data = json.loads(request.body)
#             print("Received Data:", data)  # Debugging
            
#             symptoms = data.get("symptoms", "")
#             print("Extracted Symptoms:", symptoms)  # Debugging
            
#             if not symptoms:
#                 return JsonResponse({"error": "No symptoms provided"}, status=400)

#             # 🔥 Debug: Ensure model is loaded properly
#             global model
#             if not model:
#                 return JsonResponse({"error": "Model not loaded"}, status=500)

#             # 🔥 Debug: Print what is being passed to the model
#             print("Input to Model:", [symptoms])

#             # Call ML Model Here
#             prediction = model.predict([symptoms])  
#             print("Model Output:", prediction)

#             return JsonResponse({"prediction": prediction[0]})
        
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON format"}, status=400)

#         except Exception as e:
#             print("Error Occurred:", str(e))  # Debugging
#             return JsonResponse({"error": str(e)}, status=500)

#     return JsonResponse({"error": "Invalid request method"}, status=400)
import joblib

# Load the pre-trained model
model = joblib.load('ml_models/disease_model.pkl')

def predict_disease(symptoms):
    # Preprocess symptoms (e.g., converting to features the model can understand)
    features = preprocess(symptoms)
    
    # Make the prediction
    disease_prediction = model.predict([features])
    
    return disease_prediction[0]

def preprocess(symptoms):
    # This is a placeholder. You should preprocess the symptoms as per your trained model's requirements
    return symptoms

  


# Load the pre-trained model
model = joblib.load('symptom_disease_model.pkl')

def predict_disease(symptoms):
    # Preprocess symptoms (e.g., converting to features the model can understand)
    features = preprocess(symptoms)
    
    # Make the prediction
    disease_prediction = model.predict([features])
    
    return disease_prediction[0]

def preprocess(symptoms):
    # This is a placeholder. You should preprocess the symptoms as per your trained model's requirements
    return symptoms
 
import openai


openai.api_key = 'your-api-key-here'

# Load the pre-trained model
model = joblib.load('symptom_disease_model.pkl')

def get_symptom_input():
    print("Please describe your symptoms in detail.")
    symptoms = input("You: ")
    return symptoms

def predict_disease(symptoms):
    # Preprocess symptoms as per your model's requirements
    features = preprocess(symptoms)
    
    # Make the prediction
    disease_prediction = model.predict([features])
    
    return disease_prediction[0]

def preprocess(symptoms):
    # Assuming we have some preprocessing logic (e.g., feature extraction, encoding)
    return symptoms  # Example placeholder

def chat():
    print("Hello! I'm your medical assistant. I can help you understand potential health conditions based on your symptoms.")
    
    while True:
        symptoms = get_symptom_input()

        if 'exit' in symptoms.lower():
            print("Goodbye! Stay healthy.")
            break
        
        # Step 1: Predict disease from the symptoms using your model
        disease = predict_disease(symptoms)
        
        # Step 2: Ask follow-up questions (to make it conversational)
        response = f"Based on your symptoms, I think you might be experiencing {disease}. "
        response += "Would you like me to provide more details or assist with any further symptoms?"
        
        print(f"Bot: {response}")
        
        # Optional: Ask if the user wants more information or suggest seeing a doctor
        while True:
            follow_up = input("You: ").lower()
            
            if 'yes' in follow_up:
                print("Bot: I recommend you visit a healthcare provider for an accurate diagnosis. Would you like me to suggest some clinics nearby?")
                break
            elif 'no' in follow_up:
                print("Bot: Okay, take care! If you feel worse, don't hesitate to seek medical help.")
                break
            elif 'exit' in follow_up:
                print("Goodbye! Take care!")
                break
            else:
                print("Bot: I'm here to help! Let me know how I can assist you further.")
                break

