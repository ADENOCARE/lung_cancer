import os
import base64
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from decouple import config  # Import config from python-decouple
import google.generativeai as genai

# Configure Google Gemini API using the API key from the .env file
genai.configure(api_key=config("GOOGLE_GENAI_API_KEY"))

def encode_image(image_path):
    """Encodes an image file to base64 format."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def analyze_image(image_path, prompt="Analyze this chest X-ray for lung cancer."):
    """Sends an image along with a prompt to Google Gemini API for analysis."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    encoded_image = encode_image(image_path)
    response = model.generate_content([
        {"mime_type": "image/png", "data": encoded_image},
        {"text": prompt}
    ])
    return response.text

from django.shortcuts import render

def index(request):
    return render(request, 'app1/index.html')

def home(request):
    return render(request, 'app1/home.html')

def symptom_checker(request):
    return render(request, 'app1/symptom_checker.html')

def lung_analysis(request):
    if request.method == "POST" and request.FILES.get("xray"):
        xray = request.FILES["xray"]
        fs = FileSystemStorage()
        file_path = fs.save(xray.name, xray)
        file_path = fs.path(file_path)

        try:
            result = analyze_image(file_path)
            os.remove(file_path)  # Clean up the uploaded file
            return render(request, "app1/lung_analysis.html", {"analysis_result": result})
        except Exception as e:
            messages.error(request, f"Error analyzing image: {e}")
            return redirect("lung_analysis")

    return render(request, "app1/lung_analysis.html")

def community(request):
    return render(request, 'app1/community.html')
