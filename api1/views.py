from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import studentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        print("hello1")
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        print("hello2")
        serializer =studentSerializers(data=pythondata)
        print("hello3")
        if serializer.is_valid():
            print("hello4")
            serializer.save()
            print("hello5")
            res = {'msg':'Data created'}
            print(res)
            json_data = JSONRenderer().render(res)
            return HttpResponse({'message': json_data})
