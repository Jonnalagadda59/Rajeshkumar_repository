from django.shortcuts import render
from .models import UserData,FeedbackData
import datetime
date1 = datetime.datetime.now()
from django.http.response import HttpResponse
# Create your views here.
def main_page(request):
    return render(request,'main_page.html')


def home_page(request):
    return render(request,'home_page.html')


def contact_page(request):
    if request.method == "POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        mobile=request.POST.get('mobile')
        states=request.POST.get('states')
        subject=request.POST.get('subject')

        data=UserData(
        firstname=firstname,
        lastname=lastname,
        mobile=mobile,
        states=states,
        subject=subject,
        )
        data.save()
        udata=UserData()
        return render(request, 'contact_page.html',{'udata':udata})

    else:
        udata=UserData()
        return render(request, 'contact_page.html', {'udata': udata})


def feedback_page(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        work_rating = request.POST.get('work_rating', '')
        feedback = request.POST.get('feedback', '')
        data = FeedbackData(name=name,
                            work_rating=work_rating,
                            feedback=feedback,
                            date=date1)
        data.save()
        fdata = FeedbackData.objects.all()
        return render(request, 'feedback.html', {'fdata': fdata})

    else:
        fdata = FeedbackData()
        return render(request, 'feedback.html', {'fdata': fdata})


def about_page(request):
    return render(request,'about.html')