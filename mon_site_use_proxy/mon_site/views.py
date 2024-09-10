from django.shortcuts import redirect, render

def home(request):
    current_path = request.get_full_path()
    print(current_path)
    if "ticket" in current_path:
        ticket = current_path.split("ticket=")[1]
        print(ticket)
        return render(request, "mon_site/AfterLog.html")
    return render(request, "mon_site/LogPage.html")


def login(request):
    # Quand on clique sur se connecter, appel du CAS ave le service en paramètre
    MonServeur= "https://testclientcas.onrender.com/"
    CasServer = "https://mamacas1.onrender.com/"
    return redirect(CasServer + "cas/login?service=" + MonServeur)