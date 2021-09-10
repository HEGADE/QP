from django.shortcuts import render
from .forms import ProvideForm
from django.contrib import messages

# Create your views here.

# this function helps users to upload therir question papers to qpweb
def provider(request):
    if request.method=='POST':
        form = ProvideForm(request.POST or None, request.FILES)
        if form.is_valid():
            try:
                provide=form.save()
                print(provide)
                provide.name = request.user
                provide.save()
                messages.success(
                    request, 'Thank you, we will check and update it soon .')
                form = ProvideForm()
        
            except:
                messages.error(request,"something went wrong")
        else:
             messages.warning(request,  form.errors)


    providers = {
        'form': ProvideForm
    }

    return render(request, 'provides/provide.html', providers)
