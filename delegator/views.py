from django.shortcuts import render

def delegator_view(request):
    return render(request, 'delegator/delegator.html')