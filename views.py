from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def tbe(request):
    return render_to_response('TesseractBoxEditor/tbeApp.html', context_instance=RequestContext(request));