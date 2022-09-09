#from unittest import result
from django.shortcuts import render
from dropdown_graph.models import showemp

def showempnames(request):
    results = showemp.objects.all()
    return render(request, "DisplayRecords.html", {"showemp":results})

 