from django.shortcuts import render

def panel(request):
    return render(request, "control_panel/control_panel.html")
