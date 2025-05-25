from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .serializers import WomenSerializer
from .models import Women
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIViewToo(APIView):
    def get(self, request):
        # lst = Women.objects.all().values()
        # return Response({'posts': list(lst)})
        w = Women.objects.all()
        return Response({'posts' : WomenSerializer(w, many=True).data})

    def post(self, request):
        new_post = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id'],
        )
        return Response({'post': model_to_dict(new_post)})