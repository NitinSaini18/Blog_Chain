from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse



def index(request):
    return HttpResponseRedirect(reverse("App_Blog:blog_list"))
