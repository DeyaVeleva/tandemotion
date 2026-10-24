from django.shortcuts import render

def home_page_view(request):

    return render(request, 'home-page/home.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)