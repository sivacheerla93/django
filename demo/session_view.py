from django.shortcuts import render, HttpResponse, HttpResponseRedirect


def languages(request):
    if 'langs' in request.session:
        langs = request.session['langs']
    else:
        langs = []

    if request.method == "POST":
        lang = request.POST["lang"]
        langs.append(lang)
        request.session["langs"] = langs

    print(langs)
    return render(request, 'demo/languages.html', {'langs': langs})


def clear(request):
    del request.session["langs"]
    return HttpResponse("Languages cleared!!")
