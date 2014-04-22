from django.shortcuts import render

# Create your views here.



from havefun.models import registerModel,registerForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView

def register(request):
    

    if request.method=='POST':
        form=registerForm(request.POST)
        if form.is_valid():
            human=True
            form.save()
            return HttpResponseRedirect(reverse('havefun:thanks'))
    else:
        form=registerForm()

    return render(request,'register.html',{'form':form,})


def thanks(request):
    return render(request,'thanks.html')
"""
def listRegister(request):
    return render(request,'list.html')

"""
class listRegister(ListView):
    model=registerModel
    #context_object_name='listR'
    template_name='list.html'










































"""
from django.http import HttpResponseRedirect
from havefun.models import RegisterForm

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/havefun/thanks/')

    else:
        form=RegisterForm()

    return render(request,'register.html',{'form':form,
            })
"""


        