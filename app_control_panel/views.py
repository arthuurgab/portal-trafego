from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def panel(request):
    if request.user.is_superuser:
        return render(request, "control_panel/control_panel_superuser.html")
    else:
        return render(request, "control_panel/control_panel.html")
