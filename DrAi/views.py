from django.http import JsonResponse
import pandas as pd
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

try:
    dataset = pd.read_csv("dataset.csv")
    dataset.fillna("", inplace=True)  # Empty values ko "" se replace kar raha hoon
except Exception as e:
    print("Error loading dataset:", e)


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

            # 🔥 Format Fix: Input symptoms ko lowercase aur strip karke set me convert kar
            symptoms = set([symptom.strip().lower() for symptom in symptoms])

            matched_diseases = []
            for _, row in dataset.iterrows():
                # 🔥 Dataset ke symptoms ko bhi lowercase aur strip karke set me convert kar
                disease_symptoms = set(str(symptom).strip().lower() for symptom in row[1:].values if str(symptom).strip())

                if symptoms.issubset(disease_symptoms):
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
