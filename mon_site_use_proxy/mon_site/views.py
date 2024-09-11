from django.shortcuts import redirect, render

def home(request):
    if request.user.is_authenticated:
        return render(request, "mon_site/AfterLog.html")
    return render(request, "mon_site/LogPage.html")
