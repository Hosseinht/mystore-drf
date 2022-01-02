from django.shortcuts import render
from rest_framework.views import APIView
import logging
import requests

# @cache_page(5 * 60)
# def say_hello(request):
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#
#     return render(request, 'hello.html', {'name': data})

logger = logging.getLogger(__name__)


class HelloView(APIView):

    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response ')
            data = response.json()
        except request.ConnectionError:
            logger.critical('httpbin is offline')

        return render(request, 'hello.html', {'name': data})
