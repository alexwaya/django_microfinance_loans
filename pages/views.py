from django.shortcuts import render


def index_view(request):
    context = {
        
    }
    return render(request, 'pages/index.html', context)