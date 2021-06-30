from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
# Create your views here.


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'languages/index.html'

    def get(self, request):
        queryset = Language.objects.all()
        return Response({'languages': queryset})


