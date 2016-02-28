import traceback
from django.http import HttpResponse
from authorise import Authorise

def interface(request):
    try:
        instance_authorise = Authorise(request)
        if instance_authorise.check_signature():
           retrurn wx_authorise_response(request) 
    except Exception as e:
        print traceback.format_exc()
    return HttpResponse('check signatrue failed')


def wx_authorise_response(request):
    response = request.GET.get('echostr')
    return HttpResponse(response)


