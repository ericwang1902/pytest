from django.shortcuts import render
from django.views.generic.base import View
from .models import Brand
# Create your views here.

class brand(View):
    def get(self,request):
        brand1 = Brand()
        brand1.company_name="test"
        brand1.save()
        return render(request,"index.html")