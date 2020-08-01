from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Deal
# Create your views here.

# def index(request):
# 	return HttpResponse("Hello World.")

def index(request):
	deal = Deal.objects
	return render(request, 'deals/index.html', {'deals': deal})

def register(request):
	deal = Deal.objects
	return render(request, 'deals/register.html', {'deals': deal})

def contact(request):
	deal = Deal.objects
	return render(request, 'deals/contact.html', {'deals': deal})

def detail(request, deal_id):
	deal_detail = get_object_or_404(Deal, pk=deal_id)
	return render(request, 'deals/detail.html', {'dealdetail': deal_detail})	
