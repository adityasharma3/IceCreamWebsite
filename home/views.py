from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable' : 'this is sent'
    }
    return render(request , 'index.htm' , context)

def about(request):
    return HttpResponse("about page")

def services(request):
    return HttpResponse("services page")

def contact(request):
    return HttpResponse("contact page")
    