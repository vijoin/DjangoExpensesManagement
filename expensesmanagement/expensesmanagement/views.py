from django.shortcuts import render


def homepage(request):
    return render(request, template_name='base.html')
