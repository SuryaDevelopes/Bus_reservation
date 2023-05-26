from django.shortcuts import render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from bookTicket.models import bookAticket
from bus.models import BusInfo,BusPickArea,BusDropArea
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request,tempate_name="registration/register.html"):
    if request.method == 'POST':
        postdata=request.POST.copy()
        form = UserCreationForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username','')
            pw = postdata.get('password1','')
            from django.contrib.auth import authenticate, login
            new_user = authenticate(username=un,password=pw)
            if new_user and new_user.is_active:
                    login(request, new_user)
                    url = reverse('account:my_account')
                    return HttpResponseRedirect(url)
    else:
        form=UserCreationForm()
    
    page_title = 'Registration'
    return render(request,tempate_name,locals())

@login_required
def my_account(request, template_name="registration/my_account.html"):
    page_title = 'My Account'
    tickets = bookAticket.objects.filter(user=request.user)
    name = request.user.username
    return render(request,template_name, locals())

@login_required
def ticket_details(request,ticket_id,template_name="registration/ticketdetails.html"):
    page_title = 'Ticket details'
    tickets = get_object_or_404(bookAticket,id=ticket_id)
    bus_info = get_object_or_404(BusInfo,id=tickets.bus_id)
    bus_arrive = get_object_or_404(BusDropArea,id=bus_info.depature_at_id)
    bus_depart = get_object_or_404(BusPickArea,id=bus_info.arriving_from_id)
    name = request.user.username
    return render(request,template_name, locals())
