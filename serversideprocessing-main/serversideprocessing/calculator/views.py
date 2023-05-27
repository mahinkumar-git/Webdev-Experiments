from django.shortcuts import render
# Create your views here.

def index(request):
    if request.method == 'POST':
        try:
            num1 = int(request.POST['num1'])
            num2 = int(request.POST['num2'])
        except ValueError:
            return render(request,'index.html',{'result':'Enter a valid number!'})
        if 'add' in request.POST:
            return render(request,'index.html',{'result':num1+num2})
        elif 'mul' in request.POST:
            return render(request,'index.html',{'result':num1*num2})
        elif 'sub' in request.POST:
            return render(request,'index.html',{'result':num1-num2})
        elif 'div' in request.POST:
            try:
                return render(request,'index.html',{'result':num1/num2})
            except ZeroDivisionError:
                return render(request,'index.html',{'result':'Cannot divide by zero!'})
        elif 'pow' in request.POST:
            return render(request,'index.html',{'result':num1**num2})
    return render(request,"index.html")
