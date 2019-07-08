from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import operator

# function 'index' for execute index.html on home (HTML RENDER)
def index(request):
    #otomatis file 'views.py' ini secara default memanggil file yg ada  di directory 'templates'.
    #tidak user requestnya memanggil directory 'templates' lagi cukup nama directory
    # di dalam templates kita
    return render(request, 'index.html')

def count(request):
    return render(request, 'count.html')

def eggs(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    countingstr = len(fulltext)
    countword = fulltext.split()

    #print(countword)
    #mencari brp kali sebuah kata disebutkan
    worddictionary = {}
    for word in countword:
        if word in worddictionary:
            #increase
            worddictionary[word] +=1
        else:
            #add into dictionary
            worddictionary[word] = 1


    #wordpredict = {}

    #for key, value in wordkeyval.items():
    #    wordpredict = print("{}: {}".format(key, value))


    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedwords)

    return render(request, 'eggs.html', {'fulltext': fulltext, 'countstr':countingstr, 'countwrd':len(countword), 'sortedwords': sortedwords})



def about(request):
    return render(request, 'about.html')

