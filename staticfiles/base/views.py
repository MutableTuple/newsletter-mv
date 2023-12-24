from django.shortcuts import render
from .models import Newsletter, Page
from .forms import  EmailForm

# Create your views here.
def HomeNewsletter(request):
    form = EmailForm()
    context={"form":form}
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
        
        
    return render(request, "base/signup_page.html", context=context)

def single_page_view(request):
    # Get the page object from the database
    page, created = Page.objects.get_or_create(title='homepage')

    # Increment the view count
    page.views += 1
    
    # Save the updated page object
    page.save()

    context = {'page': page}
    return render(request, 'base/signup_page.html', context)