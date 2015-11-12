# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response
from books.models import Books,Author
#####################################################################
def Show(request):
    books_l = Books.objects.all()
    c = Context({"book_list":books_l})
    return render_to_response("home.html",c)
    
def Delete(request):
    if 'b_isbn' in request.GET:
        d_isbn = request.GET["b_isbn"]
        Books.objects.get(ISBN=d_isbn).delete()
        return HttpResponseRedirect('/home/')
        
def Search(request):
    if request.POST:
        a_id = request.POST["target"]
        auth = Author.objects.filter(Name=a_id)
        b_l = []
        for a in auth:
            b_l.extend(Books.objects.filter(AuthorID=auth))
        tr_fo = [auth,b_l]
        c = Context({"trfo":tr_fo})
        return render_to_response("search.html",c)
        
def Add1(request):
    if request.GET:
        a_id = request.GET["a_id"]
        a_na = Author.objects.get(AuthorID = a_id).Name
        al = [a_id,a_na]
        c = Context({"l":al})
    return render_to_response("add.html",c)
    
def Add(request):
    if request.POST:
        post = request.POST
        auth = Author.objects.get(AuthorID = post['aid'])
        b = Books(ISBN=post['is'],Title=post['tit'],AuthorID=auth,Publisher=post['pb'],Publisher_Date=post['pbd'],Price=post['pri'])
        b.save()
        return Search(request)
        
def Delete1(request):
    if request.GET:
        a_id = request.GET['a_id']
        Author.objects.get(AuthorID=a_id).delete()
        return HttpResponseRedirect('/home/')
        

def Delete2(request):
    if request.POST:
        b_id = request.POST['b_isbn']
        Books.objects.get(ISBN=b_id).delete()
        return Search(request)
        
def Add2(request):
    return render_to_response("add1.html")

def Add3(request):
    if request.POST:
        post = request.POST
        a = Author(AuthorID=post['aid'],Name=post['target'],Age=post['age'],Country=post['coun'])
        a.save()
        return Search(request)
        
def Inform(request):
    if request.GET:
        b_is = request.GET['b_is']
        b = Books.objects.get(ISBN=b_is)
        c = Context({"book":b})
        return render_to_response("inform.html",c)
