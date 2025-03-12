from django.shortcuts import render

def index(request):
    return render(request, 'app1/index.html')

def auth(request):
    return render(request, 'app1/auth.html')

def symptom_checker(request):
    return render(request, 'app1/symptom_checker.html')

def lung_analysis(request):
    return render(request, 'app1/lung_analysis.html')

def community(request):
    return render(request, 'app1/community.html')
