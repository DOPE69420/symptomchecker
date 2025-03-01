from django.http import JsonResponse
import pandas as pd
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
from django.http import JsonResponse
import json
import joblib

# Load ML model globally
model = joblib.load("path/to/model.pkl")  

def predict_disease(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            symptoms = data.get("symptoms", "").lower()  # Convert to lowercase for consistency
            print("Received Symptoms:", symptoms)

            if not symptoms:
                return JsonResponse({"error": "No symptoms provided"}, status=400)

            # 🔥 Model Prediction
            prediction = model.predict([symptoms])  # Ensure model supports text input
            print("Model Prediction:", prediction)

            return JsonResponse({"prediction": prediction[0]})

        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
