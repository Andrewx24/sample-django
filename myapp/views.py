from django.http import HttpResponse  # Import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World")  # Return an HTTP response
