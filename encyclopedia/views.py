from django.shortcuts import redirect, render

from . import util
import re
import random
from markdown2 import Markdown 

def index(request):
    ##x = random.randrange(0,len(util.list_entries))
    txt =random.choice(util.list_entries())
    t = request.GET.get('q') if request.GET.get('q') != None else 'There is not topic with that name'
    context = {"entries":util.list_entries(), "random":txt}
    return render(request, "encyclopedia/index.html", context)

def notfound(request):
    txt =random.choice(util.list_entries())

    return render(request, 'encyclopedia/notfound.html', {'random':txt})

def search(request):

    txt =random.choice(util.list_entries())
    f = request.GET.get('q')
    t=request.GET.get('q')
    if(util.get_entry(f)):
        return redirect( 'detail', f)
    elif(f):
        c = util.search_entry(f)
        print(c)
    else:
        c ="Nothing to display"
    context = {"random":txt, "q":t, "f":f, "result": c}
    return render(request, "encyclopedia/search.html", context)

def layout(request):
    txt =random.choice(util.list_entries())
    
    context = {"random":txt}
    return render(request, "encyclopedia/layout.html", context)


def entries(request, pk):
    txt =random.choice(util.list_entries())    
    el = Markdown()
    e = el.convert(util.get_entry(pk))
    context = {"title":pk, "entry":e, "random":txt }
    return render(request, "encyclopedia/entry.html", context)


def create(request):
    txt =random.choice(util.list_entries())    

    if (request.method == 'POST'):
        title = request.POST.get('title')
        content = request.POST.get('content')

        if (util.get_entry(title)==None):
            util.save_entry(title, content)
            return redirect("detail", title)
        else:
            return redirect("duplicate")
        
    return render(request, "encyclopedia/create.html", {"random":txt})

def duplicate(request):
    txt =random.choice(util.list_entries())    

    return render(request,"encyclopedia/exist.html", {"random":txt})

def edit(request, pk):
    txt =random.choice(util.list_entries())    

    if (request.method == "POST"):
        title = pk
        content = request.POST.get('content')
        util.save_entry(pk, content)
        return redirect("detail", title)
    return render(request, "encyclopedia/edit.html", {"otitle":pk, "random":txt, "oentry":util.get_entry(pk)})


def delete(request, pk):
    if(request.method == "POST"):
        util.delete_entry(pk)
    return redirect("index")





