import pandas as pd  
from django.http import JsonResponse  
from django.shortcuts import render  

# CSV File Load Karna
df = pd.read_csv("symptoms.csv")  # CSV file ka naam check karle

def predict_disease_csv(request):
    if request.method == "POST":
        symptoms = request.POST.getlist("symptoms")  # User se symptoms list le rahe hain
        
        # CSV me disease find karna (Basic matching)
        matched_rows = df[df[symptoms].sum(axis=1) > 0]  # Symptoms match kar rahe hain
        
        if not matched_rows.empty:
            predicted_disease = matched_rows.iloc[0, -1]  # Last column disease hoti hai
        else:
            predicted_disease = "Disease not found"

        return JsonResponse({"predicted_disease": predicted_disease})

    return render(request, "predict.html")
