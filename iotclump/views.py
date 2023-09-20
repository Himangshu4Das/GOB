from django.shortcuts import render

def iotclump_view(request):
    return render(request, 'iotclump/iotclump.html')