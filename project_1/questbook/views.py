from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    comments = Comments.objects.order_by('data_added')
    context = {
        'comments' : comments
    }
    return render(request, 'questbook/index.html', context)

