from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def tools(request):
    if request.method == 'POST':
        #     uppercase = request.POST.get('uppercase', 'off')
        #     lowercase = request.POST.get('lowercase', 'off')
        #     camelcase = request.POST.get('camelcase', 'off')
        #     removepunc = request.POST.get('removepunc', 'off')
        #     countwords = request.POST.get('countwords', 'off')
        #     removenewline = request.POST.get('removenewline', 'off')
        #     removespace = request.POST.get('removespace', 'off')
        #     removenum = request.POST.get('removenum', 'off')
        #     countfrequency = request.POST.get('countfrequency', 'off')
        # {'uppercase': uppercase, 'lowercase': lowercasecase, 'camelcase': camelcase, 'removepunc': removepunc, 'countwords': countwords,
        #     'removenewline': removenewline, 'removespace': removespace, 'removeenum': removenum, 'countfrequency': countfrequency}
        # if uppercase == "on":
        #     params = {'text': "uppercase", 'flag': 1}
        #     return render(request, 'input.html', {'params': params})
        # elif lowercase == "on":
        #     text = "lowercase"
        #     return render(request, 'input.html', {'params': text, 'flag': 1})
        # elif camelcase == "on":
        #     text = "camelcase"
        #     return render(request, 'input.html', {'params': text, 'flag': 1})
        # elif removepunc == "on":
        #     text = "removepunc"
        #     return render(request, 'input.html', {'params': text, 'flag': 1})
        # elif countwords == "on":
        #     text = "countword"
        #     return render(request, 'input.html', {'params': text, 'flag': 1})
        # elif removenewline == "on":
        #     text = "removenewline"
        #     return render(request, 'input.html', {'params': text, 'flag': 1})
        # elif removespace == "on":
        #     text = "removespace"
        #     return render(request, 'input.html', {'params': text, 'flag': 1})
        # elif removenum == "on":
        #     text = "removenum"
        #     return render(request, 'input.html', {'params': text, 'flag': 1})
        # elif countfrequency == "on":
        #     text = "countfrequency"
        return render(request, 'input.html')
    else:
        return render(request, 'tools.html')


def input(request, text):
    if request.method == "GET":
        messages.info(request, "Change to Uppercase")
        return render(request, 'input.html', {'text1': text})
    if request.method == "POST":
        djtext = request.POST['txtarea']
        if text == "uppercase1":
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            return render(request, 'input.html', {'purpose': 'Changed to Uppercase',
                                                  'analyzed_text': analyzed, 'flag': 1, 'text1': text})
        if text == "uppercase":
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            return render(request, 'input.html', {'purpose': 'Changed to Uppercase',
                                                  'analyzed_text': analyzed, 'flag': 1, 'text1': text})

        if text == "lowercase":
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.lower()
            return render(request, 'input.html', {'purpose': 'Changed to Lowercase',
                                                  'analyzed_text': analyzed, 'flag': 1, 'text1': text})

        if text == "removepunc":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char

            return render(request, 'input.html', {'purpose': 'Removed Punctuations',
                                                  'analyzed_text': analyzed, 'flag': 1, 'text1': text})

        if text == "extraspaceremover":
            analyzed = ""
            for index, char in enumerate(djtext):
                # It is for if a extraspace is in the last of the string
                if char == djtext[-1]:
                    if not(djtext[index] == " "):
                        analyzed = analyzed + char

                elif not(djtext[index] == " " and djtext[index+1] == " "):
                    analyzed = analyzed + char

            return render(request, 'input.html', {'purpose': 'Removed Extra spaces',
                                                  'analyzed_text': analyzed, 'flag': 1, 'text1': text})

        if text == "newlineremover":
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char

            return render(request, 'input.html', {'purpose': 'Removed NewLines',
                                                  'analyzed_text': analyzed, 'flag': 1, 'text1': text})

        if text == "numberremover":
            analyzed = ""
            numbers = '0123456789'

            for char in djtext:
                if char not in numbers:
                    analyzed = analyzed + char

            return render(request, 'input.html', {'purpose': 'Removed Numbers',
                                                  'analyzed_text': analyzed, 'flag': 1, 'text1': text})


def feedback(request):
    return render(request, 'feedback.html')
