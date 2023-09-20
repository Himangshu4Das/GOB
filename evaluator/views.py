from django.shortcuts import render

def evaluator_view(request):
    return render(request, 'evaluator/evaluator.html')