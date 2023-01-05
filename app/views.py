from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.contrib.auth.decorators import login_required
from .forms import submitPaymentpage

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Dr. Yeoh.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'ABC System',
            'message':'This application processes ...',
            'year':datetime.now().year,
        }
    )

def cfopage(request):
    """Renders the CFO Page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cfopage.html',{
            
        }
    )

def subPayPage(request):
    """Renders the Submit Payment Page"""
    assert isinstance(request, HttpRequest)
    form = submitPaymentPage()
    return render(
        request,
        'app/submitPaymentPage.html',
        {"form" :form}
    )

@login_required
def menu(request):
    # in database this can potentially be used to differentiate different actors
    check_employee = request.user.groups.filter(name='employee').exists()
    context = {
            'title':'Main Menu',
            'is_employee': check_employee,
            'year':datetime.now().year,
        }
    context['user'] = request.user

    return render(request,'app/menu.html',context)


