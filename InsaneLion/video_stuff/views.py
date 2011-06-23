from django.http import HttpResponse
# Create your views here.
def default_view(request):
    origHost = request.get_host()
    return HttpResponse(origHost)
    return HttpResponse('Hello World...')
