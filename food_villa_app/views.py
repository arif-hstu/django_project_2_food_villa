from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'food_villa_app/index.html')
