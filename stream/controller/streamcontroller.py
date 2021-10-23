from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view



@csrf_exempt
@api_view(['GET','POST'])
def video_upload(request):
    pass
