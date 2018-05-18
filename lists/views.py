from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item


# Create your views here.

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
        #    else:
        #        new_item_text = ''
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
#                 {'new_item_text': new_item_text,}
