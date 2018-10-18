from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print ("I'm here")
    return render(request, 'first_app/index.html')

def process(request):
    if request.method=="POST":
        if not 'count' in request.session:
           request.session['count']=1
        else:
            request.session['count']+=1
        #set the key called 'count' into a dictionary calld request.session and set the key in the dictionary to be set to one; else is used when comparing two things; elif is used more than two comparisons
        request.session['first_name']=request.POST['first_name']
        request.session['location']=request.POST['location']
        request.session['language']=request.POST['language']
        request.session['comment']=request.POST['comment']
    return redirect ('/result')

def result(request):
    return render(request, 'first_app/result.html')

def clear(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
