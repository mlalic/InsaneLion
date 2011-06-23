from django.http import HttpResponse
# Create your views here.
def default_view(request):
    return HttpResponse('Hello World...')
