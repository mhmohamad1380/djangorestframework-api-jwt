from django.http import HttpResponse
from django.shortcuts import redirect
from .permissions import IsSuperuser
from rest_framework.viewsets import *
from rest_framework.generics import *
from rest_framework.parsers import JSONParser
from django.views.generic import TemplateView
from main.models import Email, Food
from .serializers import FoodsSerializer
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class HomePage(TemplateView):
    template_name = "HomePage.html"

class FoodAPIList(ListAPIView):
    parser_classes = [JSONParser]
    queryset = Food.objects.all()
    serializer_class = FoodsSerializer
    permission_classes = [AllowAny]
    search_fields = ['title']
    filter_backends = [SearchFilter,OrderingFilter]

class FoodAPIRetrieveDestroy(RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication,]
    queryset = Food.objects.all()
    serializer_class = FoodsSerializer
    permission_classes = [IsSuperuser]

def add_email(request):
    if request.method == "POST":
        email = request.POST['email']
        is_exists = Email.objects.filter(email__iexact=email).exists()
        if is_exists:
            return HttpResponse("this email has been added before")
        Email.objects.create(email=email)
        return redirect("/")