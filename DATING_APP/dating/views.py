from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request , 'dating/home.html')
@login_required
def dashboard(request):
    return render(request , 'dating/dashboard.html')

@login_required
def Interests(request):
    return render(request , 'dating/interests.html')

@login_required
def Pending(request):
    return render(request, 'dating/pending.html')

