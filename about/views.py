from django.shortcuts import render


def research(request):
    context = {'': ''}
    return render(request, 'about/research.html', context=context)


def bio(request):
    context = {'': ''}
    return render(request, 'about/bio.html', context=context)

