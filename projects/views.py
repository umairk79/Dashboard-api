from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import config
import time
from django.core.mail import send_mail
# Create your views here.


class projects(APIView):

    def get(self, request):
        send_mail('mail subject', 'body content', 'kuh282930@gmail.com',
                  ['khanumair7910@gmail.com'], fail_silently=False)
        return Response(config.projects)

class login(APIView):

    def post(self, request):
        print(request.POST)
        bob_ids = ["10320", "10321", "10322", "10820"]
        return Response(bob_ids)


class envIdentifier(APIView):
    def post(self, request):
        bob_id = request.data['bobId']
        env = request.data['env']
        config.projects['GL'][bob_id]['env'] = env
        config.projects['SL'][bob_id]['env'] = env
        print(config.projects['GL'][bob_id])
        return Response(config.projects['GL'][bob_id])
