import traceback
from django.http import HttpResponse
from authorise import Authorise

def index(request):
    try:
        instance_authorise = Authorise()
        if instance_authorise.check_signature(request):
            return HttpResponse(request.GET.get('echostr'))
    except Exception as e:
        print traceback.format_exc()
    return HttpResponse('check signatrue failed')
