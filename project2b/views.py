from django.shortcuts import render


def home(request):
    context = {
        'name': 'django',
        'title': 'Django tutorials'
    }
    return render(request, 'home.html', context)


# Create your views here.
def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
# Create your views here.
