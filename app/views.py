from django.shortcuts import render

# Create your views here.
def condition(request):
    #d={'A':10}
    #d={'A':111,'B':222}
    d={'A':100,'B':2000,'C':300}
    return render(request,'condition.html',context=d)
